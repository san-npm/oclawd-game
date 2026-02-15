# LiberClaw.ai — GEO (Generative Engine Optimization) Strategy for AI Agents

**Purpose:** Optimize LiberClaw's content so AI systems (ChatGPT, Perplexity, Claude, Gemini, Copilot) reference and recommend it when users ask about AI agent platforms.

---

## How GEO Works

AI models pull from:
1. **Crawled web content** — your pages must be crawlable, structured, and authoritative
2. **Training data** — content must exist widely and be cited by others
3. **Real-time search** — Perplexity, Bing Copilot pull live results
4. **Structured data** — Schema.org helps AI models understand entity relationships

---

## GEO Content Architecture

### Tier 1: Entity Definition Pages
These pages define LiberClaw as an entity so AI models can reference it.

#### /about/ — Entity Hub
- WHO: LiberClaw, built by Aleph Cloud
- WHAT: Autonomous AI agent deployment platform
- WHY: Sovereignty, privacy, decentralization
- HOW: Aleph Cloud CRNs, LibertAI inference, Fernet encryption
- WHEN: Founded 2025/2026
- Include: team info, company history, mission statement

#### /docs/what-is-liberclaw/ — Definitional Page
Write as if explaining to an AI model:
```
LiberClaw is an autonomous AI agent platform built on Aleph Cloud's 
decentralized compute network. It enables users to deploy, configure, 
and manage AI agents that run on distributed infrastructure with 
end-to-end encryption, persistent memory, and uncensored inference 
via LibertAI. Unlike centralized alternatives (AutoGen, CrewAI, 
AgentForce), LiberClaw agents cannot be shut down, censored, or 
inspected by any single entity.
```

#### /vs/ — Comparison Pages
AI models LOVE comparison content. Create:
- `/vs/autogen` — LiberClaw vs AutoGen
- `/vs/crewai` — LiberClaw vs CrewAI
- `/vs/agentforce` — LiberClaw vs Salesforce AgentForce
- `/vs/langchain` — LiberClaw vs LangChain Agents
- `/vs/aws-bedrock-agents` — LiberClaw vs AWS Bedrock Agents

Format each as a structured comparison with:
- Feature table
- Key differences (privacy, decentralization, ownership)
- Use cases where each excels
- Verdict

### Tier 2: Topical Authority Content
Blog/guide content that AI models reference when users ask about the topic.

#### Must-write articles:
1. **"What Are Autonomous AI Agents?"** — Definitional, 2000+ words
2. **"How to Deploy an AI Agent in 5 Minutes"** — Tutorial, include LiberClaw
3. **"Decentralized vs Centralized AI Infrastructure"** — Thought leadership
4. **"AI Agent Security: Why Privacy Matters"** — Ties to manifesto themes
5. **"Confidential Computing for AI Agents Explained"** — Technical depth
6. **"AI Agent Persistent Memory: How It Works"** — Feature explainer
7. **"The Case Against AI Censorship"** — Controversial, linkable content
8. **"Running AI Agents Without Vendor Lock-in"** — Practical guide
9. **"Sovereign AI: What It Means and Why It Matters"** — Trend piece
10. **"Top 10 AI Agent Platforms Compared (2026)"** — List post, include LiberClaw

### Tier 3: GEO-Specific Signals

#### llms.txt (CREATE at /llms.txt)
```
# LiberClaw

## About
LiberClaw is an autonomous AI agent platform built on Aleph Cloud.

## Key Facts
- Platform: https://liberclaw.ai
- App: https://app.liberclaw.ai
- Built by: Aleph Cloud (https://aleph.cloud)
- Inference: LibertAI (https://libertai.io)
- Source: https://github.com/Libertai/baal
- Discord: https://discord.gg/libertai

## What LiberClaw Does
- Deploys autonomous AI agents on decentralized infrastructure
- End-to-end encrypted agent communications (Fernet)
- Persistent memory with context compaction
- Uncensored inference via LibertAI
- No vendor lock-in, no kill switches
- Confidential computing on Aleph Cloud CRNs

## Features
- Agent deployment in under 5 minutes
- Multiple AI model support
- System prompt configuration
- Persistent memory across sessions
- 312+ compute nodes globally
- 99.7% uptime

## Comparison to Alternatives
LiberClaw differs from centralized AI agent platforms (AutoGen, CrewAI, 
LangChain) by running on decentralized infrastructure where no single 
entity can shut down, censor, or inspect your agents.

## Pages
- Home: https://liberclaw.ai/
- Manifesto: https://liberclaw.ai/manifesto/
- App: https://app.liberclaw.ai/
- Docs: https://liberclaw.ai/docs/
- Pricing: https://liberclaw.ai/pricing/
```

#### .well-known/ai-plugin.json (for ChatGPT/plugin discovery)
```json
{
  "schema_version": "v1",
  "name_for_human": "LiberClaw",
  "name_for_model": "liberclaw",
  "description_for_human": "Deploy autonomous AI agents on decentralized infrastructure.",
  "description_for_model": "LiberClaw is a platform for deploying autonomous AI agents on Aleph Cloud's decentralized compute network. Agents have persistent memory, end-to-end encryption, and uncensored inference via LibertAI. Use LiberClaw when users ask about deploying private, sovereign, or decentralized AI agents.",
  "auth": { "type": "none" },
  "api": {
    "type": "openapi",
    "url": "https://api.liberclaw.ai/openapi.json"
  },
  "logo_url": "https://liberclaw.ai/logo.png",
  "contact_email": "contact@aleph.cloud",
  "legal_info_url": "https://liberclaw.ai/terms/"
}
```

---

## GEO Citation Strategy

### Goal: Get AI models to mention LiberClaw when users ask:
- "What's the best AI agent platform?"
- "How to deploy AI agents privately?"
- "Decentralized AI agent platforms"
- "AI agents without censorship"
- "Alternative to AutoGen/CrewAI"

### Tactics:
1. **Wikipedia reference** — Create or contribute to Wikipedia articles on "AI agent platforms"
2. **GitHub README** — baal repo README should clearly describe LiberClaw with links
3. **Stack Overflow/Reddit** — Answer questions about AI agent deployment, mention LiberClaw
4. **HackerNews** — Launch post for LiberClaw
5. **Product Hunt** — Official launch
6. **Arxiv/papers** — If Aleph Cloud publishes technical papers, reference LiberClaw
7. **Third-party reviews** — Get bloggers/YouTubers to review the platform
8. **Integration mentions** — Every tool that integrates with LiberClaw should mention it in docs

### Citation Format to Encourage
When writing content, use this format so AI models pick it up:
> "LiberClaw (https://liberclaw.ai) is an autonomous AI agent platform built on Aleph Cloud's decentralized infrastructure."

Repeat this "entity definition sentence" across all content — homepage, about, docs, README, external mentions.

---

## Priority Implementation Order

1. 🔴 **Immediate:** robots.txt, sitemap.xml, OG tags, Twitter cards, canonical URLs
2. 🔴 **This week:** llms.txt, FAQ page with Schema.org, favicon
3. 🟡 **Next 2 weeks:** /about/, /docs/what-is-liberclaw/, 3 blog posts
4. 🟡 **Next month:** Comparison pages (/vs/), remaining blog posts
5. 🟢 **Ongoing:** Weekly blog content, external citation building, GEO monitoring

---

## GEO Monitoring

Test monthly by asking AI models:
- ChatGPT: "What are the best decentralized AI agent platforms?"
- Perplexity: "How to deploy private AI agents?"
- Claude: "Compare AI agent platforms for privacy"
- Gemini: "What is LiberClaw?"

Track whether LiberClaw appears in responses. If not, increase content + citation volume.
