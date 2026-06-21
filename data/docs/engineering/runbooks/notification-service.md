# Runbook: notification-service

**Owner:** Notifications Team · **Language:** Go · **Port:** 8070 · **Doc ID:** RUN-NOTIFICATION-SERVICE

## Purpose
`notification-service` sends email and Slack alerts.

## Health & dashboards
The service exposes `/healthz` on port 8070. The primary Grafana board is
`vela/notification-service-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `notify-queue-backup`
This is the most frequent page for `notification-service`. First, check the `notification-service-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `NOT-503`
`NOT-503` means the outbound notification queue is backed up. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart notification-service` (rolling, zero-downtime). For a full reset use
`velactl restart notification-service --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `notification-service` outage may be a
downstream symptom — verify those first.
