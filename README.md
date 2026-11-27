# hello-agent-daddy

Minimal first-party test application for Agent Daddy's private, Tailscale-only deployments.

- `GET /` returns a page that says "Agent Daddy is operational."
- `GET /health` returns `{"status": "ok"}`.

Python standard library only. It has no dependencies, secrets, persistent storage or outbound
network calls. Deployment files are on the `cloud-deployment` branch.

Run it locally with `python3 app.py`, then open http://127.0.0.1:8000/.
