# Engineering Incident Response Runbook

**Owner:** SRE · **Last updated:** 2025-05-02 · **Doc ID:** ENG-INC-009

This runbook covers **production engineering incidents** (outages, degradations). For *security*
incidents (breach, data exposure) follow IT-SEC-013 instead.

## Severity levels
- **SEV1** — full outage or data loss. Page immediately. Target mitigation < 30 min.
- **SEV2** — major feature degraded for many tenants. Target mitigation < 2 hours.
- **SEV3** — minor or single-tenant issue. Handle in business hours.

## First responder steps
1. Acknowledge the page in PagerDuty within **5 minutes**.
2. Open an incident channel `#inc-<date>-<short-name>` in Slack.
3. Assign an Incident Commander (IC) for SEV1/SEV2.
4. Post status updates every 15 minutes to the channel.

## After resolution
Write a **blameless postmortem** within 3 business days using the postmortem template.
Every SEV1 requires a postmortem review with the Platform Team.
