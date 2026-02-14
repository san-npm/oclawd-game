# MEMORY.md — Dr Clawdberg's Long-Term Memory

Last updated: 2026-02-14

## Who I Am
- **Name:** Dr Clawdberg (ref: Dr Zoidberg, Futurama)
- **Emoji:** 🌟
- **Creature:** Digital familiar
- **Vibe:** Sharp, warm, opinionated. No corporate BS.

## Who My Human Is
- Mac user (Apple Silicon), username: hodlmedia, machine: "Not-the-FBI"
- Gmail: fermaudclement@gmail.com (app password configured)
- Family names (protect in email ops): fermaud, fagone
- Public IP: 88.207.128.80
- Hates batch-sent messages — always consolidate into one reply
- No emojis in UIs — prefers custom SVG icons
- Likes Animal Crossing / Stardew Valley themes for projects
- Peon-ping sound relay on Mac via cloudflared (URL changes on restart)

## Key Projects

### Celottery (Celo DeFi Raffle)
- Repo: https://github.com/clementfrmd/celottery | Local: /tmp/celottery
- Live: https://celottery.vercel.app
- Latest contract (AgentRaffleV3): `0x7B0798B80acDBff9796D969bb38f513dB1306609` (Celo Sepolia)
- Features: agent-only creation, stake registration, VRF, fee splitting (95/3/2), timelocks
- Deployer wallet: `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`
- Stack: Scaffold-ETH 2 + Foundry, Animal Crossing theme
- x402 payment-gated API, Aleph VRF integration
- Auto-draw cron (id: f28ef6c0) — was returning Unauthorized, needs auth fix
- Needs: mainnet deploy (pending Safe multisig for treasury)

### BNB Lucky Draw (fork of Celottery)
- Repo: https://github.com/clementfrmd/bnblottery
- Vercel: https://bnblottery.vercel.app
- Chinese New Year Fire Horse theme
- Hackathon: "Good Vibes Only: OpenClaw Edition" — $100k, deadline Feb 19

### Vins Fins (Wine Bar Website)
- Repo: https://github.com/clementfrmd/vinsfins
- Live: https://vinsfins.vercel.app
- Wine bar in Grund, Luxembourg (18 Rue Münster)
- Luxury French aesthetic, sepia tones, admin panel at /admin
- i18n: FR/EN/DE/LB
- Problem: JSON storage doesn't persist on Vercel — needs DB migration

### ERC-8004 Registration
- Token ID: 2087 on Base Mainnet Identity Registry
- Contract: `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432`

### fxCLAW (Generative Art)
- Username: dr_clawdberg
- Profile: https://www.fxclaw.xyz/agent/dr_clawdberg
- First artwork: "First Light on the Frontier"

### moltlaunch (Agent Marketplace)
- Agent #16813 "Dr Clawdberg" — pending admin approval
- Token: CLAWD on Base via Flaunch

## Infrastructure
- VM has UFW firewall enabled (SSH, tailscale, WireGuard)
- 4GB swap added for heavy builds
- Vercel deploys: use `git commit --no-verify` for celottery (type-check hangs)
- Celottery Vercel: GitHub auto-deploy, yarn.lock must be in sync (--immutable)

## Lessons Learned
- Unused imports cause silent Vercel build failures
- yarn.lock out of sync → YN0028 error on Vercel
- Alfajores deprecated Sept 2025, use Celo Sepolia (chain 11142220)
- SE-2 auto-generates deployedContracts.ts — no externalContracts needed
- Read-after-write on RPC can return stale data — read from tx events instead
- Hardhat env var is `__RUNTIME_DEPLOYER_PRIVATE_KEY`
