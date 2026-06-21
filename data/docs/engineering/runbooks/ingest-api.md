# Runbook: ingest-api

**Owner:** Ingest Team · **Language:** Go · **Port:** 8443 · **Doc ID:** RUN-INGEST-API

## Purpose
`ingest-api` receives metrics/logs/traces over gRPC and HTTP.

## Health & dashboards
The service exposes `/healthz` on port 8443. The primary Grafana board is
`vela/ingest-api-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `ingest-api-high-latency`
This is the most frequent page for `ingest-api`. First, check the `ingest-api-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `ING-503`
`ING-503` means the ingest buffer is full and events are being shed. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart ingest-api` (rolling, zero-downtime). For a full reset use
`velactl restart ingest-api --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `ingest-api` outage may be a
downstream symptom — verify those first.
