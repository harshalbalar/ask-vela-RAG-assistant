# Platform Architecture Overview

**Owner:** Platform Team · **Last updated:** 2025-04-12 · **Doc ID:** ENG-ARCH-008

Vela Cloud runs a multi-tenant observability platform on AWS (us-east-1, eu-west-1).

## High-level components
- **Ingest API** (Go) — receives metrics/logs/traces over gRPC and HTTP.
- **Stream processor** (Rust, Kafka) — enriches and routes events.
- **Query service** (Go) — serves dashboards and the query language VelaQL.
- **Web app** (TypeScript / React) — the customer console.
- **Storage** — ClickHouse for time-series, Postgres for metadata, S3 for cold storage.

## Tenancy
Each customer is a tenant, isolated by `tenant_id`. Data retention defaults to 30 days (hot)
and 13 months (cold) and is configurable per plan.

## Environments
`dev` → `staging` → `prod`. All services are containerized and deployed via Kubernetes (EKS).
