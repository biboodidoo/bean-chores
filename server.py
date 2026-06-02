#!/usr/bin/env python3
"""
Bean's Chore Quest - LAN sync server.

Serves the app (index.html) and a tiny shared-state API so every device on the
home Wi-Fi reads and writes ONE board. No third-party packages, Python 3 stdlib only.

Run:   python3 server.py            # serves on http://0.0.0.0:8080
       python3 server.py 9000       # custom port

Data lives in data.json next to this file (the single source of truth).
Every write is atomic (temp file + os.replace) and snapshotted into backups/.
"""
import datetime
import http.server
import json
import os
import shutil
import socketserver
import sys
import tempfile
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data.json")
BACKUP_DIR = os.path.join(HERE, "backups")
INDEX = os.path.join(HERE, "index.html")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", "8080"))

_lock = threading.Lock()


def read_data():
    try:
        with open(DATA, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"version": 0, "state": None}


def write_data(obj):
    fd, tmp = tempfile.mkstemp(dir=HERE, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        json.load(open(tmp, encoding="utf-8"))  # validate before swap
        os.replace(tmp, DATA)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def backup():
    try:
        if not os.path.exists(DATA):
            return
        os.makedirs(BACKUP_DIR, exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
        shutil.copy2(DATA, os.path.join(BACKUP_DIR, "data-%s.json" % stamp))
        snaps = sorted(x for x in os.listdir(BACKUP_DIR) if x.startswith("data-"))
        for old in snaps[:-30]:  # keep the most recent 30 snapshots
            os.remove(os.path.join(BACKUP_DIR, old))
    except Exception:
        pass


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_GET(self):
        if self.path.startswith("/api/state"):
            with _lock:
                self._send(200, json.dumps(read_data(), ensure_ascii=False))
            return
        if self.path.startswith("/api/ping"):
            self._send(200, json.dumps({"ok": True}))
            return
        try:
            with open(INDEX, "rb") as f:
                self._send(200, f.read(), "text/html; charset=utf-8")
        except Exception:
            self._send(404, "not found", "text/plain")

    def do_PUT(self):
        if not self.path.startswith("/api/state"):
            self._send(404, json.dumps({"ok": False}))
            return
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8"))
        except Exception:
            self._send(400, json.dumps({"ok": False, "error": "bad json"}))
            return
        with _lock:
            cur = read_data()
            newver = (cur.get("version", 0) or 0) + 1
            write_data({"version": newver, "state": payload.get("state")})
            self._send(200, json.dumps({"ok": True, "version": newver}, ensure_ascii=False))
        backup()

    def log_message(self, *args):
        pass  # keep the console quiet


class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    print("Bean's Chore Quest server -> http://0.0.0.0:%d   (data: %s)" % (PORT, DATA))
    print("On other devices open: http://<this-computer-name>.local:%d" % PORT)
    try:
        ThreadingServer(("0.0.0.0", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
