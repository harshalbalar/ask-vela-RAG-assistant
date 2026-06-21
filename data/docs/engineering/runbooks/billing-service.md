# Runbook: billing-service

**Owner:** Billing Team · **Language:** Go · **Port:** 8090 · **Doc ID:** RUN-BILLING-SERVICE

## Purpose
`billing-service` handles invoicing and Stripe sync.

## Health & dashboards
The service exposes `/healthz` on port 8090. The primary Grafana board is
`vela/billing-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `billing-sync-failure`
This is the most frequent page for `billing-service`. First, check the `billing-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `BIL-402`
`BIL-402` means a Stripe charge was declined. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart billing-service` (rolling, zero-downtime). For a full reset use
`velactl restart billing-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `billing-service` outage may be a
downstream symptom — verify those first.
