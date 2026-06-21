# Runbook: dashboard-service

**Owner:** Frontend Team · **Language:** TypeScript · **Port:** 3100 · **Doc ID:** RUN-DASHBOARD-SERVICE

## Purpose
`dashboard-service` renders dashboards server-side.

## Health & dashboards
The service exposes `/healthz` on port 3100. The primary Grafana board is
`vela/dashboard-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `dashboard-render-fail`
This is the most frequent page for `dashboard-service`. First, check the `dashboard-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `DSH-500`
`DSH-500` means a dashboard panel failed to render. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart dashboard-service` (rolling, zero-downtime). For a full reset use
`velactl restart dashboard-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `dashboard-service` outage may be a
downstream symptom — verify those first.
