# Retrieval Eval — rerank-local

- Generated: 2026-06-21 14:41 UTC
- Mode: **rerank** · Set: **hard** · top_k=4
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2` · chunk_size=1000, overlap=150

| Metric | Value |
|---|---|
| Hit@4 | 0.963 |
| MRR | 0.861 |
| P@4 | 0.275 |
| R@4 | 0.963 |

## Per-question

| Question | First gold rank | Top retrieved |
|---|---|---|
| The invoicing service is down — how do I bounce it? | 1 | engineering/runbooks/billing-service.md, engineering/postmortems/inc-2025-042.md, engineering/runbooks/notification-service.md, operations/support-escalation-process.md |
| I'm seeing a 429 from the query layer, what's going on? | 1 | engineering/runbooks/query-service.md, product/velaql-functions.md, engineering/postmortems/inc-2025-031.md |
| Which port does our event ingestion endpoint listen on? | 1 | engineering/runbooks/ingest-api.md, engineering/postmortems/inc-2025-037.md, engineering/runbooks/stream-processor.md, engineering/runbooks/trace-collector.md |
| Who's responsible for the alerts emailer? | 1 | engineering/runbooks/notification-service.md, engineering/postmortems/inc-2025-069.md, engineering/runbooks/alerting-service.md, product/alert-rules.md |
| What's wrong when stream processing throws a 418? | 1 | engineering/runbooks/stream-processor.md, engineering/postmortems/inc-2025-051.md, engineering/architecture-overview.md |
| Post-mortem for the EU query timeouts back in March? | 1 | engineering/postmortems/inc-2025-031.md, engineering/runbooks/query-service.md, engineering/architecture-overview.md, meeting-notes/2025-06-18-hr-policy.md |
| Why did we send customers double bills that one time? | 1 | engineering/postmortems/inc-2025-042.md, operations/customer-refund-sop.md, hr/remote-work-policy.md, operations/customer-offboarding.md |
| What broke our logins in late April? | 1 | engineering/postmortems/inc-2025-048.md, engineering/postmortems/inc-2025-069.md, engineering/postmortems/inc-2025-055.md, engineering/postmortems/inc-2025-064.md |
| Holiday allowance for staff in Deutschland? | 2 | hr/regions/germany/public-holidays.md, hr/regions/germany/pto.md, hr/regions/uk/public-holidays.md, hr/parental-leave.md |
| Time-off entitlement for our Bangalore team? | **MISS** | faq/time-off.md, hr/pto-and-leave-policy.md, hr/regions/india/notice-period.md |
| How much notice must I give to quit in Britain? | 1 | hr/regions/uk/notice-period.md, hr/regions/us/notice-period.md, hr/regions/germany/notice-period.md, hr/regions/india/notice-period.md |
| How many bank holidays do we get in Germany? | 1 | hr/regions/germany/public-holidays.md, hr/regions/germany/pto.md, hr/parental-leave.md, hr/regions/germany/parental-leave.md |
| How long is maternity leave in the UK? | 1 | hr/regions/uk/parental-leave.md, hr/regions/us/parental-leave.md, hr/parental-leave.md, hr/regions/germany/parental-leave.md |
| Can I carry over unused leave in Germany? | 1 | hr/regions/germany/pto.md, hr/parental-leave.md, hr/regions/germany/parental-leave.md, hr/pto-and-leave-policy.md |
| How do I connect to the corporate VPN? | 2 | faq/vpn.md, it-security/tools/tailscale.md, it-security/vpn-and-access.md, meeting-notes/2025-06-10-ops-standup.md |
| Do I need two-factor for our code repo? | 1 | it-security/tools/github.md, engineering/coding-standards.md, operations/discount-approval.md, it-security/password-and-mfa-policy.md |
| What's the 403 from our identity provider about? | 1 | it-security/tools/okta.md, it-security/vpn-and-access.md, engineering/runbooks/auth-service.md, hr/code-of-conduct.md |
| Who do I tell if I think there's been a breach? | 2 | faq/refunds.md, it-security/data-classification-policy.md, engineering/incident-response-runbook.md, operations/customer-refund-sop.md |
| What's the uptime promise on our top-tier plan? | 1 | operations/sla-tiers.md, operations/support-escalation-process.md, hr/regions/us/parental-leave.md, hr/regions/uk/parental-leave.md |
| Biggest markdown a salesperson can offer on their own? | 1 | operations/discount-approval.md, meeting-notes/2025-06-10-ops-standup.md, operations/support-escalation-process.md, hr/remote-work-policy.md |
| What's the turnaround for a right-to-be-forgotten request? | 1 | operations/data-deletion-gdpr.md, operations/customer-offboarding.md, it-security/vpn-and-access.md, it-security/tools/1password.md |
| After a customer leaves, when do we wipe their data? | 1 | operations/customer-offboarding.md, operations/data-deletion-gdpr.md, it-security/data-classification-policy.md, engineering/incident-response-runbook.md |
| Which tier do I need for single sign-on with SAML? | 1 | product/saml-sso.md, it-security/tools/okta.md, it-security/vpn-and-access.md, meeting-notes/2025-05-20-product-review.md |
| Calls-per-minute cap on the mid plan? | 4 | faq/oncall.md, engineering/oncall-policy.md, operations/sla-tiers.md, product/api-rate-limits.md |
| How long do we keep recent data hot? | 1 | product/retention-settings.md, engineering/git-workflow.md, operations/data-deletion-gdpr.md, faq/laptops.md |
| Can I push to prod on a Friday afternoon? | 2 | product/alert-rules.md, engineering/deployment-and-release-process.md, product/custom-dashboards.md, product/audit-logs.md |
| How much do I get for carrying the pager? | 1 | faq/oncall.md, engineering/oncall-policy.md, operations/vendor-onboarding.md, faq/expenses.md |
