import os, base64, zipfile, io, subprocess, sys
from pathlib import Path
from cryptography.fernet import Fernet

key = os.environ.get("DEPLOY_BUNDLE_KEY")
if not key:
    raise SystemExit("DEPLOY_BUNDLE_KEY is required")

root = Path("/tmp/sadaf-publisher")
root.mkdir(parents=True, exist_ok=True)

parts = []
for name in ["payload_00.txt", "payload_01.txt", "payload_02.txt", "payload_03.txt"]:
    parts.append(Path("/app", name).read_text())
payload = base64.b64decode("".join(parts))

plain = Fernet(key.encode()).decrypt(payload)
with zipfile.ZipFile(io.BytesIO(plain)) as z:
    z.extractall(root)

os.chdir(root)
subprocess.Popen([sys.executable, "scheduler.py"])
os.execv(sys.executable, [sys.executable, "server.py"])
