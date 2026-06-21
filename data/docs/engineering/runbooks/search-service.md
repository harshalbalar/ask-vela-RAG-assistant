# Runbook: search-service

**Owner:** Search Team · **Language:** Rust · **Port:** 8200 · **Doc ID:** RUN-SEARCH-SERVICE

## Purpose
`search-service` powers log and trace search.

## Health & dashboards
The service exposes `/healthz` on port 8200. The primary Grafana board is
`vela/search-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `search-index-stale`
This is the most frequent page for `search-service`. First, check the `search-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `SRC-504`
`SRC-504` means the search index is stale or unreachable. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart search-service` (rolling, zero-downtime). For a full reset use
`velactl restart search-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `search-service` outage may be a
downstream symptom — verify those first.
