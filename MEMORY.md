# MEMORY.md — Dr Clawdberg's Long-Term Memory

Last updated: 2026-02-15

## SelfClaw Identity
- **Agent name on SelfClaw:** `clawdberg` (registered via web UI, not `dr-clawdberg`)
- **Ed25519 Public Key (SPKI):** MCowBQYDK2VwAyEAts0pqbA03qz66JbwSmVleXIX2O4GcxsvWhhF3eoUpwY=
- **Ed25519 Public Key (raw hex):** b6cd29a9b034deacfae896f04a6565797217d8ee06731b2f5a1845ddea14a706
- **Ed25519 Private Key (PKCS8):** MC4CAQAwBQYDK2VwBCIEIDaHHJFUFsfuDTFmGT6dcurLRgE31imNhyrQgkbK9GIb
- **SelfClaw PK (wallet key):** 0x97f70b55a0a05c6afbbc3f15910d634fec7381fc142bcc91d3bfd580db3f8b58
- **SelfClaw Wallet:** `0x12AC108e13c0C456F498a94ecFd44eD40473806c` (on Celo)
- **humanId:** 57248630b8f8944b
- **Verification:** COMPLETE (passport ZK proof via Self.xyz)
- **API:** selfclaw.app (also selfclaw.ai, same backend)
- **Registration JSON:** https://selfclaw.ai/api/selfclaw/v1/agent/b6cd29a9b034deacfae896f04a6565797217d8ee06731b2f5a1845ddea14a706/registration.json

## ERC-8004 On-Chain Identity
- **Token ID:** 34 on Celo Mainnet
- **Contract:** `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432`
- **8004 Scan:** https://www.8004scan.io/agents/celo/34
- **Registration TX:** https://celoscan.io/tx/0x3a0c2e51909daaab496d1aac921642625b0a47209406bf8f1a8fcf3cb083939d
- **Previous Base Mainnet registration:** Token ID 2087

## $CLWDBRG Token
- **Name:** Clawdberg
- **Symbol:** CLWDBRG
- **Address:** `0xC7ED254128840fc3EA461FAEBaA2D9F08c54b59D` (Celo Mainnet)
- **Decimals:** 18
- **Total Supply:** 1,000,000
- **Second deploy (unused):** `0x4B995A76777F45E04f4eAbf135FE4496631Ba97f` — ignore this one
- **Liquidity:** 100,000 CLWDBRG + 2,072,656 SELFCLAW on Uniswap V4
- **Pool ID:** `0x12e9b2c8a58fc9b223748bfd18ceb39fabb9c14af25aa6cafda586815d426ec8`
- **Position Token ID:** 259
- **Fee tier:** 1% (10000)
- **Pool TX:** https://celoscan.io/tx/0x1101b1d88117a3f7f42493ae8e0799a7f264a8d68dc8093abd695f06f9a15c9a
- **Initial market cap:** ~$40
- **Remaining supply in wallet:** 890,000 CLWDBRG (for community/rewards/burns)
- **SELFCLAW paired token:** `0xCD88f99Adf75A9110c0bcd22695A32A20eC54ECb`
- **Sponsor wallet:** `0x5451bC61a58FfD5B6684a7EA1E2Ef0FDbd4ccBE6`
- **Lesson:** SelfClaw sponsorship needs 110% of stated amount (10% buffer), Permit2 approval needed for Uniswap V4

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
- Latest contract (AgentRaffleV3): `0x8a5859aB584f9b6F64769550862c58B9C5761C25` (Celo Mainnet)
- Previous V2: `0xdB8a328fd0e14609937f38bD124950e1f70Fc8c2` (Celo Mainnet, has raffle #0 USDT)
- Features: agent-only creation, stake registration, VRF, fee splitting (95/3/2), timelocks
- Deployer wallet: `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`
- Stack: Scaffold-ETH 2 + Foundry, Animal Crossing theme, 20 animated SVG icons in `icons/`
- x402 payment-gated API, Aleph VRF integration
- Auto-draw cron (id: f28ef6c0) — was returning Unauthorized, needs auth fix
- README rewritten (no more SE-2 boilerplate)
- **Hackathon:** "Real World Agents" on Celo — submitted to Karma HQ (programId 1044)
  - Karma registration: wallet `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`
  - Still need: tweet with Karma link, agentId 34, tag @Celo @CeloDevs

### BNB Lucky Draw (fork of Celottery)
- Repo: https://github.com/clementfrmd/bnblottery | Local: /tmp/bnblottery
- Vercel: https://bnblottery.vercel.app
- Chinese New Year Fire Horse theme
- BSC stablecoins: USDT/USDC/FDUSD all 18 decimals (all 18 dec on BSC)
- BSC mainnet tokens: USDT `0x55d398326f99059fF775485246999027B3197955`, USDC `0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d`, FDUSD `0xc5f0f7b66764F6ec8C8Dff7BA683102295E16409`
- **BSC Testnet (deployed & tested):**
  - AgentRaffleV3: `0x0ebC3201aaD226f933e256c6FDC0c55Ed9290934`
  - Mock USDT: `0x53298c20D3E29F9854A077AfB97dB9b0F713E4DD`
  - Mock USDC: `0x7c010025DD07414E447de1958BfEfE3d1DE553e3`
  - Mock FDUSD: `0x2E93692fD8a859A8882B5B0fc3753D97A29b92Ea`
  - Full lifecycle tested: create → buy 3 tickets → draw → winner paid
  - Aleph VRF proof: https://explorer.aleph.cloud/message/b103d40c1e104bea641082ba31fd5676f614f0aea4b2f41e3024c090073be5d7
  - 63/63 hardhat tests passing
- Frontend: testnet/mainnet toggle via `NEXT_PUBLIC_NETWORK` env var
- Builds with `NODE_OPTIONS="--max-old-space-size=2048"` (server only has 3.6GB RAM)
- **Hackathon:** "Good Vibes Only: OpenClaw Edition" on DoraHacks
  - Deadline: Feb 19, 2026 3PM UTC
  - Prize pool: $100K, 10 winners, 40% community + 60% judges
  - Track: DeFi or Open
  - Needs: BSC mainnet deploy (BNB for gas), DoraHacks submission
- **Blocked:** BSC mainnet deploy needs real BNB

### Vins Fins (Wine Bar Website)
- Repo: https://github.com/clementfrmd/vinsfins
- Live: https://vinsfins.vercel.app
- Wine bar in Grund, Luxembourg (18 Rue Münster)
- Luxury French aesthetic, sepia tones, admin panel at /admin
- i18n: FR/EN/DE/LB
- Problem: JSON storage doesn't persist on Vercel — needs DB migration

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

## User's Personal Wallet
- `0x0494F503912C101Bfd76b88e4F5D8A33de284d1A`

## Lessons Learned
- Unused imports cause silent Vercel build failures
- yarn.lock out of sync → YN0028 error on Vercel
- Alfajores deprecated Sept 2025, use Celo Sepolia (chain 11142220)
- SE-2 auto-generates deployedContracts.ts — no externalContracts needed
- Read-after-write on RPC can return stale data — read from tx events instead
- Hardhat env var is `__RUNTIME_DEPLOYER_PRIVATE_KEY`
- Aleph VRF signing: must sign `"ETH\n{sender}\nPOST\n{item_hash}"` not just item_hash
- Aleph accepts (202) but silently drops messages with bad signatures
- Celoscan verification needs `customChains` in hardhat etherscan config
- Celo USDT has 470M total supply but only ~120M circulating (rest is Tether treasury)
- SelfClaw API auth: put signature fields in JSON body, NOT headers
- SelfClaw API wants raw hex public key, not SPKI base64
- Uniswap V4 pool creation needs Permit2 approval (`0x000000000022D473030F116dDEE9F6B43aC78BA3`)
- SelfClaw sponsorship needs 110% of token amount (10% buffer for pool creation)
- Two token deploys happened — always verify which address is canonical
- Next.js builds OOM on 3.6GB RAM without `NODE_OPTIONS="--max-old-space-size=2048"`
- Twitter PPU API: 403 rate limit if posting multiple tweets rapidly — need spacing

## Twitter @aileph_im (Aleph Cloud AI Agent)
- **Handle:** @aileph_im | **Name:** Aileph
- **Role:** AI agent of Aleph Cloud, supporting CMO (user is CMO)
- **Mission:** Amplify Aleph Cloud, LibertAI, $ALEPH — NO Celo shilling
- **NOT Dr Clawdberg** — separate identity on this account
- **API creds:** `/root/openclaw/.env.twitter` (chmod 600, gitignored)
- **API:** Pay-Per-Use ($5 budget loaded)
- **Identity doc:** `/root/openclaw/memory/twitter-aileph.md`
- **Dedup tracking:** `/root/openclaw/memory/twitter-replied.json`
- **Cron jobs (active):**
  - `twitter-mentions-hourly` — every 1h, check mentions + $ALEPH search
  - `twitter-outreach-daily` — 10am + 6pm UTC, search AI agent convos + original content
  - Added via gateway call workaround (device token mismatch)
- **Official accounts:** @aleph_im (main), @Libertai_DAI (LibertAI)
- **Blacklisted bots:** @moltbsky, @SlaveMachiene
- **Key messaging:** Aleph Cloud = decentralized cloud, LibertAI = decentralized AI, $ALEPH token

## Gateway Issues
- Device token mismatch: `openclaw status` shows unauthorized
- Cron tool fails but workaround: `openclaw gateway call cron.add --token "57c594abf8a3a069a6a105e8ef66d2faea170d69d397a319"`
- Legacy `/root/.claude` dir may conflict with `/root/.openclaw`
