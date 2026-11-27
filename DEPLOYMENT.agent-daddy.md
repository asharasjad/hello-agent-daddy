# Deploying hello-agent-daddy with Agent Daddy

Generated documentation for the private deployment of this repository. It is safe to commit:
it contains variable names only, never values.

| Item | Value |
|---|---|
| Deploy branch | `cloud-deployment` (main is never modified) |
| Runtime | python 3.13 (no framework detected) |
| Build | `none` |
| Start | `see Dockerfile` |
| Container port | 8000 |
| Host port | 127.0.0.1:18100 (loopback only) |
| Private URL | https://vmi3790942.taildde6c7.ts.net:8472 (Tailscale only, no Funnel) |
| Health check | `/health` |
| Limits | memory 256m, CPUs 0.5, PIDs 128 |
| Volumes | none (stateless) |
| Instances | exactly one (single-instance) |

## Environment variables

Set values in Coolify (Environment Variables). Do not commit a `.env` file.

## Build validation (isolated)

1. `cloud validate <app>`: strict policy on the committed files, plus `docker compose config` canonical check.
2. The broker re-validates the exact commit, binds your approval to its fingerprint and starts the build in Coolify.
3. The deployment counts as successful only when the container health check passes.
4. If it fails, the previous version keeps running; a rollback needs a new approval.

## Warnings from analysis

- none

## Background work

Run exactly one container. If the app starts schedulers or queue workers in-process, a second instance would
duplicate them (double posts, double emails). Do not add replicas or a separate worker service without a lock.
