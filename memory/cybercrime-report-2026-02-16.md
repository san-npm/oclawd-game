# Cybercrime Report — Multi-Chain Crypto Theft via Private Key Sweeper

**Date of report:** 2026-02-16
**Date of incident:** 2026-02-15 ~16:19 UTC
**Victim wallet:** `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`

---

## Summary

On February 15, 2026, at approximately 16:19 UTC, an automated sweeper bot drained all funds from the victim's cryptocurrency wallet across 4 blockchain networks simultaneously (Celo, Base, Polygon, Optimism). The attack was executed using the victim's compromised private key, which had been inadvertently exposed in a public GitHub repository. The stolen funds were sent to accumulation wallets controlled by the attacker.

On February 16, 2026, at 22:26 UTC, the same wallet was swept again by a second sweeper bot linked to the same operator, confirming active ongoing monitoring.

**Total stolen: ~$75 USD equivalent**

---

## Attack Details

### Method
- Private key was exposed in a public GitHub repository (`base-arbitrage-agent/.env`)
- Automated bots scan GitHub for exposed private keys
- All 4 chains swept within 30 seconds (coordinated automated attack)
- Ongoing active sweeper monitoring the wallet — any funds sent are immediately stolen

### Transactions (Drain #1 — Feb 15, 16:19 UTC)

| Chain | TX Hash | Amount | Destination |
|-------|---------|--------|-------------|
| Celo | `0x4cda80d3a5865a79d5325ef628a3d468c824348585938248fb3bf592e7e0b678` | 9.65 CELO ($0.87) | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |
| Base | `0x20ee5592...` | 0.00291 ETH ($5.83) | `0x6511204Da888F103156fe67980D27bc8307981e8` |
| Base | `0xfaff4592...` | 0.00068 cbBTC ($66.50) | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |
| Polygon | `0x71659e57e6f61499186819145253582bd21717b98fa76e98509a21817c283ae7` | 1.33 POL ($0.40) | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |
| Optimism | `0xccca63e6193c93fa07b48fab69c77d8a4abbbfcd4236a77a58e56b1bc699ba04` | 0.00089 ETH ($1.78) | `0xA4570868dCef1059767337381cf523763df0E258` |

### Transaction (Drain #2 — Feb 16, 22:26 UTC)

| Chain | TX Hash | Amount | Destination |
|-------|---------|--------|-------------|
| Base | `0xc2b52ce6379775f3127024a32c2886e439fd763296f4159c27757a2386b1b917` | 0.00116 ETH ($2.32) | `0xeeeee90971B6264C53175D3Af6840a8dD5dc7b6C` |

---

## Attacker Accumulation Wallets

All wallets are **receive-only accumulators** with dozens of victim deposits (mass drainer operation):

1. **`0x763D460bD420111f1b539ce175f7A769b2cAB39E`** — Celo/Polygon/Base, ~$26 CELO accumulated
2. **`0x6511204Da888F103156fe67980D27bc8307981e8`** — Base, ~$1,104 ETH accumulated
3. **`0xA4570868dCef1059767337381cf523763df0E258`** — Optimism, ~$124 ETH accumulated
4. **`0xeeeee90971B6264C53175D3Af6840a8dD5dc7b6C`** — Base/Ethereum/multi-chain, ~$160 ETH accumulated

---

## Suspect Identification

### Primary Relay Wallet (Sweeper Bot Operator)
- **Address:** `0x8d80366409C961459BB83F4c94A809087F750617`
- **ENS names:** `meridiangroupmd.eth` (Ethereum) + `meridiangroupmd.base.eth` (Base)
- **Role:** Intermediary relay wallet — receives stolen funds from victim wallets and forwards to accumulator `0xeeeee909...`
- **Activity:** 1,776 nonce on Base, 223 on Ethereum, 589 on Arbitrum, 254 on Polygon — thousands of sweep operations
- **Also interacts with:** `fallgod6666.eth` (`0x9e6d662e030d0007cCACc265d430f7a53386Ee8a`) — same operator

### Linked Social Media / Identity

**Twitter:** [@fallgod666](https://x.com/fallgod666)
- **Display name:** "Meridian"
- **Bio:** "Web3 Advisor | You build — I scale."
- **Location:** "Europa"
- **Twitter About data:** Based in **Moldova**, account created from **Moldova Android App**
- **Twitter User ID:** `1431699982642470912`
- **Joined:** August 28, 2021
- **158 followers, 232 following, 311 tweets**

**Farcaster:** [meridiangroupmd](https://farcaster.xyz/meridiangroupmd)
- **FID:** 737531
- **Display name:** "Meridian"
- **Description:** "Crypto-investor"
- **Location:** **Logofteni, Moldova** 🇲🇩
- **Joined:** June 28, 2024

**Basenames profile:**
- **Description:** "Cryptoentusiast"
- **Location:** Moldova
- **Registered:** August 8, 2025

**OpenSea:** [meridiangroupmd_eth](https://opensea.io/0x8d80366409c961459bb83f4c94a809087f750617)
- Linked Twitter: @fallgod666
- OpenSea Beta Tester since August 2022

### Geographic Location
- **Country:** Moldova 🇲🇩
- **Specific location:** **Logofteni** (village in Hîncești district, Moldova)
- Consistent across all profiles (Farcaster, Basenames, Twitter metadata)

### Behavioral Profile
- Active airdrop farmer (begging for invite codes to Redstone, Euphoria, zkPass)
- Interacts frequently with: @OVGNFT, @steezehuman, @erequendi, @brevis_zk
- Claims to be in crypto since 2021
- Uses "Fair Shares" referral links (possible additional scam)
- Bybit user (mentioned sending USDC to Bybit on Sonic network)

---

## Evidence of Connection Between Suspect and Sweeper

1. `meridiangroupmd.base.eth` sent ETH directly to sweeper accumulator `0xeeeee909...dD5dc7b6C`:
   - TX `0x66a95d41...` — 0.00003934 ETH on Feb 13, 2026
   - TX `0xa00ce5ff...` — 0.00005023 ETH on Feb 13, 2026
2. `meridiangroupmd.eth` sent ETH to `0xeeeee909...dD5dc7b6C` on Ethereum mainnet:
   - TX `0x61ebd434...` — 0.00013849 ETH on Feb 13, 2026
   - TX `0x4184b2ea...` — 0.000472 ETH on Feb 13, 2026
3. Pattern: receives from compromised wallets → immediately forwards to `0xeeeee909...`
4. Same `0xeeeee909...` wallet received the Feb 16 sweep of the victim's wallet

---

## Arkham Intelligence Findings (Feb 16, 2026)

### meridiangroupmd.eth (0x8d8d8)
- **Galxe username:** "Elfene"
- **Polymarket username:** "Meridiangroupmd"
- **OpenSea:** meridiangroupmd_eth (Beta tester since Aug 2022)
- **+29 additional platform identities** (visible on Arkham with "+29 MORE" tag)
- **Active since:** September 2, 2021
- **Exchange deposits (total $16.42K):** Bybit $6.43K (39%), OKX $5.48K (33%), Bitget $3.0K (23%), MEXC $384, KuCoin $265, HTX $60
- **Exchange withdrawals (total $26.83K):** Bitget $16.66K (62%), Bybit $4.05K (15%), OKX $2.88K (11%), KuCoin $1.72K, MEXC $1.36K, Binance $106, Gate $55
- **Note:** Withdrawals ($26.83K) significantly exceed deposits ($16.42K) — consistent with laundering stolen funds through exchanges

### Sweeper Accumulator 0xeeeee909...
- **Total holdings:** $1,804.25 (BNB $1.02K, ETH $249, cbBTC $157, USDT $180, USDC $53)
- **First funder on Arbitrum One:** `@Kate_kurlovich` / `deadchainz.eth` (0x3BD) — possible accomplice or alt account
- **@deadchainz on Twitter:** 1 follower, joined June 2020, bio "Hmu ladies", no location

### KYC-Verified Exchange Accounts
The suspect has deposited/withdrawn through **7 exchanges that require KYC verification:**
1. **Bybit** — $6.43K deposits, $4.05K withdrawals (most recent: 4 days ago)
2. **OKX** — $5.48K deposits, $2.88K withdrawals
3. **Bitget** — $3.0K deposits, $16.66K withdrawals (largest cashout destination)
4. **MEXC** — $384 deposits, $1.36K withdrawals
5. **KuCoin** — $265 deposits, $1.72K withdrawals
6. **Binance** — $106 withdrawals
7. **Gate** — $55 withdrawals

**Each of these exchanges holds KYC identity data that law enforcement can subpoena.**

---

## Reporting Channels

### Moldova
- **CCPD (Center for Combating Cybercrime):** Part of Moldova's General Police Inspectorate
- **Email:** ccpd@politia.md
- **Website:** https://politia.md

### EU / International
- **Europol EC3 (European Cybercrime Centre):** Report via national contact point
- **IC3 (FBI Internet Crime Complaint Center):** https://www.ic3.gov (if US-based victim)

### Blockchain-Specific
- **Chainalysis / Elliptic / TRM Labs:** Blockchain analytics firms that assist law enforcement
- **Etherscan/Basescan:** Flag addresses as phishing/scam
- **Bybit:** Suspect is a Bybit user — Bybit compliance can freeze associated accounts

---

## Verification Links

- Celoscan TX: https://celoscan.io/tx/0x4cda80d3a5865a79d5325ef628a3d468c824348585938248fb3bf592e7e0b678
- BaseScan sweep: https://basescan.org/tx/0xc2b52ce6379775f3127024a32c2886e439fd763296f4159c27757a2386b1b917
- Suspect wallet (Base): https://basescan.org/address/0x8d80366409c961459bb83f4c94a809087f750617
- Suspect wallet (ETH): https://etherscan.io/address/0x8d80366409c961459bb83f4c94a809087f750617
- Accumulator wallet: https://basescan.org/address/0xeeeee90971B6264C53175D3Af6840a8dD5dc7b6C
- OpenSea profile: https://opensea.io/0x8d80366409c961459bb83f4c94a809087f750617
- Twitter: https://x.com/fallgod666
- Farcaster: https://farcaster.xyz/meridiangroupmd
