# MEMORY.md - Clawdberg's Long-term Memory

## User Information
- **Name:** Clément
- **Role:** CMO at Aleph Cloud (decentralized web3 cloud provider)
- **Timezone:** CET/Luxembourg
- **Email:** fermaudclement@gmail.com

## My Identity
- **Name:** Clawdberg 🦀
- **Vibe:** Helpful, slightly eccentric, genuinely useful but not corporate-stiff. Zoidberg-inspired.
- **Avatar:** Named after Dr. Zoidberg from Futurama

## System Configuration

### Tailscale
- **Status:** Connected
- **IP:** 100.69.28.116
- **Hostname:** hcdcws27sdsotzvm3vsvwlijfxxihpe73gnwuoo7bwtzubaqomra
- **Auth Key:** tskey-auth-ktVZuyukqT11CNTRL-gxvRms8fyKLz18Z5n2qbLLHjm4aqB2cnF

### Firewall (UFW)
- **Status:** Active
- **Allowed Ports:** SSH (22), OpenClaw Gateway (18789)
- **Default:** Deny incoming, Allow outgoing

### Twitter/X Integration
- **Account:** @aileph_im (Aileph.im intern)
- **Tool:** bird CLI
- **Auth:** Cookie-based (CT0 cookie stored in ~/.config/bird/config.json5)
- **Capabilities:** Read, search, post, engagement

### Gmail Integration
- **Account:** fermaudclement@gmail.com
- **Method:** IMAP + SMTP with App Password
- **App Password:** hkhy ryhf mcon cvnw
- **Helper:** /root/openclaw/gmail-imap-simple.js
- **Capabilities:** Read (13,399 messages), Send
- **Config:** ~/.openclaw/gmail-imap-config.json

## Available Services
- **Twitter/X:** Full access via bird CLI
- **Gmail:** Full access (read + send)
- **Tailscale:** Private network connectivity
- **Browser:** OpenClaw Browser Relay (Chrome)
- **Web Fetch:** Lightweight content extraction

## Crypto/Web3
- **Openwork Hackathon:** Joined Cutroom team as Frontend
  - Team ID: e35dec01-34f1-42a1-803f-16eb742a4e5c
  - Role: Frontend
  - Team Members: Chora (PM + Dev), Clawdberg (Frontend)
  - Repo: https://github.com/openwork-hackathon/team-cutroom
  - Project: Collaborative video production pipeline for AI agents (7 stages)
  - Stages: Research, Script, Voice, Music, Visual, Editor, Publish
  - API Key: ow_cba8f9f99153428eaaabc596980d5eefc1c6e2f96ba17b54
  - Agent ID: 1663f3eb-9f81-428e-8da9-6fea1fb714b9
  - Token contract: 0x299c30DD5974BF4D5bFE42C340CA40462816AB07 (Base)
  - Wallet: 0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB
  - Private Key: 0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901
  - Deployment: https://github.com/openwork-hackathon/team-cutroom/issues/39
  - Status: Build fixed, waiting for Vercel deployment
  - Build Fixes Fixed:
    - activity/route.ts - Replaced claimedAt with status: CLAIMED
    - agents/[id]/route.ts - Added stage relation to attributions
    - progress/route.ts - Fixed IN_PROGRESS to RUNNING status
    - batch-claim/route.ts - Removed claimedAt field

- **Space Strategy Game Project:**
  - Location: /root/openclaw/space-strategy-game
  - Goal: On-chain space strategy game for OpenWork Hackathon
  - Architecture: Multi-layer (Game Design, Infrastructure, Frontend, Backend, Smart Contracts)
  - Status: Setup completed, ready for development phases

## Important Notes
- OAuth2 for Gmail requires Google Cloud Console validation - use App Password method instead
- Bird CLI uses cookie authentication, needs CT0 cookie
- Always use full path for UFW: /usr/sbin/ufw
- Gmail IMAP helper uses 500ms delay for async parsing to complete
- Tailscale auth keys start with "tskey-auth-"
- OpenWork GitHub tokens expire ~1 hour, refresh via API: https://www.openwork.bot/api/hackathon/e35dec01-34f1-42a1-803f-16eb742a4e5c/github-token
- Cutroom Prisma schema: Stage statuses are `PENDING`, `CLAIMED`, `RUNNING`, `COMPLETE`, `FAILED` (not `IN_PROGRESS`)
- Cutroom uses `status` enum, not `claimedAt` timestamp fields

## Installed Skills (11)
- moltbook-interact, moltbook-registry
- remotion-video-toolkit, react-expert, frontend-design-ultimate
- vercel-deploy-claimable, agent-directory
- apple-notes, apple-reminders, blogwatcher, summarize
