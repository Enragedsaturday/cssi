#!/opt/homebrew/bin/python3
"""Static server for the CSSI Quartz site, with clean-URL resolution.
Quartz emits flat <slug>.html files but links to extensionless clean URLs (/Curtilage),
so we map /Foo -> /Foo.html when /Foo doesn't exist. Threaded for concurrent laptop+phone.
Usage: serve-public.py [PORT] [ROOT]"""
import os, sys, urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import functools

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
ROOT = sys.argv[2] if len(sys.argv) > 2 else "/Users/johngalt/Projects/cssi-quartz/public"
# BIND: 0.0.0.0 = reachable over Tailscale at http://johns-mac-studio.tail2e4945.ts.net:PORT
# (Option A — used because Tailscale Serve/HTTPS is not enabled on this tailnet).
# If you later enable Serve (one click) and want loopback-only behind HTTPS, pass 127.0.0.1 here.
BIND = sys.argv[3] if len(sys.argv) > 3 else "0.0.0.0"


class Handler(SimpleHTTPRequestHandler):
    def send_head(self):
        # Clean-URL resolution: /Foo -> /Foo.html when /Foo is not an existing file/dir.
        parsed = urllib.parse.urlsplit(self.path)
        fs = self.translate_path(self.path)  # drops query/fragment
        if (not os.path.exists(fs)) and (not parsed.path.endswith("/")):
            if os.path.exists(fs + ".html"):
                self.path = urllib.parse.urlunsplit(parsed._replace(path=parsed.path + ".html"))
        return super().send_head()

    def send_error(self, code, message=None, explain=None):
        # Serve Quartz's themed 404 page on not-found.
        if code == 404:
            f404 = os.path.join(ROOT, "404.html")
            if os.path.exists(f404):
                try:
                    body = open(f404, "rb").read()
                    self.send_response(404)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    if self.command != "HEAD":
                        self.wfile.write(body)
                    return
                except Exception:
                    pass
        return super().send_error(code, message, explain)


Handler = functools.partial(Handler, directory=ROOT)
httpd = ThreadingHTTPServer((BIND, PORT), Handler)
print(f"serving {ROOT} on http://{BIND}:{PORT} (clean-URL aware)", flush=True)
httpd.serve_forever()
