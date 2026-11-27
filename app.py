"""hello-agent-daddy: minimal first-party test app for Agent Daddy deployments.

Python standard library only: no dependencies, no secrets, no storage, no outbound calls.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PAGE = b"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent Daddy</title></head>
<body style="font-family: system-ui, sans-serif; display: grid; place-items: center; min-height: 90vh;">
<h1>Agent Daddy is operational.</h1>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    server_version = "hello-agent-daddy"
    sys_version = ""

    def _send(self, status: int, body: bytes, ctype: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/":
            self._send(200, PAGE, "text/html; charset=utf-8")
        elif self.path == "/health":
            self._send(200, json.dumps({"status": "ok"}).encode(), "application/json")
        else:
            self._send(404, b"not found\n", "text/plain; charset=utf-8")

    do_HEAD = do_GET

    def log_message(self, fmt: str, *args) -> None:
        print(f"{self.address_string()} {fmt % args}", flush=True)


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
