# Runbook: auth-service

**Owner:** Identity Team · **Language:** Go · **Port:** 8095 · **Doc ID:** RUN-AUTH-SERVICE

## Purpose
`auth-service` validates Okta tokens and sessions.

## Health & dashboards
The service exposes `/healthz` on port 8095. The primary Grafana board is
`vela/auth-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `auth-token-errors`
This is the most frequent page for `auth-service`. First, check the `auth-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `AUTH-401`
`AUTH-401` means an access token is expired or invalid. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart auth-service` (rolling, zero-downtime). For a full reset use
`velactl restart auth-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `auth-service` outage may be a
downstream symptom — verify those first.
