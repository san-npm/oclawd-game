# LiberClaw.ai — Schema.org Structured Data (JSON-LD)

---

## Homepage (/)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "LiberClaw",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "url": "https://liberclaw.ai",
  "description": "Deploy sovereign AI agents on Aleph Cloud. Private execution, uncensored inference via LibertAI, persistent memory.",
  "provider": {
    "@type": "Organization",
    "name": "Aleph Cloud",
    "url": "https://aleph.cloud"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": "Free tier available"
  },
  "featureList": [
    "Autonomous AI Agents",
    "Decentralized Infrastructure",
    "End-to-End Encryption",
    "Persistent Memory",
    "Confidential Computing",
    "Uncensored Inference",
    "No Vendor Lock-in"
  ],
  "screenshot": "https://liberclaw.ai/og/homepage.png"
}
</script>
```

## Organization (all pages, in footer/head)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "LiberClaw",
  "alternateName": "Aleph Cloud LiberClaw",
  "url": "https://liberclaw.ai",
  "logo": "https://liberclaw.ai/logo.png",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Aleph Cloud",
    "url": "https://aleph.cloud"
  },
  "sameAs": [
    "https://discord.gg/libertai",
    "https://github.com/Libertai/baal",
    "https://x.com/aileph_im"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "url": "https://discord.gg/libertai"
  }
}
</script>
```

## Manifesto (/manifesto/)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The LiberClaw Manifesto",
  "description": "Why AI agents should serve their operators, not surveil them.",
  "url": "https://liberclaw.ai/manifesto/",
  "datePublished": "2026-02-01",
  "author": {
    "@type": "Organization",
    "name": "Aleph Cloud"
  },
  "publisher": {
    "@type": "Organization",
    "name": "LiberClaw",
    "url": "https://liberclaw.ai"
  },
  "mainEntityOfPage": "https://liberclaw.ai/manifesto/",
  "articleSection": "Philosophy",
  "keywords": ["sovereign AI", "decentralized AI agents", "AI autonomy", "privacy by design"]
}
</script>
```

## FAQ Page (/faq/) — TO CREATE

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is LiberClaw?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LiberClaw is an autonomous AI agent platform that runs on Aleph Cloud's decentralized infrastructure. It provides private execution, uncensored inference via LibertAI, and persistent memory for your agents."
      }
    },
    {
      "@type": "Question",
      "name": "How is LiberClaw different from other AI agent platforms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LiberClaw runs on decentralized infrastructure with no single point of failure. Your agents use end-to-end encryption, can't be shut down by a single entity, and you maintain full ownership. Unlike centralized platforms, there are no content filters or kill switches."
      }
    },
    {
      "@type": "Question",
      "name": "Is LiberClaw free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LiberClaw offers a free tier to get started. You pay for compute resources on Aleph Cloud as you scale. No subscriptions, no lock-in."
      }
    },
    {
      "@type": "Question",
      "name": "What AI models does LiberClaw support?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LiberClaw supports multiple AI models including those available through LibertAI's decentralized inference network. You can choose from various open-source models with uncensored inference capabilities."
      }
    },
    {
      "@type": "Question",
      "name": "How does LiberClaw handle data privacy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LiberClaw uses Fernet end-to-end encryption for all agent communications. Agents run on Aleph Cloud's confidential computing infrastructure with hardware-level encryption. Even node operators cannot see inside your agent's execution environment."
      }
    }
  ]
}
</script>
```

## Breadcrumbs (all inner pages)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://liberclaw.ai/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Manifesto",
      "item": "https://liberclaw.ai/manifesto/"
    }
  ]
}
</script>
```
