# Runbook: web-app

**Owner:** Frontend Team · **Language:** TypeScript · **Port:** 3000 · **Doc ID:** RUN-WEB-APP

## Purpose
`web-app` the customer-facing console.

## Health & dashboards
The service exposes `/healthz` on port 3000. The primary Grafana board is
`vela/web-app-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `web-5xx-rate`
This is the most frequent page for `web-app`. First, check the `web-app-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `WEB-502`
`WEB-502` means the web app could not reach an upstream API. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart web-app` (rolling, zero-downtime). For a full reset use
`velactl restart web-app --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `web-app` outage may be a
downstream symptom — verify those first.
