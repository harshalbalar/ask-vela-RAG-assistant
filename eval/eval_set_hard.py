"""HARD retrieval eval set — realistic *messy* queries.

Same gold documents as eval_set.py, but the questions are paraphrased, use
synonyms/acronyms ("Deutschland", "Britain", "maternity", "bounce"), quote error
codes loosely, and sit among lexical distractors. This is where pure semantic
search starts to slip and where hybrid search + a re-ranker earn their keep.
"""

ANSWERABLE = [
    # --- service runbooks: symptom/synonym phrasing, no exact service name ---
    ("The invoicing service is down — how do I bounce it?",
     ["engineering/runbooks/billing-service.md"]),
    ("I'm seeing a 429 from the query layer, what's going on?",
     ["engineering/runbooks/query-service.md"]),
    ("Which port does our event ingestion endpoint listen on?",
     ["engineering/runbooks/ingest-api.md"]),
    ("Who's responsible for the alerts emailer?",
     ["engineering/runbooks/notification-service.md"]),
    ("What's wrong when stream processing throws a 418?",
     ["engineering/runbooks/stream-processor.md"]),

    # --- postmortems: described, not by ID ---
    ("Post-mortem for the EU query timeouts back in March?",
     ["engineering/postmortems/inc-2025-031.md"]),
    ("Why did we send customers double bills that one time?",
     ["engineering/postmortems/inc-2025-042.md"]),
    ("What broke our logins in late April?",
     ["engineering/postmortems/inc-2025-048.md"]),

    # --- region HR: synonyms / place nicknames ---
    ("Holiday allowance for staff in Deutschland?",
     ["hr/regions/germany/pto.md"]),
    ("Time-off entitlement for our Bangalore team?",
     ["hr/regions/india/pto.md"]),
    ("How much notice must I give to quit in Britain?",
     ["hr/regions/uk/notice-period.md"]),
    ("How many bank holidays do we get in Germany?",
     ["hr/regions/germany/public-holidays.md"]),
    ("How long is maternity leave in the UK?",
     ["hr/regions/uk/parental-leave.md"]),
    ("Can I carry over unused leave in Germany?",
     ["hr/regions/germany/pto.md"]),

    # --- IT / security: device & access synonyms, loose codes ---
    ("How do I connect to the corporate VPN?",
     ["it-security/tools/tailscale.md", "it-security/vpn-and-access.md"]),
    ("Do I need two-factor for our code repo?",
     ["it-security/tools/github.md"]),
    ("What's the 403 from our identity provider about?",
     ["it-security/tools/okta.md", "it-security/vpn-and-access.md"]),
    ("Who do I tell if I think there's been a breach?",
     ["it-security/data-classification-policy.md"]),

    # --- operations: paraphrase + distractors ---
    ("What's the uptime promise on our top-tier plan?",
     ["operations/sla-tiers.md"]),
    ("Biggest markdown a salesperson can offer on their own?",
     ["operations/discount-approval.md"]),
    ("What's the turnaround for a right-to-be-forgotten request?",
     ["operations/data-deletion-gdpr.md"]),
    ("After a customer leaves, when do we wipe their data?",
     ["operations/customer-offboarding.md"]),

    # --- product: tier paraphrase + limit phrasing ---
    ("Which tier do I need for single sign-on with SAML?",
     ["product/saml-sso.md"]),
    ("Calls-per-minute cap on the mid plan?",
     ["product/api-rate-limits.md"]),
    ("How long do we keep recent data hot?",
     ["product/retention-settings.md"]),

    # --- cross-doc paraphrases of original docs ---
    ("Can I push to prod on a Friday afternoon?",
     ["engineering/deployment-and-release-process.md"]),
    ("How much do I get for carrying the pager?",
     ["engineering/oncall-policy.md", "faq/oncall.md"]),
]

ABSTAIN = [
    "Does Vela Cloud offer a sabbatical?",
    "What is the pet insurance policy?",
    "How big is the signing bonus for new engineers?",
]
