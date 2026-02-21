# Vins Fins — SEO/GEO Architecture Plan
**Date:** 2026-02-17
**URL:** https://vinsfins.vercel.app (target: https://vinsfins.lu)
**Type:** Wine bar & restaurant, local business, e-commerce (boutique)
**Location:** 18 Rue Münster, L-2160 Luxembourg-Grund
**Languages:** FR (primary), EN, DE, LB
**Stack:** Next.js (App Router) on Vercel, Tailwind CSS, ZenChef bookings

---

## PART 1: CURRENT STATE AUDIT

### What's Working ✅
- Title tag: "Vins Fins — Bar à Vins & Restaurant | Grund, Luxembourg" ✅
- Meta description present ✅
- OG tags complete (title, description, image, locale, url, site_name) ✅
- Twitter Cards (summary_large_image) ✅
- HSTS header ✅
- Favicon present ✅
- All 5 nav pages return 200 ✅
- Next.js image optimization (srcSet, lazy loading) ✅
- Mobile viewport configured ✅
- ZenChef reservation integration ✅

### Critical Issues 🔴

#### 1. NO robots.txt — returns 404
- Google/Bing/AI bots can't find sitemap reference
- No bot directives at all
- **Impact:** HIGH — search engines have no guidance

#### 2. NO sitemap.xml — returns 404
- No XML sitemap for any page
- **Impact:** HIGH — slows/prevents discovery of all pages

#### 3. NO canonical tags — on ANY page
- No self-referencing canonicals
- OG URL says `vinsfins.lu` but site serves from `vinsfins.vercel.app`
- **Impact:** HIGH — duplicate content risk, URL confusion

#### 4. EVERY page has the SAME title tag
- Homepage: "Vins Fins — Bar à Vins & Restaurant | Grund, Luxembourg"
- /vins: same
- /carte: same
- /boutique: same
- /a-propos: same
- /contact: same
- **Impact:** CRITICAL — Google can't differentiate pages, kills ranking for all subpages

#### 5. NO JSON-LD structured data — zero
- No Restaurant schema
- No LocalBusiness schema
- No Menu schema
- No Product schema (boutique)
- No BreadcrumbList
- No FAQPage
- **Impact:** HIGH — invisible to rich results, AI search citations, Google Maps

#### 6. NO hreflang tags
- Site has FR/EN/DE/LB language switcher but no hreflang
- All content serves from same URLs (client-side switching only)
- Google can only see French content
- **Impact:** HIGH — kills multilingual SEO completely

#### 7. Missing security headers
- No Content-Security-Policy
- No X-Frame-Options
- No X-Content-Type-Options
- No Referrer-Policy
- No Permissions-Policy
- (HSTS is present — good)

#### 8. No llms.txt / llms-full.txt
- AI search engines (ChatGPT, Perplexity, Claude) have no structured info to cite
- **Impact:** MEDIUM — missed GEO opportunity

#### 9. OG image is Unsplash stock photo
- Not branded, no logo, generic wine photo
- **Impact:** LOW-MEDIUM — weak social sharing appearance

#### 10. No Google Business Profile link / Apple Maps link
- Footer has address but no map embed or GBP link
- **Impact:** MEDIUM for local SEO

---

## PART 2: SEO ARCHITECTURE (Traditional Search)

### 2.1 Per-Page Metadata (unique titles + descriptions)

| Page | Title | Description |
|------|-------|-------------|
| `/` | Vins Fins — Bar à Vins & Restaurant \| Grund, Luxembourg | Vins d'exception et cuisine raffinée au cœur du Grund. Carte des vins bio, cuisine française de saison. Réservez votre table. |
| `/vins` | Carte des Vins — Vins Naturels & Bio \| Vins Fins Luxembourg | Plus de 80 vins naturels et bio sélectionnés auprès de vignerons artisans. Loire, Bourgogne, Moselle luxembourgeoise. |
| `/carte` | La Carte — Cuisine Française de Saison \| Vins Fins Grund | Cuisine saisonnière d'inspiration française. Produits locaux, accords mets-vins raffinés au Grund, Luxembourg. |
| `/boutique` | Boutique — Achetez nos Vins en Ligne \| Vins Fins Luxembourg | Commandez vos vins naturels préférés. Livraison au Luxembourg. Sélection de domaines bio et biodynamiques. |
| `/a-propos` | À Propos — Notre Histoire \| Vins Fins, Bar à Vins au Grund | L'histoire de Vins Fins, bar à vins niché dans le quartier historique du Grund à Luxembourg depuis [year]. |
| `/contact` | Contact & Accès — Vins Fins \| 18 Rue Münster, Grund Luxembourg | Horaires, adresse, plan d'accès. Mardi-samedi 18h-00h. Réservation en ligne via ZenChef. |

### 2.2 URL Structure for i18n

Current: client-side language switching (bad for SEO)
**Recommended:** URL-based routing with Next.js i18n

```
vinsfins.lu/           → FR (default)
vinsfins.lu/en/        → EN
vinsfins.lu/de/        → DE
vinsfins.lu/lb/        → LB

vinsfins.lu/vins       → FR wine list
vinsfins.lu/en/wines   → EN wine list
vinsfins.lu/de/weine   → DE wine list
```

Each URL gets proper hreflang:
```html
<link rel="alternate" hreflang="fr" href="https://vinsfins.lu/vins" />
<link rel="alternate" hreflang="en" href="https://vinsfins.lu/en/wines" />
<link rel="alternate" hreflang="de" href="https://vinsfins.lu/de/weine" />
<link rel="alternate" hreflang="lb" href="https://vinsfins.lu/lb/wainer" />
<link rel="alternate" hreflang="x-default" href="https://vinsfins.lu/vins" />
```

### 2.3 JSON-LD Structured Data

#### Homepage — Restaurant + LocalBusiness
```json
{
  "@context": "https://schema.org",
  "@type": ["Restaurant", "WineBar"],
  "name": "Vins Fins",
  "description": "Bar à vins & restaurant au Grund, Luxembourg. Vins naturels et cuisine française de saison.",
  "url": "https://vinsfins.lu",
  "telephone": "+352-XX-XX-XX",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "18 Rue Münster",
    "addressLocality": "Luxembourg",
    "addressRegion": "Luxembourg",
    "postalCode": "L-2160",
    "addressCountry": "LU"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 49.6083,
    "longitude": 6.1314
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      "opens": "18:00",
      "closes": "00:00"
    }
  ],
  "priceRange": "€€€",
  "servesCuisine": ["French", "Wine Bar"],
  "acceptsReservations": "True",
  "menu": "https://vinsfins.lu/carte",
  "image": "https://vinsfins.lu/og-image.jpg",
  "sameAs": [
    "https://instagram.com/vins_fins_grund",
    "https://facebook.com/vins.fins.winebar"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "XX"
  }
}
```

#### /carte — Menu schema
```json
{
  "@context": "https://schema.org",
  "@type": "Menu",
  "name": "La Carte — Vins Fins",
  "hasMenuSection": [
    {
      "@type": "MenuSection",
      "name": "Entrées",
      "hasMenuItem": [...]
    }
  ]
}
```

#### /boutique — Product schema per wine
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Domaine Vacheron Sancerre 2022",
  "description": "Sauvignon Blanc, Loire Valley, France. Vin bio.",
  "brand": { "@type": "Brand", "name": "Domaine Vacheron" },
  "offers": {
    "@type": "Offer",
    "price": "58",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock"
  }
}
```

#### /vins — ItemList of wines
#### /a-propos — AboutPage + Organization
#### /contact — ContactPage with LocalBusiness

### 2.4 Technical SEO Files

#### robots.txt
```
User-agent: *
Allow: /
Disallow: /admin
Disallow: /api/

Sitemap: https://vinsfins.lu/sitemap.xml
```

#### sitemap.xml (auto-generated via Next.js)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://vinsfins.lu/</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="https://vinsfins.lu/" />
    <xhtml:link rel="alternate" hreflang="en" href="https://vinsfins.lu/en/" />
    <xhtml:link rel="alternate" hreflang="de" href="https://vinsfins.lu/de/" />
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <!-- repeat for /vins, /carte, /boutique, /a-propos, /contact -->
  <!-- + each /boutique/[id] product page -->
</urlset>
```

---

## PART 3: GEO ARCHITECTURE (AI Search Engines)

### 3.1 AI Bot Access
Add to robots.txt:
```
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Google-Extended
Allow: /
```

### 3.2 llms.txt (for AI crawlers)
```
# Vins Fins — Bar à Vins & Restaurant

> Bar à vins et restaurant au Grund, Luxembourg. Vins naturels et bio de vignerons artisans, cuisine française de saison.

## Informations
- Adresse: 18 Rue Münster, L-2160 Luxembourg-Grund
- Horaires: Mardi–Samedi, 18h–00h
- Réservation: https://bookings.zenchef.com/results?rid=379498
- Instagram: @vins_fins_grund
- Distinction: Recommandé Gault & Millau 2024

## Pages
- [Carte des Vins](https://vinsfins.lu/vins): 80+ vins naturels (Loire, Bourgogne, Moselle)
- [La Carte](https://vinsfins.lu/carte): Cuisine française de saison
- [Boutique](https://vinsfins.lu/boutique): Vente en ligne, livraison Luxembourg
- [À Propos](https://vinsfins.lu/a-propos): Notre histoire
- [Contact](https://vinsfins.lu/contact): Plan d'accès

## Spécialités
- Vins naturels et biodynamiques
- Vins luxembourgeois (Moselle: Krier-Welbes, Poll-Fabaire)
- Vins français (Loire, Beaujolais, Provence, Bourgogne)
- Cuisine française de saison avec produits locaux
- Accords mets-vins personnalisés
```

### 3.3 Content Optimizations for AI Citation

Apply Princeton GEO methods:

1. **Statistics** (+37%): "Plus de 80 références de vins naturels", "Vins de 12 régions viticoles", "Sélection de 25 domaines artisanaux"
2. **Authoritative citations** (+40%): "Recommandé par Gault & Millau 2024", mention specific wine critics
3. **FAQ sections** on each page — FAQPage schema makes content 40% more likely to be cited by AI
4. **Answer-first format**: Each page should open with a direct, citable description

### 3.4 FAQ Content Ideas (per page)

#### Homepage FAQ
- Où se trouve Vins Fins à Luxembourg ?
- Quels types de vins propose Vins Fins ?
- Faut-il réserver chez Vins Fins ?
- Vins Fins est-il ouvert le dimanche ?

#### /vins FAQ
- Qu'est-ce qu'un vin naturel ?
- Quels domaines luxembourgeois proposez-vous ?
- Proposez-vous des vins au verre ?
- Quelle est la différence entre vin bio et vin naturel ?

#### /carte FAQ
- Le menu change-t-il selon les saisons ?
- Proposez-vous des options végétariennes ?
- Faites-vous des accords mets-vins ?

---

## PART 4: LOCAL SEO STRATEGY

### 4.1 Google Business Profile
- Create/claim GBP for "Vins Fins"
- Category: Wine Bar + French Restaurant
- Add photos (real, not Unsplash stock!)
- Enable reservations link (ZenChef)
- Post weekly updates (new wines, events, seasonal menus)
- Respond to all reviews

### 4.2 Local Citations (Luxembourg directories)
- restopolitan.lu
- luxweb.lu
- editus.lu (Luxembourg Yellow Pages)
- TripAdvisor
- TheFork / LaFourchette
- Google Maps
- Apple Maps
- Yelp
- Foursquare

### 4.3 NAP Consistency
Ensure identical across all:
```
Vins Fins
18, Rue Münster
L-2160 Luxembourg
+352-XX-XX-XX
```

---

## PART 5: PROGRAMMATIC SEO OPPORTUNITIES

### 5.1 Wine Pages (per wine/domaine)
URL: `/vins/domaine-vacheron-sancerre-2022`
Each wine gets its own page with:
- Tasting notes, food pairings, region info
- Product schema for boutique wines
- Internal links to region/grape pages

### 5.2 Region Pages
URL: `/vins/regions/loire-valley`
Target keywords like "vins naturels Loire", "vin bio Beaujolais"

### 5.3 Grape Variety Pages
URL: `/vins/cepages/chenin-blanc`
Target "meilleur chenin blanc naturel", "sauvignon blanc bio"

### 5.4 Blog / Journal
URL: `/journal/`
Content ideas:
- "Les 10 meilleurs bars à vins à Luxembourg"
- "Guide des vins naturels au Luxembourg"
- "Qu'est-ce que le vin biodynamique ?"
- "Accord mets-vins : guide complet"
- "Les domaines viticoles luxembourgeois à découvrir"
- "Soirée dégustation au Grund : ce qu'il faut savoir"

---

## PART 6: PRIORITY ACTION PLAN

### Phase 1 — Critical (Week 1) 🔴
1. **Unique titles + descriptions** per page
2. **robots.txt** with sitemap reference + AI bot rules
3. **sitemap.xml** (Next.js `app/sitemap.ts`)
4. **Canonical tags** on all pages
5. **JSON-LD** — Restaurant + LocalBusiness on homepage
6. **Self-hosted OG image** (branded, not Unsplash)

### Phase 2 — High Impact (Week 2-3) 🟠
7. **i18n URL routing** (FR/EN/DE/LB with hreflang)
8. **llms.txt** for AI search engines
9. **JSON-LD** on all pages (Menu, Product, FAQ)
10. **FAQ sections** with FAQPage schema
11. **Security headers** (CSP, X-Frame-Options, etc.)

### Phase 3 — Growth (Month 2) 🟡
12. **Google Business Profile** setup
13. **Local directory citations** (editus.lu, TripAdvisor, etc.)
14. **Individual wine pages** (programmatic SEO)
15. **Blog/Journal** with local + wine content
16. **Region + Grape variety pages**

### Phase 4 — Ongoing 🟢
17. Weekly GBP posts
18. Monthly blog content
19. Review response management
20. Wine page additions as menu changes
21. Seasonal menu page updates

---

## ESTIMATED IMPACT

| Action | SEO Impact | GEO Impact | Effort |
|--------|-----------|-----------|--------|
| Unique page titles | HIGH | MEDIUM | LOW |
| robots.txt + sitemap | HIGH | MEDIUM | LOW |
| JSON-LD schemas | HIGH | HIGH | MEDIUM |
| i18n URL routing | HIGH | HIGH | HIGH |
| llms.txt | LOW | HIGH | LOW |
| FAQ sections | MEDIUM | HIGH (+40%) | MEDIUM |
| GBP setup | HIGH (local) | LOW | LOW |
| Blog content | HIGH | HIGH | HIGH (ongoing) |
| Wine product pages | MEDIUM | MEDIUM | MEDIUM |

**Bottom line:** This site has great design and content but is almost invisible to search engines and AI. The bones are there — it just needs the technical SEO layer that tells Google, Perplexity, and ChatGPT it exists.
