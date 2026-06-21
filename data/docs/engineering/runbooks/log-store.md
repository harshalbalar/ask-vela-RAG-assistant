# Runbook: log-store

**Owner:** Storage Team · **Language:** ClickHouse · **Port:** 8124 · **Doc ID:** RUN-LOG-STORE

## Purpose
`log-store` stores log data.

## Health & dashboards
The service exposes `/healthz` on port 8124. The primary Grafana board is
`vela/log-store-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `log-write-fail`
This is the most frequent page for `log-store`. First, check the `log-store-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `LOG-507`
`LOG-507` means a log write batch failed to flush. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart log-store` (rolling, zero-downtime). For a full reset use
`velactl restart log-store --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `log-store` outage may be a
downstream symptom — verify those first.
