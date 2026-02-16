# Wallet Drain Investigation

**Date:** 2026-02-16  
**Victim Wallet:** `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`  
**Drain Time:** 2026-02-15 ~16:19 UTC (coordinated across all chains simultaneously)

---

## Summary

The wallet was drained on Feb 15, 2026 at approximately 16:19 UTC across **4 chains simultaneously**. All native tokens and at least one ERC-20 (cbBTC) were swept to attacker-controlled accumulation wallets. The attacker used **3 different destination addresses** — two chain-specific collectors and one shared across Celo/Polygon/Base tokens.

**Total estimated value stolen:**
- 9.65 CELO (~$0.87)
- 1.33 POL (~$0.40)
- 0.00291611 ETH on Base (~$5.83)
- 0.00068212 cbBTC on Base (~$66.50 at ~$97.5k/BTC)
- 0.00089199 ETH on Optimism (~$1.78)
- **Total: ~$75.38**

---

## Chain-by-Chain Analysis

### 1. Celo (Chain 42220)

**Current Balance:** $0.00 CELO (fully drained)

**Drain Transaction:**
- TX: `0x4cda80d3a5865a79d5325ef628a3d468c824348585938248fb3bf592e7e0b678`
- Time: 2026-02-15 16:19:03
- Amount: **9.65117256 CELO** → `0x763D460bD420111f1b539ce175f7A769b2cAB39E`

**Pre-drain activity (Feb 14):** Normal usage — deploying AgentRaffleV3 contract, purchasing tickets, attestations, approvals (all to legitimate contracts like cUSD token, 0x8791Ac8c...E80275950, 0x8a5859aB...9C5761C25).

---

### 2. Base (Chain 8453)

**Current Balance:** 0.000010 ETH ($0.02) — near zero

**Drain Transactions (Feb 15 16:19):**

| TX | Type | Amount | Destination |
|---|---|---|---|
| `0x20ee5592...` | Native ETH | 0.00291611 ETH | `0x6511204Da888F103156fe67980D27bc8307981e8` |
| `0xfaff4592...` | cbBTC (ERC-20) | 0.00068212 cbBTC | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |

**Other ERC-20 outbound (pre-drain, likely legitimate):**
- Feb 8: 1.08 USDC → `0xC15fB53F...ccc26efd6` (swap)
- Feb 8: 1.08 fake "ꓴꓢꓓC" token → `0xc15f1FA9...1b8E9EFD6`
- Various swap/DeFi activity (Aerodrome, Uniswap, KyberSwap)

---

### 3. Polygon (Chain 137)

**Current Balance:** $0.00 POL (fully drained)

**Drain Transaction:**
- TX: `0x71659e57e6f61499186819145253582bd21717b98fa76e98509a21817c283ae7`
- Time: 2026-02-15 16:19:05
- Amount: **1.33294333 POL** → `0x763D460bD420111f1b539ce175f7A769b2cAB39E`

**Prior activity:** Only 2 total transactions — one Diamond call (Jan 27) and this drain.

---

### 4. Optimism (Chain 10)

**Current Balance:** 0.000010 ETH ($0.02) — near zero

**Drain Transaction:**
- TX: `0xccca63e6193c93fa07b48fab69c77d8a4abbbfcd4236a77a58e56b1bc699ba04`
- Time: 2026-02-15 16:19:29
- Amount: **0.00089199 ETH** → `0xA4570868dCef1059767337381cf523763df0E258`

**Prior activity:** Farcaster registration (Feb 5), Across Protocol bridge (Feb 5).

---

## Attacker Destination Addresses

### Address 1: `0x763D460bD420111f1b539ce175f7A769b2cAB39E`
- **Used on:** Celo (CELO), Polygon (POL), Base (cbBTC)
- **Current Celo balance:** ~$26.10 in CELO
- **Behavior:** **Receive-only accumulator** — has ZERO outbound transactions
- **Pattern:** Receives small amounts from dozens of different wallets (drip-drain pattern)
- **Notable senders:** Various .eth names (liveitx.eth, macmasterx.eth, abundancex.eth, jediman.eth, bombaman.eth, blessedx.eth, etc.) — suggesting mass compromise of wallets
- **Largest single deposit:** 33.81 CELO from `0xeF4DB09D...68976535E` (Jan 15)
- **Funds have NOT moved yet** — still accumulating

### Address 2: `0x6511204Da888F103156fe67980D27bc8307981e8`
- **Used on:** Base (ETH)
- **Current balance:** 0.5524 ETH (~$1,104)
- **Behavior:** **Receive-only accumulator** — has ZERO outbound transactions
- **Pattern:** Receives from many different wallets, small amounts each
- **Funds have NOT moved yet** — still accumulating

### Address 3: `0xA4570868dCef1059767337381cf523763df0E258`
- **Used on:** Optimism (ETH)
- **Current balance:** 0.0621 ETH (~$124)
- **Behavior:** **Receive-only accumulator** — has ZERO outbound transactions
- **Pattern:** Receives from many different wallets over months (since Nov 2025)
- **Notable senders:** Various .eth names (derianar.eth, smartdevx.eth, idhaniel.eth)
- **Funds have NOT moved yet** — still accumulating

---

## Attack Pattern Analysis

1. **Coordinated timing:** All chains drained within ~30 seconds of each other (16:19:03 to 16:19:29 UTC)
2. **Private key compromise:** The attacker had the victim's private key (or seed phrase) — they sent native tokens directly, no contract exploit
3. **Multi-chain sweep:** Automated bot that sweeps all chains simultaneously
4. **Mass operation:** All three destination wallets show the same pattern — receiving small amounts from many different victim wallets over weeks/months. This is a large-scale drainer operation, not a targeted attack.
5. **Funds not yet cashed out:** All three accumulation wallets still hold funds with no outbound transactions — the attacker hasn't consolidated or laundered yet.

---

## Remaining Assets in Victim Wallet

Per multichain portfolio (from Polygonscan):
- **52,276 CLAWD tokens** on Base (~$2.49) — not stolen (likely too illiquid)
- Dust ETH on Base and Optimism (~$0.02 each)
- Various airdropped tokens on Base (SPARKNET, Agent8, ADR, WAR, etc.) — not stolen

---

## Recommendations

1. **Do NOT send any more funds to this wallet** — the private key is compromised
2. **Revoke all token approvals** from this address on all chains
3. **Monitor the 3 attacker addresses** — when they start moving funds, it may reveal exchange deposit addresses
4. **Report to:** Celo/Base/Polygon/OP security teams; any exchanges the attacker addresses interact with
5. **Check how the key was compromised** — phishing, malware, seed phrase leak, etc.
