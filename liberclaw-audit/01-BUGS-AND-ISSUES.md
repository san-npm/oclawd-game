# LiberClaw.ai — Bugs & Issues Report
**Audit Date:** 2026-02-15
**Site:** https://liberclaw.ai | https://app.liberclaw.ai

---

## 🔴 CRITICAL

### 1. No robots.txt
- `https://liberclaw.ai/robots.txt` → **404**
- Search engines have no crawl directives
- Impact: Uncontrolled crawling, no sitemap reference

### 2. No sitemap.xml
- `https://liberclaw.ai/sitemap.xml` → **404**
- Search engines can't discover pages efficiently
- Impact: Poor indexing, especially for `/manifesto`

### 3. No favicon
- No `<link rel="icon">` in the homepage HTML
- App subdomain has one (`/favicon.ico`) but marketing site doesn't
- Impact: Missing browser tab icon, looks unfinished

### 4. API root returns 404
- `https://api.liberclaw.ai` → `{"detail":"Not Found"}`
- No health endpoint or API docs at root
- Impact: Developers hitting the API get a confusing response

### 5. Zero Open Graph tags
- No `og:title`, `og:description`, `og:image`, `og:url`, `og:type`
- When shared on Twitter/LinkedIn/Discord, the link preview will be blank or ugly
- Impact: **Massive** loss of social media click-through

### 6. Zero Twitter Card tags
- No `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`
- Impact: Same as above — poor social sharing

### 7. No canonical URLs
- No `<link rel="canonical">` on any page
- Impact: Potential duplicate content issues, SEO dilution

---

## 🟡 HIGH

### 8. Missing security headers
Response headers are bare minimum:
- ❌ No `Content-Security-Policy`
- ❌ No `X-Frame-Options`
- ❌ No `X-Content-Type-Options`
- ❌ No `Strict-Transport-Security` (HSTS)
- ❌ No `Referrer-Policy`
- ❌ No `Permissions-Policy`
- ❌ No `X-XSS-Protection`
- Impact: Security audit failures, potential clickjacking, MIME sniffing

### 9. No structured data (JSON-LD)
- No Schema.org markup on any page
- Impact: No rich snippets in Google search results

### 10. Heading hierarchy issues
- H1: "Unstoppable Autonomy." ✅ (only one, good)
- Missing H3 level entirely — jumps from H2 to H4
- H2 text has formatting issues: "DecentralizedInfrastructure" (missing space), "RapidDeployment" (missing space)
- Impact: Accessibility issues, screen reader confusion

### 11. Zero ARIA labels
- `aria-label` count: **0** across entire homepage
- Interactive elements (buttons, nav) lack accessibility attributes
- Impact: WCAG compliance failure

### 12. No alt text infrastructure
- No `<img>` tags found (all visual elements are CSS/SVG)
- The live network map SVG has no `<title>` or `aria-label`
- Impact: Screen readers can't describe the visual content

### 13. Section elements have no IDs
- 6 `<section>` elements, none have `id` attributes
- Only anchor targets are `#features` and `#agents`
- Impact: Deep linking impossible for most sections

---

## 🟢 MEDIUM

### 14. No legal pages
- `/terms` → 404
- `/privacy` → 404
- Impact: Legal compliance risk, especially for EU users (GDPR)

### 15. No pricing page
- `/pricing` → 404
- Users can't find pricing without launching the app
- Impact: Conversion friction

### 16. No documentation
- `/docs` → 404
- Only reference is GitHub repo link
- Impact: Developer adoption barrier

### 17. No blog or content pages
- `/blog` → 404
- Impact: Zero organic SEO content strategy

### 18. Homepage is 105KB of HTML
- Large inline JavaScript for the live network map
- Impact: Slightly slow initial render, though acceptable

### 19. App subdomain has no description meta tag
- `https://app.liberclaw.ai` has minimal meta tags
- Only `<title>LiberClaw</title>` — no description
- Impact: Poor app SEO (though app pages often don't need it)

### 20. Font loading — 4 external font requests
- Google Fonts: Inter + JetBrains Mono + 2x Material Icons
- Uses `preconnect` (good) but no `font-display: swap` visible in HTML
- Impact: Potential FOIT (flash of invisible text)

---

## ✅ WORKING CORRECTLY

- SSL: Valid Let's Encrypt certificate
- Server: Caddy (good choice, auto-HTTPS)
- HTML lang attribute: `lang="en"` ✅
- Single H1 per page ✅
- External links all resolve (aleph.cloud, libertai.io, Discord, GitHub) ✅
- 404 page returns proper 404 status code ✅
- Astro framework — good for static sites ✅
- App subdomain loads (Expo/React Native Web) ✅
- Dark theme consistent ✅

---

## BROKEN LINKS SUMMARY

| URL | Status | Notes |
|-----|--------|-------|
| /robots.txt | 404 | Missing |
| /sitemap.xml | 404 | Missing |
| /pricing | 404 | Page doesn't exist |
| /docs | 404 | Page doesn't exist |
| /terms | 404 | Page doesn't exist |
| /privacy | 404 | Page doesn't exist |
| /blog | 404 | Page doesn't exist |
| api.liberclaw.ai (root) | 404 | No health/docs endpoint |
| All internal nav links | ✅ | Working |
| All external links | ✅ | Working |
