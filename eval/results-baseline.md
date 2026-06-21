# Retrieval Eval — baseline

- Generated: 2026-06-21 13:53 UTC
- Chat model: `gemini-2.5-flash` · Embeddings: `gemini-embedding-001`
- Retrieval: top_k=4, chunk_size=1000, overlap=150

| Metric | Value |
|---|---|
| Hit@4 | 1.000 |
| MRR | 0.983 |
| P@4 | 0.283 |
| R@4 | 0.983 |

## Per-question

| Question | First gold rank | Top retrieved |
|---|---|---|
| How do I restart the billing-service? | 1 | engineering/runbooks/billing-service.md, engineering/runbooks/config-service.md, engineering/runbooks/query-service.md |
| What does error QRY-429 mean? | 1 | engineering/runbooks/query-service.md, engineering/postmortems/inc-2025-031.md, engineering/runbooks/search-service.md |
| What port does the ingest-api run on? | 1 | engineering/runbooks/ingest-api.md, engineering/runbooks/stream-processor.md, engineering/runbooks/trace-collector.md |
| What is the common alert for the search-service? | 1 | engineering/runbooks/search-service.md, engineering/runbooks/alerting-service.md |
| Which team owns the notification-service? | 1 | engineering/runbooks/notification-service.md, engineering/runbooks/alerting-service.md, engineering/runbooks/config-service.md |
| What does STR-418 indicate? | 1 | engineering/runbooks/stream-processor.md, engineering/runbooks/billing-service.md, engineering/runbooks/ingest-api.md |
| What caused incident INC-2025-031? | 1 | engineering/postmortems/inc-2025-031.md, engineering/postmortems/inc-2025-076.md, engineering/postmortems/inc-2025-064.md, engineering/postmortems/inc-2025-048.md |
| What was the root cause of the duplicate invoices incident? | 1 | engineering/postmortems/inc-2025-042.md, engineering/runbooks/billing-service.md, engineering/postmortems/inc-2025-080.md, engineering/postmortems/inc-2025-072.md |
| Why did login failures spike in incident INC-2025-048? | 1 | engineering/postmortems/inc-2025-048.md, engineering/runbooks/auth-service.md, engineering/runbooks/config-service.md, engineering/runbooks/notification-service.md |
| How many vacation days do employees in Germany get? | 1 | hr/regions/germany/pto.md, hr/regions/germany/public-holidays.md, hr/regions/germany/parental-leave.md, hr/regions/germany/notice-period.md |
| How much PTO do employees in India receive? | 1 | hr/regions/india/pto.md, hr/regions/india/public-holidays.md, hr/regions/india/parental-leave.md, hr/pto-and-leave-policy.md |
| What is the notice period in the UK? | 1 | hr/regions/uk/notice-period.md, hr/regions/germany/notice-period.md, hr/regions/us/notice-period.md, hr/regions/india/notice-period.md |
| How many public holidays are there in Germany? | 1 | hr/regions/germany/public-holidays.md, hr/regions/germany/pto.md, hr/regions/uk/public-holidays.md, hr/regions/us/public-holidays.md |
| Parental leave for the birthing parent in the UK? | 1 | hr/regions/uk/parental-leave.md, hr/parental-leave.md, hr/regions/us/parental-leave.md, hr/regions/germany/parental-leave.md |
| What is the vacation rollover rule in Germany? | 1 | hr/regions/germany/pto.md, hr/regions/germany/public-holidays.md, meeting-notes/2025-06-18-hr-policy.md, hr/regions/uk/pto.md |
| How do I get access to Tailscale? | 1 | it-security/tools/tailscale.md, it-security/vpn-and-access.md, faq/vpn.md, it-security/tools/1password.md |
| Is 2FA required for GitHub? | 1 | it-security/tools/github.md, it-security/password-and-mfa-policy.md, engineering/git-workflow.md, engineering/runbooks/auth-service.md |
| What uptime does the Enterprise SLA guarantee? | 1 | operations/sla-tiers.md, product/saml-sso.md, product/audit-logs.md, product/retention-settings.md |
| What discount can a sales rep give without approval? | 1 | operations/discount-approval.md, faq/refunds.md, meeting-notes/2025-06-10-ops-standup.md, onboarding/sales-rep.md |
| How long do we have to fulfil a GDPR data deletion request? | 1 | operations/data-deletion-gdpr.md, operations/customer-offboarding.md, product/retention-settings.md, operations/customer-refund-sop.md |
| When does customer data get permanently deleted after cancellation? | 1 | operations/customer-offboarding.md, operations/data-deletion-gdpr.md, product/retention-settings.md, product/audit-logs.md |
| Which plan includes SAML SSO? | 1 | product/saml-sso.md, meeting-notes/2025-05-20-product-review.md, it-security/tools/okta.md, product/rbac.md |
| What is the API rate limit on the Growth plan? | 1 | product/api-rate-limits.md, operations/sla-tiers.md, product/data-export.md, product/retention-settings.md |
| What is the default hot data retention? | 1 | product/retention-settings.md, engineering/architecture-overview.md, product/audit-logs.md, engineering/runbooks/log-store.md |
| Which plans include audit logs? | 1 | product/audit-logs.md, product/retention-settings.md, product/rbac.md, product/anomaly-detection.md |
| What does error OKTA-403 mean? | 1 | it-security/tools/okta.md, engineering/runbooks/auth-service.md, engineering/runbooks/config-service.md |
| How do I report a security incident? | 1 | it-security/data-classification-policy.md, engineering/incident-response-runbook.md, meeting-notes/2025-06-02-security-review.md, engineering/postmortems/inc-2025-048.md |
| What is the deploy freeze policy? | 1 | engineering/deployment-and-release-process.md, product/feature-flag-policy.md, engineering/git-workflow.md, hr/parental-leave.md |
| What is the refund approval limit for a support agent? | 2 | faq/refunds.md, operations/customer-refund-sop.md, operations/discount-approval.md, onboarding/support-agent.md |
| What is the on-call stipend? | 1 | faq/oncall.md, engineering/oncall-policy.md, hr/benefits-overview.md, hr/remote-work-policy.md |

_Abstention set (5 questions) evaluated in Phase 3._
