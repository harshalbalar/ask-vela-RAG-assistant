"""Labeled retrieval eval set (auto-generated). Edit freely.

Each ANSWERABLE entry maps a question to the document(s) that should be
retrieved. ABSTAIN questions have no supporting document; the system should
say it does not know (answer-quality check comes in Phase 3).
"""

ANSWERABLE = [
    ('How do I restart the billing-service?', ['engineering/runbooks/billing-service.md']),
    ('What does error QRY-429 mean?', ['engineering/runbooks/query-service.md']),
    ('What port does the ingest-api run on?', ['engineering/runbooks/ingest-api.md']),
    ('What is the common alert for the search-service?', ['engineering/runbooks/search-service.md']),
    ('Which team owns the notification-service?', ['engineering/runbooks/notification-service.md']),
    ('What does STR-418 indicate?', ['engineering/runbooks/stream-processor.md']),
    ('What caused incident INC-2025-031?', ['engineering/postmortems/inc-2025-031.md']),
    ('What was the root cause of the duplicate invoices incident?', ['engineering/postmortems/inc-2025-042.md']),
    ('Why did login failures spike in incident INC-2025-048?', ['engineering/postmortems/inc-2025-048.md']),
    ('How many vacation days do employees in Germany get?', ['hr/regions/germany/pto.md']),
    ('How much PTO do employees in India receive?', ['hr/regions/india/pto.md']),
    ('What is the notice period in the UK?', ['hr/regions/uk/notice-period.md']),
    ('How many public holidays are there in Germany?', ['hr/regions/germany/public-holidays.md']),
    ('Parental leave for the birthing parent in the UK?', ['hr/regions/uk/parental-leave.md']),
    ('What is the vacation rollover rule in Germany?', ['hr/regions/germany/pto.md']),
    ('How do I get access to Tailscale?', ['it-security/tools/tailscale.md']),
    ('Is 2FA required for GitHub?', ['it-security/tools/github.md']),
    ('What uptime does the Enterprise SLA guarantee?', ['operations/sla-tiers.md']),
    ('What discount can a sales rep give without approval?', ['operations/discount-approval.md']),
    ('How long do we have to fulfil a GDPR data deletion request?', ['operations/data-deletion-gdpr.md']),
    ('When does customer data get permanently deleted after cancellation?', ['operations/customer-offboarding.md']),
    ('Which plan includes SAML SSO?', ['product/saml-sso.md']),
    ('What is the API rate limit on the Growth plan?', ['product/api-rate-limits.md']),
    ('What is the default hot data retention?', ['product/retention-settings.md']),
    ('Which plans include audit logs?', ['product/audit-logs.md']),
    ('What does error OKTA-403 mean?', ['it-security/vpn-and-access.md', 'it-security/tools/okta.md']),
    ('How do I report a security incident?', ['it-security/data-classification-policy.md']),
    ('What is the deploy freeze policy?', ['engineering/deployment-and-release-process.md']),
    ('What is the refund approval limit for a support agent?', ['operations/customer-refund-sop.md']),
    ('What is the on-call stipend?', ['engineering/oncall-policy.md', 'faq/oncall.md']),
]

ABSTAIN = [
    'Does Vela Cloud offer a sabbatical?',
    'What is the pet insurance policy?',
    'How big is the signing bonus for new engineers?',
    "What is the company's stock ticker symbol?",
    'What is the dental reimbursement amount in Japan?',
]
