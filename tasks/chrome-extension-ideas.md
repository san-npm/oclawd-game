# Chrome Extension Portfolio Ideas — Solo Dev, $50-500/mo Each

*Researched Feb 2026. Goal: portfolio of 10-15 small extensions, not one big hit.*

## Strategy Summary

The proven playbook from successful indie devs (Easy Folders at $3.7k MRR, CSS Scan at $100k+, the dev with 4 extensions at $15k MRR total):
- **One sharp pain point** per extension
- **Freemium** with generous free tier → $2-5/mo subscription or $5-15 one-time
- **Chrome Web Store SEO** is your entire distribution — nail the title, description, screenshots
- **Platform-specific tools** outperform generic productivity tools (less competition, higher willingness to pay)

---

## Tier A — Highest Confidence (Low Competition + Clear Pain + Proven Demand)

### 1. Tab Session Saver with Smart Groups
**What:** Save and restore groups of tabs as named sessions (e.g., "Work Project X", "Tax Season", "Side Hustle") with one click.
**Target:** Knowledge workers who juggle multiple projects and have 50+ tabs open.
**Competitors:** Session Buddy (~800k users, hasn't been updated in years, many complaints about bugs and lost sessions). OneTab (2M+ users but is a tab minimizer, not a session organizer). Toby (~300k, different UX focus).
**Why it works:** Session Buddy is essentially abandoned. Users are begging for a maintained alternative. The 1-star reviews are a goldmine — data loss, sync issues, no cloud backup.
**Monetization:** Free for 5 sessions, $3/mo for unlimited + cloud sync. Realistic: $150-400/mo with 50-130 subscribers.
**Build time:** 2 days

### 2. Meeting Link Quick-Launcher
**What:** Detects upcoming calendar meetings (Google Calendar) and shows a floating button to join the call (Zoom/Meet/Teams) 2 minutes before, no tab-switching needed.
**Target:** Remote workers who attend 5+ meetings/day.
**Competitors:** Very few doing this as a standalone extension. Most are inside calendar apps themselves. "Meeting Scheduler" extensions focus on booking, not joining.
**Why it works:** The friction of: open calendar → find meeting → click link → wait for app — happens 5-10x/day. Saving 30 seconds each time feels magical.
**Monetization:** Free for Google Meet only, $2/mo for Zoom+Teams+Webex support. Realistic: $100-300/mo.
**Build time:** 1.5 days (Google Calendar API + content script injection)

### 3. LinkedIn Post Formatter
**What:** Rich text formatting toolbar for LinkedIn posts — bullet points, line breaks, bold/italic via Unicode, emoji shortcuts, post templates, and character counter.
**Target:** LinkedIn creators and B2B marketers posting daily.
**Competitors:** AuthoredUp (~30k users, $20/mo — expensive!). LinkedIn Post Inspector (small, limited). Few others.
**Why it works:** AuthoredUp charges $20/mo which is absurd for formatting. A $3/mo tool that does 80% of what AuthoredUp does will steal their low end. LinkedIn's native editor is garbage — every daily poster feels this pain.
**Monetization:** Free basic formatting, $3/mo for templates + analytics + scheduling hints. Realistic: $200-500/mo.
**Build time:** 2 days

### 4. YouTube Playlist Duration & Progress Tracker
**What:** Shows total playlist duration, remaining time, tracks which videos you've watched, and estimates completion time.
**Target:** Students, course-takers, tutorial followers using YouTube as a learning platform.
**Competitors:** A few basic "playlist length" calculators (~10-50k users each) but none track progress or show remaining time in a persistent way.
**Why it works:** Millions use YouTube playlists for learning. Knowing "I'm 40% through this 8-hour course, 4h48m remaining" is genuinely useful. No one does the progress tracking well.
**Monetization:** Free basic duration calc, $5 one-time for progress tracking + cross-device sync. Realistic: $100-300/mo.
**Build time:** 1.5 days

### 5. Google Docs Word/Page Counter Overlay
**What:** Persistent floating widget showing real-time word count, page count, reading time, and paragraph count — visible while scrolling through Google Docs.
**Target:** Writers, students, content marketers who need to hit word counts.
**Competitors:** Google Docs has a built-in word counter but it's buried in a menu, not persistent. A few extensions exist but most are poorly maintained or have <5k users.
**Why it works:** Writers check word count obsessively. Having it always visible (like Scrivener does natively) is a no-brainer. Simple to build, simple to sell.
**Monetization:** Free basic counter, $3 one-time for per-section counts + target goals + daily writing stats. Realistic: $50-150/mo.
**Build time:** 1 day

---

## Tier B — Good Confidence (Validated Demand, Slightly More Competition)

### 6. Email Follow-Up Reminder (Gmail)
**What:** Right-click an email in Gmail → "Remind me if no reply in X days." Gets a notification if the recipient hasn't replied.
**Target:** Salespeople, freelancers, anyone who sends emails that need responses.
**Competitors:** Boomerang (large, $5-15/mo — overkill for many). Mailtrack (tracking focused). Right Inbox (feature-heavy).
**Why it works:** Boomerang et al. are bloated suites. Many users just want the "remind me if no reply" feature and nothing else. A $2/mo single-purpose tool undercuts the big guys.
**Monetization:** Free for 5 reminders/mo, $2/mo for unlimited. Realistic: $100-300/mo.
**Build time:** 2 days

### 7. Notion Template Quick-Insert
**What:** A popup that lets you quickly create Notion pages from templates without opening Notion — select a template, fill a few fields, and it creates the page via Notion API.
**Target:** Notion power users who log daily notes, meeting notes, habits, etc.
**Competitors:** Notion Web Clipper (saves pages TO Notion, doesn't create FROM templates). Save to Notion (~100k users, similar but different). Very few do quick-create from templates.
**Why it works:** Notion's own new-page flow requires: open Notion → navigate to workspace → pick template → fill in. This skips all that. Daily habit loggers would use this 1-5x/day.
**Monetization:** Free for 1 template, $3/mo for unlimited templates + custom fields. Realistic: $100-250/mo.
**Build time:** 2 days

### 8. Auto-Expand All / Read More Clicker
**What:** Automatically clicks all "Read more", "Show more", "See all replies" buttons on a page so you can read full content without clicking 20 times.
**Target:** Anyone browsing LinkedIn, Reddit, Amazon reviews, news sites, forums.
**Competitors:** A few niche scripts exist, but no polished general-purpose extension with good UX. "Auto Expand" has a couple with <5k users.
**Why it works:** This is a universally annoying UX pattern. LinkedIn alone truncates every single post. The extension is dead simple technically (content script that queries for common button patterns). Monetize via a "site pack" model.
**Monetization:** Free for 5 sites, $5 one-time for all sites + custom site rules. Realistic: $50-200/mo.
**Build time:** 1 day

### 9. Screenshot-to-Clipboard with Annotation
**What:** Select any area of a page, annotate it (arrows, boxes, blur sensitive info), and copy straight to clipboard — no file saving, no extra app.
**Target:** Anyone who shares screenshots in Slack/Discord/email daily (developers, PMs, support).
**Competitors:** Awesome Screenshot (~2M users, bloated), Nimbus (~1M users, wants you to sign up), GoFullPage (full page only). The market is big but existing tools are overengineered.
**Why it works:** The key differentiator: zero-friction. No account, no cloud upload, no bloat. Select → annotate → clipboard. Done. Target users frustrated by Awesome Screenshot's signup walls and Nimbus's complexity.
**Monetization:** Free basic capture, $8 one-time for blur tool + templates + auto-upload to Imgur/S3. Realistic: $100-300/mo.
**Build time:** 2-3 days

### 10. Price History Tracker for Niche Stores
**What:** Shows price history charts on product pages for stores OTHER than Amazon — like Walmart, Target, Best Buy, B&H Photo, Newegg.
**Target:** Bargain shoppers who buy electronics/home goods from non-Amazon stores.
**Competitors:** CamelCamelCamel/Keepa dominate Amazon. Honey shows coupons. But specific price history for Walmart/Target/B&H is barely covered.
**Why it works:** The Amazon price-tracking space is saturated, but the same demand exists for every other retailer. Start with 3-5 stores, add more over time. You're the Keepa of non-Amazon.
**Monetization:** Free for 1 store, $3/mo for all stores + price drop alerts. Realistic: $100-400/mo.
**Build time:** 2-3 days (scraping + chart rendering)

---

## Tier C — Speculative but Interesting (Less Validated, Worth Testing)

### 11. Twitter/X Thread Reader with Highlights
**What:** Unrolls Twitter threads into clean readable format AND lets you highlight/save key passages to a personal archive.
**Target:** Twitter power users, researchers, content curators.
**Competitors:** Thread Reader App (huge but is a bot, not an extension). A few small unroller extensions exist. None combine unrolling + highlighting + archiving.
**Why it works:** The highlight + save angle is what differentiates. Thread Reader just unrolls. This creates a personal knowledge base from threads.
**Monetization:** Free unrolling, $3/mo for highlights + search + export. Realistic: $50-200/mo.
**Build time:** 2 days

### 12. Freelancer Invoice Timer
**What:** Floating timer that tracks time per client/project and generates a simple invoice PDF with hours + rates — right from the browser toolbar.
**Target:** Freelancers billing hourly (designers, developers, consultants).
**Competitors:** Toggl (full app, not extension-first). Clockify (similar). Harvest (enterprise). No lightweight extension-only solution that goes timer → invoice in one click.
**Why it works:** Most freelancers don't need Toggl's full project management. They need: start timer → stop timer → generate invoice. The "extension-only, no webapp required" angle is the moat.
**Monetization:** Free for 1 client, $4/mo for unlimited clients + PDF branding + export. Realistic: $100-300/mo.
**Build time:** 2-3 days

### 13. Color Palette Extractor from Any Page
**What:** Click to extract the full color palette of any website — shows hex/RGB/HSL values, generates a downloadable palette, and copies to clipboard.
**Target:** Designers, front-end developers, brand managers.
**Competitors:** ColorZilla (~4M users, but it's a single-pixel picker, not a full-page palette extractor). CSS Peeper (~200k). Eye Dropper.
**Why it works:** ColorZilla picks ONE color. This extracts the ENTIRE palette (dominant colors, accent colors, background colors) programmatically. Different use case. CSS Scan proved devs pay for browser tools.
**Monetization:** Free for 5 palettes, $7 one-time for unlimited + export to Figma/Sketch format + palette history. Realistic: $50-200/mo.
**Build time:** 1.5 days

### 14. Cookie Consent Auto-Clicker (Privacy Mode)
**What:** Automatically rejects all non-essential cookies on GDPR/CCPA consent popups across all sites.
**Target:** Privacy-conscious users, especially in Europe.
**Competitors:** "I don't care about cookies" (~1M users, was acquired by Avast and now ACCEPTS all cookies — completely opposite of what many users want). Consent-O-Matic (~50k users, good but niche). Super Agent (~100k).
**Why it works:** "I don't care about cookies" used to reject but now accepts — users feel betrayed (visible in reviews). There's a clear gap for a tool that specifically REJECTS non-essential cookies and is transparent about it. Trust + privacy messaging.
**Monetization:** Free with optional donation / $2/mo for stats dashboard showing how many trackers blocked. Realistic: $50-200/mo (hard to monetize privacy users, but volume compensates).
**Build time:** 2 days

### 15. Google Sheets Formula Helper
**What:** Sidebar that explains what a selected formula does in plain English, suggests fixes for errors, and offers a natural-language-to-formula converter.
**Target:** Non-technical Sheets users (marketers, ops people, small business owners).
**Competitors:** Numerous AI tools exist broadly, but few are embedded directly in Google Sheets as an extension. SheetAI (~50k users) and a handful of others.
**Why it works:** The key is it works in-context — select a cell, see explanation in sidebar. No copy-paste to ChatGPT. Uses your own API key (BYOK) to keep costs zero for you.
**Monetization:** Free for 20 queries/day, $3/mo for unlimited + BYOK option. Realistic: $100-300/mo.
**Build time:** 2 days

### 16. Bookmark Deduplicator & Dead Link Checker
**What:** Scans your bookmarks, finds duplicates, detects dead links (404s), and lets you clean up in bulk.
**Target:** Anyone with 500+ bookmarks accumulated over years.
**Competitors:** A few old extensions exist but most are abandoned or have <10k users. "Bookmark Manager" extensions focus on organizing, not cleaning.
**Why it works:** Everyone has bookmark rot. This is a utility you run once a month. Dead simple to build, universally useful, and the "wow, I had 200 dead links" moment drives word-of-mouth.
**Monetization:** Free for scan + report, $5 one-time for bulk actions + scheduled auto-scan. Realistic: $50-150/mo.
**Build time:** 1 day

### 17. Focus Mode: Hide Distracting Elements
**What:** One-click to hide comments, sidebars, recommended videos, and feeds on YouTube, Twitter, LinkedIn, Reddit, and news sites.
**Target:** People trying to use these platforms for work without falling into doom-scrolling.
**Competitors:** DF Tube (~300k, YouTube only). Unhook (~500k, YouTube only). News Feed Eradicator (~200k, Facebook/Twitter). No single tool covers ALL major platforms.
**Why it works:** Existing tools are single-platform. A unified "focus mode" across YouTube + Twitter + LinkedIn + Reddit with per-site toggles is genuinely useful and doesn't exist as one cohesive product.
**Monetization:** Free for 2 sites, $3/mo for all sites + custom element hiding + scheduled focus hours. Realistic: $100-300/mo.
**Build time:** 2 days

---

## ❌ Killed Ideas (and Why)

| Idea | Reason Killed |
|------|--------------|
| **Ad blocker** | uBlock Origin is free and perfect. Zero chance. |
| **Password manager** | Bitwarden is free and open-source. Can't compete. |
| **Tab manager** | Too many good free options (Arc, Tab Manager Plus, OneTab). |
| **Grammar checker** | Grammarly and LanguageTool dominate completely. |
| **Amazon price tracker** | CamelCamelCamel + Keepa = unbeatable free combo. |
| **Coupon finder** | Honey (PayPal-backed), Capital One Shopping — can't compete with free + massive databases. |
| **AI chatbot sidebar** | Dozens exist, most free. ChatGPT/Claude native sidebars incoming. |
| **Dark mode** | Dark Reader (5M+ users, free, excellent). Dead on arrival. |
| **New tab dashboard** | Momentum (3M+), dozens of alternatives. Saturated. |
| **Screen recorder** | Loom is free tier is good enough. OBS exists. |
| **Shopify spy/detector** | Wappalyzer and BuiltWith are free and comprehensive. |
| **Amazon FBA tools** | Helium 10, Jungle Scout, AMZScout — VC-backed, can't compete as solo dev. |

---

## Recommended Build Order (Effort vs. Revenue Potential)

1. **#8 Auto-Expand All** — 1 day build, universal pain, easy to validate
2. **#5 Google Docs Word Counter** — 1 day build, simple, writers love it
3. **#16 Bookmark Deduplicator** — 1 day build, utility play, good reviews potential
4. **#3 LinkedIn Post Formatter** — 2 days, clear undercut of $20/mo AuthoredUp
5. **#1 Tab Session Saver** — 2 days, proven demand from Session Buddy's decay
6. **#4 YouTube Playlist Progress** — 1.5 days, students = great audience
7. **#17 Focus Mode Multi-Platform** — 2 days, wellness angle, growing market
8. **#2 Meeting Link Launcher** — 1.5 days, remote work staple
9. **#15 Sheets Formula Helper** — 2 days, BYOK model = zero server costs
10. **#6 Email Follow-Up Reminder** — 2 days, clear Boomerang undercut

Build the first 3 in your first week. Ship fast, iterate based on reviews, move to the next.

---

## Revenue Projections (Conservative)

| Scenario | Extensions | Avg Revenue Each | Monthly Total |
|----------|-----------|-----------------|---------------|
| **Minimum viable** | 5 live | $80/mo | $400/mo |
| **Portfolio mode** | 10 live | $120/mo | $1,200/mo |
| **Optimized** | 10 live | $250/mo | $2,500/mo |

The magic of the portfolio approach: you don't need any single extension to be a hit. You need 10 extensions each making $100-250/mo. Chrome Web Store SEO + reviews compound over time. The first 6 months are slow; months 6-12 is when organic traffic kicks in.

---

*Last updated: Feb 28, 2026*
