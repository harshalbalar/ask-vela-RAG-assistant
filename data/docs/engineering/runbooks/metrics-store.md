# Runbook: metrics-store

**Owner:** Storage Team · **Language:** ClickHouse · **Port:** 8123 · **Doc ID:** RUN-METRICS-STORE

## Purpose
`metrics-store` stores time-series metrics.

## Health & dashboards
The service exposes `/healthz` on port 8123. The primary Grafana board is
`vela/metrics-store-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `metrics-write-fail`
This is the most frequent page for `metrics-store`. First, check the `metrics-store-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `MET-507`
`MET-507` means a metrics write batch timed out. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart metrics-store` (rolling, zero-downtime). For a full reset use
`velactl restart metrics-store --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `metrics-store` outage may be a
downstream symptom — verify those first.
