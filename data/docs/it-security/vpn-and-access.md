# VPN & System Access

**Owner:** IT · **Last updated:** 2025-04-05 · **Doc ID:** IT-VPN-016

## VPN
Vela Cloud uses **Tailscale** for access to internal systems. Install it from the IT self-service
portal and sign in with your Okta SSO account. Production database access additionally requires
approval in Okta and is logged.

## Single sign-on
All apps are behind **Okta SSO**. If you lose access, raise a ticket in the IT portal or message
`#it-help` in Slack.

## Access requests
Request access to a new system via Okta. Requests route to the system owner and are reviewed
quarterly in an access audit. Access not used for 60 days is automatically revoked.

## Error codes
If you see `OKTA-403` you lack a group assignment; `VPN-110` means Tailscale is not running.
