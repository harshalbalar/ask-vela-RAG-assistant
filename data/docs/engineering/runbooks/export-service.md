# Runbook: export-service

**Owner:** Data Team · **Language:** Go · **Port:** 8110 · **Doc ID:** RUN-EXPORT-SERVICE

## Purpose
`export-service` runs scheduled data export jobs.

## Health & dashboards
The service exposes `/healthz` on port 8110. The primary Grafana board is
`vela/export-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `export-job-stuck`
This is the most frequent page for `export-service`. First, check the `export-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `EXP-507`
`EXP-507` means an export job exceeded its time budget. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart export-service` (rolling, zero-downtime). For a full reset use
`velactl restart export-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `export-service` outage may be a
downstream symptom — verify those first.
