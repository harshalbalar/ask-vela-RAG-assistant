# Runbook: alerting-service

**Owner:** Alerting Team · **Language:** Go · **Port:** 8120 · **Doc ID:** RUN-ALERTING-SERVICE

## Purpose
`alerting-service` evaluates customer alert rules.

## Health & dashboards
The service exposes `/healthz` on port 8120. The primary Grafana board is
`vela/alerting-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `alert-eval-delay`
This is the most frequent page for `alerting-service`. First, check the `alerting-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `ALR-422`
`ALR-422` means an alert rule has an invalid VelaQL expression. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart alerting-service` (rolling, zero-downtime). For a full reset use
`velactl restart alerting-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `alerting-service` outage may be a
downstream symptom — verify those first.
