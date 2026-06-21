# SOP: Customer Refunds

**Owner:** Customer Operations · **Last updated:** 2025-04-22 · **Doc ID:** OPS-REF-018

## When a refund applies
Refunds may be issued for billing errors, verified service outages breaching the SLA, or within
**14 days** of an annual plan upgrade (cooling-off period).

## Approval
- Refunds **under $500**: support agent may approve directly.
- **$500–$5,000**: requires Customer Operations manager approval.
- Over **$5,000**: requires Finance approval.

## Process
1. Verify the customer and the charge in Stripe.
2. Log the reason in the CRM (HubSpot) under the account.
3. Issue the refund in Stripe; SLA-breach credits are applied as account credit, not cash, unless requested.
4. Email the customer confirmation within 1 business day.

## SLA credits
For a confirmed SLA breach, credits follow the published SLA: 10% credit for <99.9% uptime, 25% for <99.0%.
