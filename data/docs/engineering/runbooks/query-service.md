# Runbook: query-service

**Owner:** Query Team · **Language:** Go · **Port:** 8081 · **Doc ID:** RUN-QUERY-SERVICE

## Purpose
`query-service` serves dashboards and VelaQL queries.

## Health & dashboards
The service exposes `/healthz` on port 8081. The primary Grafana board is
`vela/query-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `query-timeout-spike`
This is the most frequent page for `query-service`. First, check the `query-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `QRY-429`
`QRY-429` means a tenant exceeded its concurrent query quota. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart query-service` (rolling, zero-downtime). For a full reset use
`velactl restart query-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `query-service` outage may be a
downstream symptom — verify those first.
