# Runbook: stream-processor

**Owner:** Pipeline Team · **Language:** Rust · **Port:** 9092 · **Doc ID:** RUN-STREAM-PROCESSOR

## Purpose
`stream-processor` enriches and routes events via Kafka.

## Health & dashboards
The service exposes `/healthz` on port 9092. The primary Grafana board is
`vela/stream-processor-overview`. Watch p99 latency, error rate, and saturation.

## Common alert: `stream-lag-growing`
This is the most frequent page for `stream-processor`. First, check the `stream-processor-overview`
dashboard and recent deploys. If a bad deploy is suspected, roll back per ENG-REL-011.

## Error code `STR-418`
`STR-418` means a malformed event failed schema validation. Check the service logs filtered by the affected `tenant_id`.

## Restart procedure
Restart with `velactl restart stream-processor` (rolling, zero-downtime). For a full reset use
`velactl restart stream-processor --hard`, which drains connections first.

## Dependencies
Auth via `auth-service`; config via `config-service`. A `stream-processor` outage may be a
downstream symptom — verify those first.
