# Adspirer Search Ads for Muse

PPC and paid search agent for Google Ads and Microsoft Advertising (Bing Ads). Research keywords and competitor ads, review search performance, find wasted spend, audit conversion tracking, and plan, create and optimize search campaigns, with your approval before any change that affects spend.

This is Adspirer's company-owned **submission kit for the Muse hosted MCP connector** covering Google Ads and Microsoft Advertising (Bing Ads). It is not a Muse plugin runtime. The hosted Adspirer service is the runtime; this repository holds review materials only. The main connector, covering every platform, has its own kit at [Adspirer/adspirer-muse-connector](https://github.com/Adspirer/adspirer-muse-connector).

## Connection

| Field | Value |
| --- | --- |
| Connection type | Existing MCP |
| Endpoint | `https://mcp.adspirer.com/search-ads` |
| Transport | Streamable HTTP |
| Authentication | OAuth with PKCE (S256) |
| Registration | Dynamic client registration |
| Support | support@adspirer.com |

## Connector overview (guidelines §5.1)

- Who it's for: small businesses, in-house marketers and PPC agencies running Google Ads or Microsoft Advertising.
- What it does: keyword research with volume and CPC, search-term and wasted-spend analysis, negative keywords, bid and budget changes, responsive search ad copy, conversion-tracking audits, and paused campaign creation on Google Ads (Search, Shopping, Performance Max) and Microsoft Advertising.
- Why it beats the browser: it reads the user's own ad accounts through the platforms' APIs, so the answer is the account's real data. It finishes the change in the account after approval rather than sending the user to the Google Ads or Microsoft Advertising UI.
- Optional context: Google Analytics 4, Search Console and Tag Manager, when the user has connected them in Adspirer.

An Adspirer account and admin access to at least one Google Ads or Microsoft Advertising account (read-only access is enough for reporting).

## Tools

15 top-level tools, each classified Read, Write or Sensitive write in [submission/TOOLS.md](submission/TOOLS.md). Every platform has a read-only router that the server enforces, and every write router asks for confirmation on the server before it runs.

## Submission workflow

1. Review `submission/connector.json`, `submission/FORM.md` and `submission/TOOLS.md`. The JSON is our internal source of truth, **not a published Muse manifest format**.
2. Run `python3 scripts/package.py --check` and `python3 scripts/package.py`.
3. Complete the [reviewer checklist](submission/REVIEWER.md) and arrange reviewer access privately.
4. Use the [Muse submission portal](https://muse.ai/platform). Copy the form details, upload the Adspirer icon, and attach or link the tool documentation.
5. Record the receipt and review state in a submission-tracking issue. Never put credentials or private reviewer details in public issues.

CI validates and builds a reviewer ZIP on pushes, pull requests and manual runs. It never submits to Muse.

## Status

Kit prepared 2026-11-02. Not yet submitted. Muse authorization and live tool execution remain to be verified in Muse.

## Documentation

- [Muse setup](https://www.adspirer.com/docs/ai-clients/muse)
- [MCP documentation](https://www.adspirer.com/docs/mcp)
- [Tool catalog](https://www.adspirer.com/docs/agent-skills/tools)
- [Security and data handling](https://www.adspirer.com/docs/knowledge-base/security)
- [Privacy policy](https://www.adspirer.com/privacy)
