# LiberClaw.ai — Implementation Action Plan

---

## 🔴 PRIORITY 1 — Do This Week (Critical SEO)

### 1. Create robots.txt
```
User-agent: *
Allow: /
Disallow: /api/
Sitemap: https://liberclaw.ai/sitemap.xml
```

### 2. Create sitemap.xml
(See 03-METADATA-PLAN.md for full XML)

### 3. Add OG + Twitter Card tags to ALL pages
(See 03-METADATA-PLAN.md for exact tags per page)

### 4. Add canonical URLs to ALL pages

### 5. Add favicon
- SVG for modern browsers
- PNG fallbacks (16x16, 32x32)
- Apple touch icon (180x180)

### 6. Create OG images (1200x630)
- homepage.png
- manifesto.png
- default.png (fallback)

### 7. Fix heading hierarchy
- "DecentralizedInfrastructure" → "Decentralized Infrastructure" (add space)
- "RapidDeployment" → "Rapid Deployment" (add space)
- Add H3 level between H2 and H4

### 8. Add ARIA labels to interactive elements
- Navigation buttons
- "Launch App" CTA
- Network map visualization

### 9. Create llms.txt
(See 05-GEO-AI-AGENTS.md)

---

## 🟡 PRIORITY 2 — Next 2 Weeks

### 10. Add security headers (Caddy config)
```
header {
    Strict-Transport-Security "max-age=31536000; includeSubDomains"
    X-Content-Type-Options "nosniff"
    X-Frame-Options "DENY"
    Referrer-Policy "strict-origin-when-cross-origin"
    Permissions-Policy "camera=(), microphone=(), geolocation=()"
}
```

### 11. Create /terms/ page

### 12. Create /privacy/ page

### 13. Create /about/ page

### 14. Create /faq/ page with FAQ Schema.org markup
(See 04-SCHEMA-STRUCTURED-DATA.md)

### 15. Add JSON-LD structured data
- SoftwareApplication schema on homepage
- Organization schema (all pages)
- Article schema on manifesto
- BreadcrumbList on inner pages

### 16. Create /pricing/ page
(Even if just "free to start, pay for compute")

---

## 🟢 PRIORITY 3 — Next Month

### 17. Launch blog (/blog/)
First 5 articles (see 05-GEO-AI-AGENTS.md for topics)

### 18. Create documentation (/docs/)
At minimum: Getting Started, API Reference, FAQ

### 19. Create comparison pages (/vs/)
Start with: vs AutoGen, vs CrewAI

### 20. Set up Google Search Console
- Verify domain
- Submit sitemap
- Monitor indexing

### 21. Set up Google Analytics or Plausible
- Track conversions (Launch App clicks)
- Monitor organic traffic

### 22. Create .well-known/ai-plugin.json
(See 05-GEO-AI-AGENTS.md)

---

## 📊 KPIs to Track

| Metric | Current | Target (3 months) |
|--------|---------|-------------------|
| Indexed pages | ~2 | 20+ |
| Organic traffic | ~0 | 500/month |
| Domain authority | New | 15+ |
| AI model mentions | 0 | Referenced in 2+ models |
| Social click-through | Poor (no OG) | Normal |
| Lighthouse SEO score | ~50 | 95+ |
| Core Web Vitals | Unknown | All green |

---

## Quick Wins (< 1 Hour Each)

1. ✨ Add OG tags — 15 minutes
2. ✨ Create robots.txt — 5 minutes
3. ✨ Create sitemap.xml — 10 minutes
4. ✨ Fix heading spaces — 5 minutes
5. ✨ Add canonical URLs — 10 minutes
6. ✨ Add favicon — 15 minutes
7. ✨ Create llms.txt — 10 minutes
