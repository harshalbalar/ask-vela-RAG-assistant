# Runbook: config-service

**Owner:** Platform Team · **Language:** Go · **Port:** 8130 · **Doc ID:** RUN-CONFIG-SERVICE

## Purpose
`config-service` serves per-tenant configuration.

## Health & dashboards
The service exposes `/healthz` on port 8130. The primary Grafana board is
`vela/config-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `config-fetch-fail`
This is the most frequent page for `config-service`. First, check the `config-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `CFG-404`
`CFG-404` means the requested tenant config key was not found. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart config-service` (rolling, zero-downtime). For a full reset use
`velactl restart config-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `config-service` outage may be a
downstream symptom — verify those first.
