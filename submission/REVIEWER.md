# Reviewer verification guide

These are planned checks, not completed test results. Arrange a reviewer account privately through support@adspirer.com, with a test Google Ads account (and, if possible, a Microsoft Advertising account). Never commit credentials, customer exports, OAuth codes or state, tokens, or session recordings containing personal data.

1. Start a fresh Muse connection to `https://mcp.adspirer.com/search-ads`. Discover the OAuth metadata and complete the authorization-code flow with PKCE S256.
2. Sign in or sign up to Adspirer, review the requested access, finish authorization and return to Muse. Check both the new-user and returning-user paths.
3. Call `get_connections_status` and confirm the connected test accounts match.
4. Ask for the last seven complete days of performance. Compare with the platform's own UI using the same timezone, currency and attribution window.
5. Read-only boundary: call `google_ads_read` with `action: "execute"` and a mutating `tool_name`. The server must refuse it.
6. Ask for a campaign plan without writes. Check that the assistant asks for missing details and waits for approval.
7. Only with separately approved test-account access: through `google_ads_write`, approve creating a campaign. Check that the server asks for confirmation first, that declining makes no change, and that an accepted create lands **paused** in the ad platform. Never activate a campaign or spend budget during routine review, and coordinate cleanup explicitly.
8. Check denied and revoked authorization, unavailable accounts, insufficient permissions and usage-limit errors. Confirm the assistant does not report success it didn't get.

Record the date, Muse version, test case, expected and actual result, and sanitized evidence.
