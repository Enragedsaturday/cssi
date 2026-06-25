/* =========================================================================
   CSSI Flashcards — spaced-repetition study app (vanilla JS, no build step)

   Scheduler: ts-fsrs 5.4.1, vendored UMD. Global is window.FSRS.
   Persistence: IndexedDB (DB "cssi-flashcards"), with a one-time, lossless
   migration from the legacy localStorage blob (key "cssi.flashcards.v1").
   localStorage is preserved untouched as a safety fallback, and is also the
   live store when IndexedDB is unavailable (private mode, blocked, no support).
   Migrate-by-id on deck version change: survivors keep progress, removed ids
   are dropped, new ids start as New.
   Mounts on #flashcards-app. SPA-robust: re-inits on Quartz `nav` events,
   guards against double-binding, and also runs standalone.

   No external dependencies beyond the vendored FSRS global.
   ========================================================================= */
(function () {
  "use strict";

  /* ----- ts-fsrs surface (override-confirmed: global is window.FSRS) ----- */
  var FSRS = window.FSRS;
  if (!FSRS) {
    // Scheduler script failed to load — surface a clear message at mount time.
    document.addEventListener("nav", failNoLib);
    failNoLib();
    return;
  }
  var fsrs = FSRS.fsrs;
  var createEmptyCard = FSRS.createEmptyCard;
  var Rating = FSRS.Rating;          // Manual=0, Again=1, Hard=2, Good=3, Easy=4
  var State = FSRS.State;            // New=0, Learning=1, Review=2, Relearning=3
  var TypeConvert = FSRS.TypeConvert;

  function failNoLib() {
    var el = document.getElementById("flashcards-app");
    if (!el || el.dataset.fcReady) return;
    el.dataset.fcReady = "error";
    el.textContent = "";
    el.appendChild(
      panel("error", "§", "Scheduler unavailable",
        "The FSRS scheduling library did not load. Confirm " +
        "/static/flashcards/vendor/ts-fsrs-5.4.1.umd.js is reachable, then reload.")
    );
  }

  /* ----- constants ----- */
  var KEY = "cssi.flashcards.v1";   // legacy localStorage blob key (still read for migration / fallback)
  var STORAGE_SCHEMA = 1;
  var NEW_PER_SESSION = 20;
  var SWIPE_THRESHOLD = 60;
  var DEFAULT_DECK_URL = "/static/flashcards/flashcards.json";

  /* IndexedDB names. "progress" is keyed by card id and holds the same
     serialized FSRS card record the app already uses; "meta" is a small
     key/value store for deckVersion, filter, the one-time migrated flag, etc. */
  var IDB_NAME = "cssi-flashcards";
  var IDB_VERSION = 1;
  var STORE_PROGRESS = "progress";
  var STORE_META = "meta";

  // One scheduler instance for the whole app. Fuzz spreads due dates.
  var scheduler = fsrs({ enable_fuzz: true });

  /* Per-mount controller so re-init can tear down cleanly. */
  var current = null;

  /* =======================================================================
     Legacy localStorage helpers — all wrapped so private mode / quota degrade
     to memory. Still used as the migration source and as the fallback store
     when IndexedDB is unavailable.
     ===================================================================== */
  function loadLocal() {
    try {
      var raw = localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }
  function saveLocal(s) {
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* memory-only */ }
  }
  function clearLocal() {
    try { localStorage.removeItem(KEY); } catch (e) { /* ignore */ }
  }
  function freshStorage(version) {
    return {
      storageSchema: STORAGE_SCHEMA,
      deckVersion: version,
      filter: "All",
      cards: {},
      updatedAt: new Date().toISOString()
    };
  }

  /* =======================================================================
     IndexedDB layer.

     Schema (DB "cssi-flashcards", v1):
       - object store "progress": keyed by card id; value is the serialized
         FSRS card record (the exact shape stored in state.cards[id] — due,
         stability, difficulty, reps, lapses, state, last_review,
         scheduled_days, elapsed_days, learning_steps, …).
       - object store "meta": key/value pairs { key, value }. Keys used:
         "storageSchema", "deckVersion", "filter", "updatedAt", "migrated".

     The rest of the app keeps working against the same in-memory `state`
     object ({ storageSchema, deckVersion, filter, cards:{}, updatedAt }); the
     IDB facade just hydrates that object on load and persists changes on write.
     ===================================================================== */

  function idbSupported() {
    try { return typeof indexedDB !== "undefined" && indexedDB !== null; }
    catch (e) { return false; }
  }

  function reqAsPromise(req) {
    return new Promise(function (resolve, reject) {
      req.onsuccess = function () { resolve(req.result); };
      req.onerror = function () { reject(req.error); };
    });
  }
  function txDone(tx) {
    return new Promise(function (resolve, reject) {
      tx.oncomplete = function () { resolve(); };
      tx.onerror = function () { reject(tx.error); };
      tx.onabort = function () { reject(tx.error || new Error("tx aborted")); };
    });
  }

  /* Open (and upgrade/create) the database. Rejects if IDB is unavailable or
     blocked, so callers can fall back to the localStorage path. */
  function openDB() {
    return new Promise(function (resolve, reject) {
      if (!idbSupported()) { reject(new Error("indexedDB unavailable")); return; }
      var req;
      try { req = indexedDB.open(IDB_NAME, IDB_VERSION); }
      catch (e) { reject(e); return; }
      req.onupgradeneeded = function () {
        var db = req.result;
        if (!db.objectStoreNames.contains(STORE_PROGRESS)) db.createObjectStore(STORE_PROGRESS);
        if (!db.objectStoreNames.contains(STORE_META)) db.createObjectStore(STORE_META, { keyPath: "key" });
      };
      req.onsuccess = function () { resolve(req.result); };
      req.onerror = function () { reject(req.error); };
      // Some browsers fire onblocked instead of resolving when a prior
      // connection holds an older version open; treat as a failure to open.
      req.onblocked = function () { reject(new Error("indexedDB open blocked")); };
    });
  }

  function metaGet(db, key) {
    var tx = db.transaction(STORE_META, "readonly");
    return reqAsPromise(tx.objectStore(STORE_META).get(key)).then(function (row) {
      return row ? row.value : undefined;
    });
  }

  /* Read the entire persisted state back into the in-memory blob shape. */
  function idbLoadState(db) {
    var tx = db.transaction([STORE_PROGRESS, STORE_META], "readonly");
    var progStore = tx.objectStore(STORE_PROGRESS);
    var metaStore = tx.objectStore(STORE_META);
    var out = { cards: {} };
    var pending = [];

    // Prefer getAllKeys/getAll where available; fall back to a cursor.
    if (typeof progStore.getAll === "function" && typeof progStore.getAllKeys === "function") {
      pending.push(
        Promise.all([reqAsPromise(progStore.getAllKeys()), reqAsPromise(progStore.getAll())])
          .then(function (pair) {
            var keys = pair[0], vals = pair[1];
            for (var i = 0; i < keys.length; i++) out.cards[keys[i]] = vals[i];
          })
      );
    } else {
      pending.push(new Promise(function (resolve, reject) {
        var creq = progStore.openCursor();
        creq.onsuccess = function () {
          var cur = creq.result;
          if (cur) { out.cards[cur.key] = cur.value; cur.continue(); }
          else resolve();
        };
        creq.onerror = function () { reject(creq.error); };
      }));
    }

    pending.push(reqAsPromise(metaStore.getAll ? metaStore.getAll() : null).then(function (rows) {
      (rows || []).forEach(function (row) { out[row.key] = row.value; });
    }).catch(function () { /* getAll may be absent; meta keys read individually below */ }));

    return Promise.all(pending).then(function () {
      // If getAll wasn't available for meta, fetch the keys we care about.
      if (out.storageSchema === undefined && out.deckVersion === undefined) {
        return Promise.all([
          metaGet(db, "storageSchema"), metaGet(db, "deckVersion"),
          metaGet(db, "filter"), metaGet(db, "updatedAt")
        ]).then(function (vals) {
          out.storageSchema = vals[0]; out.deckVersion = vals[1];
          out.filter = vals[2]; out.updatedAt = vals[3];
          return out;
        });
      }
      return out;
    });
  }

  /* Persist the whole in-memory state into IDB in one transaction. Used after
     reconcile/migration and on reset. */
  function idbSaveState(db, state, alsoMigratedFlag) {
    var tx = db.transaction([STORE_PROGRESS, STORE_META], "readwrite");
    var progStore = tx.objectStore(STORE_PROGRESS);
    var metaStore = tx.objectStore(STORE_META);
    progStore.clear();
    var cards = state.cards || {};
    Object.keys(cards).forEach(function (id) { progStore.put(cards[id], id); });
    metaStore.put({ key: "storageSchema", value: state.storageSchema });
    metaStore.put({ key: "deckVersion", value: state.deckVersion });
    metaStore.put({ key: "filter", value: state.filter });
    metaStore.put({ key: "updatedAt", value: state.updatedAt });
    if (alsoMigratedFlag) metaStore.put({ key: "migrated", value: true });
    return txDone(tx);
  }

  /* Persist a single card record + the updatedAt stamp (the hot path: grading). */
  function idbPutCard(db, id, record, updatedAt) {
    var tx = db.transaction([STORE_PROGRESS, STORE_META], "readwrite");
    tx.objectStore(STORE_PROGRESS).put(record, id);
    if (updatedAt != null) tx.objectStore(STORE_META).put({ key: "updatedAt", value: updatedAt });
    return txDone(tx);
  }

  /* Persist just a single meta key (e.g. the filter selection). */
  function idbPutMeta(db, key, value) {
    var tx = db.transaction(STORE_META, "readwrite");
    tx.objectStore(STORE_META).put({ key: key, value: value });
    return txDone(tx);
  }

  /* One-time, lossless migration of the legacy localStorage blob into IDB.
     Copies every card record verbatim (all FSRS fields preserved) plus the
     deck/filter meta, then sets migrated=true. localStorage is NOT cleared.
     Safe to call when there is nothing to migrate (writes an empty fresh
     state + the flag). Returns the freshly-loaded in-memory state. */
  function idbMigrateFromLocal(db, version) {
    var legacy = loadLocal();
    var seed;
    if (legacy && legacy.storageSchema === STORAGE_SCHEMA && legacy.cards) {
      // Copy verbatim — do not reshape records; preserve every FSRS field.
      seed = {
        storageSchema: STORAGE_SCHEMA,
        deckVersion: legacy.deckVersion != null ? legacy.deckVersion : version,
        filter: legacy.filter || "All",
        cards: legacy.cards,
        updatedAt: legacy.updatedAt || new Date().toISOString()
      };
    } else {
      // Nothing usable to migrate — start clean but still set the flag so we
      // never re-run migration (and never clobber later IDB writes).
      seed = freshStorage(version);
    }
    return idbSaveState(db, seed, true).then(function () { return seed; });
  }

  /* Resolve the live state for this boot.
       - IDB available  -> open, migrate-once, load, return { db, state }.
       - IDB unavailable -> { db: null, state: <localStorage blob or null> }.
     Always resolves (never rejects); falls back to localStorage on any error. */
  function openPersistence(version) {
    if (!idbSupported()) {
      return Promise.resolve({ db: null, state: loadLocal() });
    }
    return openDB().then(function (db) {
      return metaGet(db, "migrated").then(function (migrated) {
        var ready = migrated ? Promise.resolve(null) : idbMigrateFromLocal(db, version);
        return ready.then(function () {
          return idbLoadState(db).then(function (state) {
            return { db: db, state: state };
          });
        });
      });
    }).catch(function () {
      // Any IDB failure (blocked, private mode, quota on open, etc.) -> fall
      // back to the still-intact localStorage path. No data is lost.
      return { db: null, state: loadLocal() };
    });
  }

  /* Stable FNV-1a deck fingerprint for bare-array decks lacking a version. */
  function deckHash(cards) {
    var basis = JSON.stringify(
      cards.map(function (c) { return [c.id, c.front, c.back]; })
           .sort(function (a, b) { return a[0] < b[0] ? -1 : 1; })
    );
    var h = 0x811c9dc5;
    for (var i = 0; i < basis.length; i++) {
      h ^= basis.charCodeAt(i);
      h = (h * 0x01000193) >>> 0;
    }
    return "h" + h.toString(16);
  }

  /* Reconcile stored state with the loaded deck (the migration). */
  function reconcile(stored, cards, version) {
    if (!stored || stored.storageSchema !== STORAGE_SCHEMA) {
      // Storage SHAPE changed (or none yet) -> the only full-reset case.
      return freshStorage(version);
    }
    if (stored.deckVersion !== version) {
      // Deck changed -> migrate by id; keep survivors, drop removed, new = New.
      var ids = {};
      cards.forEach(function (c) { ids[c.id] = true; });
      var kept = {};
      Object.keys(stored.cards || {}).forEach(function (id) {
        if (ids[id]) kept[id] = stored.cards[id];
      });
      stored.cards = kept;
      stored.deckVersion = version;
      stored.updatedAt = new Date().toISOString();
    }
    if (!stored.cards) stored.cards = {};
    if (!stored.filter) stored.filter = "All";
    return stored;
  }

  /* =======================================================================
     Card state access
     ===================================================================== */
  function getCard(state, id) {
    var stored = state.cards[id];
    if (!stored) return createEmptyCard();
    try {
      return TypeConvert && TypeConvert.card ? TypeConvert.card(stored) : rehydrate(stored);
    } catch (e) {
      return rehydrate(stored);
    }
  }
  // Fallback rehydration if TypeConvert is somehow absent.
  function rehydrate(c) {
    var out = {};
    for (var k in c) if (Object.prototype.hasOwnProperty.call(c, k)) out[k] = c[k];
    out.due = new Date(c.due);
    if (c.last_review) out.last_review = new Date(c.last_review);
    return out;
  }
  function serialize(card) { return JSON.parse(JSON.stringify(card)); }

  function isDue(card) {
    return card.state === State.New ||
           new Date(card.due).getTime() <= Date.now();
  }

  /* =======================================================================
     Text rendering — escape first, then a tiny safe whitelist.
     Never inject raw card HTML.
     ===================================================================== */
  function escapeHtml(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }
  // Apply after escaping: **bold**, *italics*, `code`, newline -> <br>.
  function renderText(s) {
    var t = escapeHtml(s);
    t = t.replace(/`([^`]+?)`/g, function (_, c) { return "<code>" + c + "</code>"; });
    t = t.replace(/\*\*([^*]+?)\*\*/g, "<strong>$1</strong>");
    t = t.replace(/(^|[^*])\*([^*\n]+?)\*(?!\*)/g, "$1<em>$2</em>");
    t = t.replace(/\r?\n/g, "<br>");
    return t;
  }
  function setRich(el, s) { el.innerHTML = renderText(s); }

  /* small DOM builder */
  function h(tag, cls, text) {
    var el = document.createElement(tag);
    if (cls) el.className = cls;
    if (text != null) el.textContent = text;
    return el;
  }

  function panel(kind, mark, title, body, actions) {
    var p = h("div", "fc-panel" + (kind ? " fc-panel--" + kind : ""));
    p.appendChild(h("div", "fc-panel-mark", mark));
    p.appendChild(h("h2", null, title));
    var bp = h("p");
    if (typeof body === "string") bp.textContent = body; else bp.appendChild(body);
    p.appendChild(bp);
    if (actions && actions.length) {
      var row = h("div", "fc-panel-actions");
      actions.forEach(function (a) { row.appendChild(a); });
      p.appendChild(row);
    }
    return p;
  }

  /* Friendly relative interval, e.g. "4d", "2mo", "1y", "<1m". */
  function fmtInterval(fromDate) {
    var ms = new Date(fromDate).getTime() - Date.now();
    if (ms <= 0) return "now";
    var mins = ms / 60000;
    if (mins < 1) return "<1m";
    if (mins < 60) return Math.round(mins) + "m";
    var hrs = mins / 60;
    if (hrs < 24) return Math.round(hrs) + "h";
    var days = hrs / 24;
    if (days < 30) return Math.round(days) + "d";
    var mos = days / 30;
    if (mos < 12) return Math.round(mos) + "mo";
    return (Math.round(days / 36.5) / 10) + "y";
  }
  function fmtDue(fromDate) {
    var iv = fmtInterval(fromDate);
    return iv === "now" ? "now" : "in " + iv;
  }

  /* =======================================================================
     Controller
     ===================================================================== */
  function Controller(root) {
    this.root = root;
    this.deck = [];
    this.state = null;
    this.db = null;            // open IDBDatabase, or null when using localStorage fallback
    this.version = "";
    this.filter = "All";
    this.queue = [];
    this.currentId = null;
    this.flipped = false;
    this.reviewedThisSession = 0;
    this.cleanups = [];        // teardown callbacks
  }

  Controller.prototype.destroy = function () {
    this.cleanups.forEach(function (fn) { try { fn(); } catch (e) {} });
    this.cleanups = [];
    if (this.db) { try { this.db.close(); } catch (e) {} this.db = null; }
  };

  /* ----- persistence facade: route writes to IDB when open, else localStorage.
     All wrapped so a failed write degrades to in-memory without throwing. ----- */

  // Persist the whole state (after reconcile/migration and on reset).
  Controller.prototype.persistAll = function () {
    if (this.db) {
      var self = this;
      idbSaveState(this.db, this.state, false).catch(function () { saveLocal(self.state); });
    } else {
      saveLocal(this.state);
    }
  };

  // Persist one graded card record + the updatedAt stamp (hot path).
  Controller.prototype.persistCard = function (id, record, updatedAt) {
    if (this.db) {
      var self = this;
      idbPutCard(this.db, id, record, updatedAt).catch(function () { saveLocal(self.state); });
    } else {
      saveLocal(this.state);
    }
  };

  // Persist a single meta value (the filter selection).
  Controller.prototype.persistMeta = function (key, value) {
    if (this.db) {
      var self = this;
      idbPutMeta(this.db, key, value).catch(function () { saveLocal(self.state); });
    } else {
      saveLocal(this.state);
    }
  };

  Controller.prototype.start = function () {
    var self = this;
    var deckUrl = this.root.getAttribute("data-deck-url") || DEFAULT_DECK_URL;
    this.deckUrl = deckUrl;
    this.root.textContent = "Loading flashcards…";

    fetch(deckUrl, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (deck) { self.boot(deck); })
      .catch(function (err) { self.renderLoadError(err); });
  };

  Controller.prototype.boot = function (deck) {
    var self = this;
    var cards = Array.isArray(deck) ? deck : (deck && deck.cards) || [];
    cards = cards.filter(function (c) { return c && c.id; });
    if (!cards.length) { this.renderEmptyDeck(); return; }

    this.deck = cards;
    this.deckTitle = (deck && deck.title) || "";
    this.version = (deck && deck.version) || deckHash(cards);

    // Open persistence (IDB with one-time migration, or localStorage fallback)
    // and ONLY THEN reconcile + render. The await here is what prevents reading
    // progress before the migration has finished.
    openPersistence(this.version).then(function (res) {
      if (!self.root.isConnected) { if (res.db) { try { res.db.close(); } catch (e) {} } return; }
      self.db = res.db;
      var stored = reconcile(res.state, cards, self.version);
      self.state = stored;
      self.filter = stored.filter || "All";
      // Persist the reconciled state (covers fresh state, deck-version migration,
      // and the post-localStorage-migration write). One transaction.
      self.persistAll();

      self.buildShell();
      self.rebuildQueue();
      self.render();
    });
  };

  /* Build the persistent shell once; render() updates the body region. */
  Controller.prototype.buildShell = function () {
    var self = this;
    this.root.textContent = "";
    this.root.dataset.fcReady = "1";

    var rootEl = h("div", "fc-root");

    /* --- top bar: counts + filter --- */
    var bar = h("div", "fc-bar");
    var counts = h("div", "fc-counts");
    this.elDue = countCell("Due", "fc-count--due");
    this.elNew = countCell("New");
    this.elRev = countCell("Review");
    counts.appendChild(this.elDue.wrap);
    counts.appendChild(this.elNew.wrap);
    counts.appendChild(this.elRev.wrap);

    var filterWrap = h("div", "fc-filter");
    var fid = "fc-topic-" + Math.random().toString(36).slice(2, 7);
    var flabel = h("label", null, "Topic");
    flabel.setAttribute("for", fid);
    var select = h("select", "fc-select");
    select.id = fid;
    this.buildTopicOptions(select);
    onEvent(this, select, "change", function () {
      self.filter = select.value;
      self.state.filter = self.filter;
      self.persistMeta("filter", self.filter);
      self.rebuildQueue();
      self.render();
    });
    this.elFilter = select;
    filterWrap.appendChild(flabel);
    filterWrap.appendChild(select);

    bar.appendChild(counts);
    bar.appendChild(filterWrap);
    rootEl.appendChild(bar);

    /* --- body region (card / panels swap in here) --- */
    this.elBody = h("div", "fc-body");
    rootEl.appendChild(this.elBody);

    /* --- footer: progress + reset --- */
    var foot = h("div", "fc-foot");
    var prog = h("div", "fc-progress");
    var track = h("div", "fc-progress-track");
    this.elFill = h("div", "fc-progress-fill");
    track.appendChild(this.elFill);
    this.elProgLabel = h("span", "fc-progress-label", "");
    prog.appendChild(track);
    prog.appendChild(this.elProgLabel);

    var reset = h("button", "fc-reset", "Reset progress");
    reset.type = "button";
    onEvent(this, reset, "click", function () { self.reset(); });

    foot.appendChild(prog);
    foot.appendChild(reset);
    rootEl.appendChild(foot);

    this.root.appendChild(rootEl);

    /* --- global key + swipe bindings (scoped, cleaned up on destroy) --- */
    this.bindKeys();

    function countCell(label, extra) {
      var wrap = h("div", "fc-count" + (extra ? " " + extra : ""));
      var b = h("b", null, "0");
      var s = h("span", null, label);
      wrap.appendChild(b); wrap.appendChild(s);
      return { wrap: wrap, value: b };
    }
  };

  Controller.prototype.buildTopicOptions = function (select) {
    var seen = {}, topics = [];
    this.deck.forEach(function (c) {
      var t = c.topic || "Untitled";
      if (!seen[t]) { seen[t] = true; topics.push(t); }
    });
    topics.sort(function (a, b) { return a.localeCompare(b); });
    select.appendChild(option("All", "All topics"));
    topics.forEach(function (t) { select.appendChild(option(t, t)); });
    // restore persisted filter if it still exists
    var has = this.filter === "All" || seen[this.filter];
    select.value = has ? this.filter : "All";
    this.filter = select.value;

    function option(val, label) {
      var o = document.createElement("option");
      o.value = val; o.textContent = label;
      return o;
    }
  };

  /* Build the due queue for the active filter. Overdue/learning first,
     New cards last and capped per session. */
  Controller.prototype.rebuildQueue = function () {
    var self = this;
    var filtered = this.deck.filter(function (c) {
      return self.filter === "All" || c.topic === self.filter;
    });
    var dueLearn = [], dueReview = [], fresh = [];
    filtered.forEach(function (c) {
      var card = getCard(self.state, c.id);
      if (!isDue(card)) return;
      if (card.state === State.New) fresh.push(c.id);
      else if (card.state === State.Learning || card.state === State.Relearning) dueLearn.push(c.id);
      else dueReview.push(c.id);
    });
    fresh = fresh.slice(0, NEW_PER_SESSION);
    this.queue = dueLearn.concat(dueReview, fresh);

    // Keep showing the current card if it's still due; else advance.
    if (this.currentId && this.queue.indexOf(this.currentId) !== -1) {
      // keep current position
    } else {
      this.currentId = this.queue[0] || null;
      this.flipped = false;
    }
  };

  /* Counts across the WHOLE filtered set (not just the capped queue). */
  Controller.prototype.computeCounts = function () {
    var self = this;
    var due = 0, neu = 0, rev = 0;
    this.deck.forEach(function (c) {
      if (self.filter !== "All" && c.topic !== self.filter) return;
      var card = getCard(self.state, c.id);
      if (card.state === State.New) neu++;
      else rev++;
      if (isDue(card)) due++;
    });
    return { due: due, neu: neu, rev: rev };
  };

  Controller.prototype.flip = function () {
    if (!this.currentId || this.flipped) return;
    this.flipped = true;
    this.render();
  };

  Controller.prototype.grade = function (rating) {
    if (!this.currentId || !this.flipped) return;
    var id = this.currentId;
    var card = getCard(this.state, id);
    var res = scheduler.next(card, new Date(), rating);
    var record = serialize(res.card);
    this.state.cards[id] = record;
    this.state.updatedAt = new Date().toISOString();
    this.persistCard(id, record, this.state.updatedAt);
    this.reviewedThisSession++;

    // Remove from queue (it may re-enter on rebuild if still due — learning step).
    var idx = this.queue.indexOf(id);
    if (idx !== -1) this.queue.splice(idx, 1);
    this.currentId = this.queue[0] || null;
    this.flipped = false;

    this.rebuildQueue();
    this.render();
  };

  Controller.prototype.reset = function () {
    var ok = true;
    try {
      ok = window.confirm(
        "Reset all study progress for this deck? Every card returns to New. " +
        "This cannot be undone.");
    } catch (e) { ok = true; }
    if (!ok) return;
    this.state = freshStorage(this.version);
    // Wipe the active store (IDB when open, else localStorage). The legacy
    // localStorage blob is intentionally left intact as a fallback when IDB
    // is the active store — it is only the migration source / fallback.
    if (this.db) {
      this.persistAll();
    } else {
      clearLocal();
      saveLocal(this.state);
    }
    this.reviewedThisSession = 0;
    this.currentId = null;
    this.flipped = false;
    this.rebuildQueue();
    this.render();
  };

  /* ----- keyboard: Space/Enter flip; 1-4 grade ----- */
  Controller.prototype.bindKeys = function () {
    var self = this;
    function onKey(e) {
      if (!self.root.isConnected) return;
      var tag = (e.target && e.target.tagName) || "";
      var typing = tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" ||
                   (e.target && e.target.isContentEditable);
      if (typing) return;
      if (!self.currentId) return;

      if (e.key === " " || e.key === "Spacebar" || e.key === "Enter") {
        if (!self.flipped) { e.preventDefault(); self.flip(); }
        return;
      }
      if (self.flipped && e.key >= "1" && e.key <= "4") {
        e.preventDefault();
        var map = { "1": Rating.Again, "2": Rating.Hard, "3": Rating.Good, "4": Rating.Easy };
        self.grade(map[e.key]);
      }
    }
    document.addEventListener("keydown", onKey);
    this.cleanups.push(function () { document.removeEventListener("keydown", onKey); });
  };

  /* ----- swipe on the card: left=Again, right=Good ----- */
  Controller.prototype.bindSwipe = function (cardEl) {
    var self = this, x0 = 0, y0 = 0, tracking = false, locked = null;
    function start(e) {
      var t = e.touches ? e.touches[0] : e;
      x0 = t.clientX; y0 = t.clientY; tracking = true; locked = null;
    }
    function move(e) {
      if (!tracking) return;
      var t = e.touches ? e.touches[0] : e;
      var dx = t.clientX - x0, dy = t.clientY - y0;
      if (locked === null && (Math.abs(dx) > 10 || Math.abs(dy) > 10)) {
        locked = Math.abs(dx) > Math.abs(dy) ? "x" : "y";
      }
    }
    function end(e) {
      if (!tracking) return;
      tracking = false;
      var t = (e.changedTouches && e.changedTouches[0]) || e;
      var dx = t.clientX - x0, dy = t.clientY - y0;
      if (locked === "x" && Math.abs(dx) >= SWIPE_THRESHOLD && Math.abs(dx) > Math.abs(dy)) {
        if (!self.flipped) { self.flip(); return; }
        self.grade(dx < 0 ? Rating.Again : Rating.Good);
      }
    }
    cardEl.addEventListener("touchstart", start, { passive: true });
    cardEl.addEventListener("touchmove", move, { passive: true });
    cardEl.addEventListener("touchend", end);
  };

  /* =======================================================================
     Render
     ===================================================================== */
  Controller.prototype.render = function () {
    if (!this.elBody) return;
    var counts = this.computeCounts();
    this.elDue.value.textContent = String(counts.due);
    this.elNew.value.textContent = String(counts.neu);
    this.elRev.value.textContent = String(counts.rev);

    // session progress: reviewed / (reviewed + remaining due in queue)
    var remaining = this.queue.length;
    var done = this.reviewedThisSession;
    var total = done + remaining;
    var pct = total > 0 ? Math.round((done / total) * 100) : (this.currentId ? 0 : 100);
    this.elFill.style.width = pct + "%";
    this.elProgLabel.textContent = total > 0
      ? done + " of " + total + " this session"
      : "No cards in queue";

    this.elBody.textContent = "";

    if (!this.currentId) {
      this.elBody.appendChild(this.caughtUpPanel(counts));
      return;
    }
    this.elBody.appendChild(this.renderCard());
  };

  Controller.prototype.renderCard = function () {
    var self = this;
    var data = this.deck.find(function (c) { return c.id === self.currentId; });
    var card = getCard(this.state, this.currentId);

    var el = h("div", "fc-card" + (this.flipped ? " is-flipped" : ""));
    el.tabIndex = 0;
    el.setAttribute("role", "button");
    el.setAttribute("aria-label",
      this.flipped ? "Flashcard, answer shown" : "Flashcard, press to reveal answer");

    /* caption row */
    var cap = h("div", "fc-caption");
    var capL = h("div");
    capL.appendChild(h("span", "fc-caption-topic", data.topic || "—"));
    if (data.page) {
      var pg = h("span", "fc-caption-page", " · " + data.page);
      capL.appendChild(pg);
    }
    cap.appendChild(capL);
    cap.appendChild(h("span", "fc-caption-type", typeLabel(data.type)));
    el.appendChild(cap);

    /* face */
    var face = h("div", "fc-face");
    var prompt = h("div", "fc-prompt");
    setRich(prompt, data.front);
    face.appendChild(prompt);

    if (!this.flipped) {
      var hint = h("div", "fc-hint");
      var kbd = h("kbd", null, "Space");
      hint.appendChild(document.createTextNode("Press "));
      hint.appendChild(kbd);
      hint.appendChild(document.createTextNode(" or tap to reveal"));
      face.appendChild(hint);
    } else {
      var divider = h("div", "fc-divider", "Answer");
      face.appendChild(divider);

      var ans = h("div", "fc-answer fc-reveal");
      setRich(ans, data.back);
      face.appendChild(ans);

      // citation + source (Bluebook cite as text; source as CourtListener link)
      if (data.cite || data.source) {
        var meta = h("div", "fc-meta");
        if (data.cite) meta.appendChild(h("div", "fc-cite", data.cite));
        if (data.source) {
          var link = h("a", "fc-source", "View on CourtListener ↗");
          link.href = data.source;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
          meta.appendChild(link);
        }
        face.appendChild(meta);
      }
    }
    el.appendChild(face);

    /* grade buttons (only when flipped) */
    if (this.flipped) {
      var preview = null;
      try { preview = scheduler.repeat(card, new Date()); } catch (e) { preview = null; }
      var grades = h("div", "fc-grades fc-reveal");
      grades.setAttribute("role", "group");
      grades.setAttribute("aria-label", "Grade your recall");
      [
        ["again", "Again", "1", Rating.Again],
        ["hard",  "Hard",  "2", Rating.Hard],
        ["good",  "Good",  "3", Rating.Good],
        ["easy",  "Easy",  "4", Rating.Easy]
      ].forEach(function (g) {
        var cls = g[0], label = g[1], key = g[2], rating = g[3];
        var btn = h("button", "fc-grade fc-grade--" + cls);
        btn.type = "button";
        var top = h("span", "fc-grade-key", label);
        btn.appendChild(top);
        var iv = "";
        if (preview && preview[rating] && preview[rating].card) {
          iv = fmtInterval(preview[rating].card.due);
        }
        btn.appendChild(h("span", "fc-grade-int", (iv ? iv + " · " : "") + key));
        btn.setAttribute("aria-label", label + " (key " + key + ")" + (iv ? ", next in " + iv : ""));
        onEvent(self, btn, "click", function (e) { e.stopPropagation(); self.grade(rating); });
        grades.appendChild(btn);
      });
      el.appendChild(grades);
    }

    /* flip on card click (ignore clicks on links/buttons) */
    onEvent(this, el, "click", function (e) {
      if (e.target.closest("a, button")) return;
      self.flip();
    });
    onEvent(this, el, "keydown", function (e) {
      if ((e.key === " " || e.key === "Enter") && !self.flipped) {
        e.preventDefault(); self.flip();
      }
    });
    this.bindSwipe(el);

    return el;

    function typeLabel(t) {
      if (t === "cloze") return "Cloze";
      if (t === "definition") return "Definition";
      return "Q & A";
    }
  };

  Controller.prototype.caughtUpPanel = function (counts) {
    var self = this;
    // next due time across the active filter
    var next = null;
    this.deck.forEach(function (c) {
      if (self.filter !== "All" && c.topic !== self.filter) return;
      var card = getCard(self.state, c.id);
      if (card.state === State.New) return;
      var due = new Date(card.due).getTime();
      if (due > Date.now() && (next === null || due < next)) next = due;
    });

    var scope = this.filter === "All" ? "this deck" : "“" + this.filter + "”";
    var body;
    if (counts.neu > 0 && counts.due === 0) {
      // there are New cards but the per-session cap was hit, OR filter empty of due
      body = "You’ve cleared the cards due in " + scope + ". " +
             (next ? "Next review " + fmtDue(next) + "." :
                     "New cards remain — switch the topic filter to study more.");
    } else if (next) {
      body = "Every card due in " + scope + " is reviewed. Next one comes up " + fmtDue(next) + ".";
    } else {
      body = "Every card in " + scope + " is reviewed. Nothing is scheduled yet — " +
             "check back later or pick another topic.";
    }
    return panel("", "✓", "All caught up", body);
  };

  Controller.prototype.renderEmptyDeck = function () {
    this.root.textContent = "";
    this.root.dataset.fcReady = "empty";
    this.root.appendChild(panel("", "§", "No cards yet",
      "The deck loaded but contains no cards. Add cards to the deck file and reload."));
  };

  Controller.prototype.renderLoadError = function (err) {
    this.root.textContent = "";
    this.root.dataset.fcReady = "error";
    var msg = h("span");
    msg.appendChild(document.createTextNode("Couldn’t load the deck from "));
    msg.appendChild(h("code", null, this.deckUrl));
    msg.appendChild(document.createTextNode(". " + (err && err.message ? "(" + err.message + ") " : "") +
      "Confirm the file is published, then reload."));
    var retry = h("button", "fc-btn fc-btn--primary", "Retry");
    retry.type = "button";
    var self = this;
    retry.addEventListener("click", function () { self.root.dataset.fcReady = ""; self.start(); });
    this.root.appendChild(panel("error", "§", "Deck unavailable", msg, [retry]));
  };

  /* Track listeners so re-init can detach them. */
  function onEvent(ctrl, el, type, fn) {
    el.addEventListener(type, fn);
    ctrl.cleanups.push(function () { el.removeEventListener(type, fn); });
  }

  /* =======================================================================
     Init — idempotent, SPA-aware. Quartz fires `nav` on every navigation
     (including first load); we also self-run for the standalone page.
     ===================================================================== */
  function init() {
    var root = document.getElementById("flashcards-app");
    if (!root) return;
    // Already initialized AND still the same live node -> nothing to do.
    if (root.dataset.fcInit === "1" && root.dataset.fcReady) return;

    // Tear down any prior controller (handles SPA re-entry / swapped DOM).
    if (current) { current.destroy(); current = null; }

    root.dataset.fcInit = "1";
    root.dataset.fcReady = "";
    current = new Controller(root);
    current.start();
  }

  // Quartz SPA navigation (also fires on first load).
  document.addEventListener("nav", init);

  // Standalone / direct load: run as soon as the DOM is ready, in case
  // there is no Quartz to emit a `nav` event.
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
