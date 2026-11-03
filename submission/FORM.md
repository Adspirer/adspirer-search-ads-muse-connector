# Muse form mapping

Use `connector.json` for the copy/paste values. It is Adspirer-owned metadata, not a Muse API payload.

| Form field | JSON field or instruction |
| --- | --- |
| Connector name | name |
| Company or developer | company |
| Product website | productWebsite |
| Example prompts | examplePrompts, one per paragraph |
| Connector icon | Upload assets/icon.svg (512x512 Adspirer branding, not Meta's logo) |
| Payments | Choose the option that describes the Adspirer subscription accurately. Do not imply Stripe Link checkout support. |
| Your name | The submitting person's full name |
| Work email | contactEmail |
| Support email or URL | supportEmail |
| Privacy policy | privacyPolicy |
| Terms of service | termsOfService |
| Connection type | connectionType |
| Hosted MCP endpoint | endpoint |
| API or MCP documentation | documentation, plus submission/TOOLS.md for per-tool classes |
| Access requirements | accessRequirements |
| Authentication | OAuth with PKCE |

## Anything else

Official Adspirer company repository for this connector: https://github.com/Adspirer/adspirer-search-ads-muse-connector. This is one of Adspirer's focused connectors, covering Google Ads and Microsoft Advertising (Bing Ads) at `https://mcp.adspirer.com/search-ads`. Our main connector, covering every platform, is submitted separately from https://github.com/Adspirer/adspirer-muse-connector. Every platform has a read-only router enforced by the server, write routers ask for confirmation on the server before running, and new campaigns are always created paused. Per-tool Read, Write and Sensitive-write classes are in submission/TOOLS.md. We can arrange reviewer access privately through support@adspirer.com.

## Before sending

Re-check the live tool list against TOOLS.md, confirm contact details and plan or region requirements, and read the current portal terms. Do not mark end-to-end tests as passed until they run inside Muse.
