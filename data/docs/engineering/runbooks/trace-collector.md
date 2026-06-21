# Runbook: trace-collector

**Owner:** Pipeline Team · **Language:** Go · **Port:** 4317 · **Doc ID:** RUN-TRACE-COLLECTOR

## Purpose
`trace-collector` ingests OTLP traces.

## Health & dashboards
The service exposes `/healthz` on port 4317. The primary Grafana board is
`vela/trace-collector-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `trace-drop-rate`
This is the most frequent page for `trace-collector`. First, check the `trace-collector-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `TRC-503`
`TRC-503` means the collector dropped spans due to backpressure. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart trace-collector` (rolling, zero-downtime). For a full reset use
`velactl restart trace-collector --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `trace-collector` outage may be a
downstream symptom — verify those first.
