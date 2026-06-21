# Retrieval Eval — dense-local

- Generated: 2026-06-21 14:39 UTC
- Mode: **dense** · Set: **hard** · top_k=4
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2` · chunk_size=1000, overlap=150

| Metric | Value |
|---|---|
| Hit@4 | 0.704 |
| MRR | 0.611 |
| P@4 | 0.191 |
| R@4 | 0.685 |

## Per-question

| Question | First gold rank | Top retrieved |
|---|---|---|
| The invoicing service is down — how do I bounce it? | 2 | engineering/postmortems/inc-2025-042.md, engineering/runbooks/billing-service.md, operations/billing-dispute.md |
| I'm seeing a 429 from the query layer, what's going on? | 2 | engineering/postmortems/inc-2025-031.md, engineering/runbooks/query-service.md, product/velaql-functions.md, meeting-notes/2025-05-12-platform-sync.md |
| Which port does our event ingestion endpoint listen on? | 1 | engineering/runbooks/ingest-api.md, engineering/postmortems/inc-2025-037.md, engineering/runbooks/stream-processor.md, engineering/runbooks/alerting-service.md |
| Who's responsible for the alerts emailer? | **MISS** | engineering/postmortems/inc-2025-069.md, engineering/runbooks/alerting-service.md, product/alert-rules.md, meeting-notes/2025-06-24-incident-review.md |
| What's wrong when stream processing throws a 418? | 1 | engineering/runbooks/stream-processor.md, engineering/postmortems/inc-2025-051.md, engineering/postmortems/inc-2025-037.md |
| Post-mortem for the EU query timeouts back in March? | 1 | engineering/postmortems/inc-2025-031.md, engineering/postmortems/inc-2025-060.md, engineering/postmortems/inc-2025-055.md, engineering/postmortems/inc-2025-069.md |
| Why did we send customers double bills that one time? | 1 | engineering/postmortems/inc-2025-042.md, operations/billing-dispute.md, operations/customer-refund-sop.md, engineering/runbooks/billing-service.md |
| What broke our logins in late April? | 1 | engineering/postmortems/inc-2025-048.md, engineering/runbooks/metrics-store.md, engineering/postmortems/inc-2025-055.md, engineering/runbooks/billing-service.md |
| Holiday allowance for staff in Deutschland? | 2 | hr/regions/germany/public-holidays.md, hr/regions/germany/pto.md, hr/regions/uk/public-holidays.md, hr/regions/us/public-holidays.md |
| Time-off entitlement for our Bangalore team? | **MISS** | hr/regions/india/notice-period.md, hr/pto-and-leave-policy.md, faq/time-off.md, hr/regions/india/public-holidays.md |
| How much notice must I give to quit in Britain? | 1 | hr/regions/uk/notice-period.md, hr/regions/us/notice-period.md, hr/regions/germany/notice-period.md, hr/pto-and-leave-policy.md |
| How many bank holidays do we get in Germany? | 1 | hr/regions/germany/public-holidays.md, hr/regions/germany/pto.md, hr/regions/uk/public-holidays.md, hr/regions/us/public-holidays.md |
| How long is maternity leave in the UK? | 1 | hr/regions/uk/parental-leave.md, hr/regions/us/parental-leave.md, hr/regions/uk/notice-period.md, hr/pto-and-leave-policy.md |
| Can I carry over unused leave in Germany? | **MISS** | hr/pto-and-leave-policy.md, hr/regions/germany/notice-period.md, hr/parental-leave.md, hr/regions/germany/parental-leave.md |
| How do I connect to the corporate VPN? | 2 | faq/vpn.md, it-security/tools/tailscale.md, it-security/vpn-and-access.md, hr/remote-work-policy.md |
| Do I need two-factor for our code repo? | 1 | it-security/tools/github.md, engineering/git-workflow.md, product/api-rate-limits.md, operations/discount-approval.md |
| What's the 403 from our identity provider about? | **MISS** | engineering/postmortems/inc-2025-048.md, it-security/data-classification-policy.md, engineering/runbooks/auth-service.md, hr/code-of-conduct.md |
| Who do I tell if I think there's been a breach? | **MISS** | engineering/postmortems/inc-2025-064.md, meeting-notes/2025-06-24-incident-review.md, engineering/postmortems/inc-2025-048.md, engineering/postmortems/inc-2025-031.md |
| What's the uptime promise on our top-tier plan? | 1 | operations/sla-tiers.md, operations/support-escalation-process.md, engineering/oncall-policy.md, hr/new-hire-onboarding.md |
| Biggest markdown a salesperson can offer on their own? | 1 | operations/discount-approval.md, meeting-notes/2025-06-10-ops-standup.md, operations/sla-tiers.md, operations/vendor-onboarding.md |
| What's the turnaround for a right-to-be-forgotten request? | **MISS** | engineering/postmortems/inc-2025-048.md, engineering/postmortems/inc-2025-069.md, operations/support-escalation-process.md, engineering/postmortems/inc-2025-031.md |
| After a customer leaves, when do we wipe their data? | 2 | operations/data-deletion-gdpr.md, operations/customer-offboarding.md, product/feature-flag-policy.md, product/retention-settings.md |
| Which tier do I need for single sign-on with SAML? | 1 | product/saml-sso.md, operations/sla-tiers.md, meeting-notes/2025-05-20-product-review.md, operations/support-escalation-process.md |
| Calls-per-minute cap on the mid plan? | **MISS** | engineering/oncall-policy.md, faq/oncall.md, operations/sla-tiers.md, operations/support-escalation-process.md |
| How long do we keep recent data hot? | 1 | product/retention-settings.md, engineering/architecture-overview.md, faq/laptops.md, operations/data-deletion-gdpr.md |
| Can I push to prod on a Friday afternoon? | **MISS** | hr/new-hire-onboarding.md, engineering/oncall-policy.md, product/api-rate-limits.md, engineering/git-workflow.md |
| How much do I get for carrying the pager? | 1 | faq/oncall.md, faq/expenses.md, hr/expense-and-reimbursement.md, operations/vendor-onboarding.md |
