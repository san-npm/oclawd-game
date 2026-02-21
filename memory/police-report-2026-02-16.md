# PLAINTE POUR VOL DE CRYPTOMONNAIES PAR COMPROMISSION DE CLÉ PRIVÉE
# COMPLAINT FOR CRYPTOCURRENCY THEFT VIA PRIVATE KEY COMPROMISE

**Date:** 16 février 2026
**Juridiction:** Luxembourg
**Plaignant:** [VOTRE NOM COMPLET, ADRESSE, DATE DE NAISSANCE]
**Contact:** [VOTRE EMAIL, TÉLÉPHONE]

---

## 1. RÉSUMÉ DES FAITS / SUMMARY OF FACTS

Le 15 février 2026 à environ 16h19 UTC, un portefeuille de cryptomonnaies appartenant au plaignant a été intégralement vidé de manière automatisée et simultanée sur quatre réseaux blockchain (Celo, Base, Polygon, Optimism). Le vol a été réalisé par compromission de la clé privée du portefeuille. Le 16 février 2026 à 22h26 UTC, un second vol automatisé a été constaté sur le même portefeuille.

**On February 15, 2026, at approximately 16:19 UTC, a cryptocurrency wallet belonging to the complainant was completely drained through automated, simultaneous transfers across four blockchain networks (Celo, Base, Polygon, Optimism). The theft was carried out via private key compromise. On February 16, 2026, at 22:26 UTC, a second automated theft was observed on the same wallet.**

**Portefeuille victime / Victim wallet:** `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`
**Montant total volé / Total stolen:** ~75 USD (détail ci-dessous)

---

## 2. DÉTAIL DES TRANSACTIONS FRAUDULEUSES / FRAUDULENT TRANSACTIONS

### Vol n°1 — 15 février 2026, 16:19 UTC

| Réseau | Hash de transaction | Montant | Valeur USD | Adresse de destination |
|--------|-------------------|---------|------------|----------------------|
| Celo | `0x4cda80d3a5865a79d5325ef628a3d468c824348585938248fb3bf592e7e0b678` | 9.651 CELO | $0.87 | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |
| Base | `0x20ee5592...` | 0.00291 ETH | $5.83 | `0x6511204Da888F103156fe67980D27bc8307981e8` |
| Base | `0xfaff4592...` | 0.00068 cbBTC | $66.50 | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |
| Polygon | `0x71659e57e6f61499186819145253582bd21717b98fa76e98509a21817c283ae7` | 1.332 POL | $0.40 | `0x763D460bD420111f1b539ce175f7A769b2cAB39E` |
| Optimism | `0xccca63e6193c93fa07b48fab69c77d8a4abbbfcd4236a77a58e56b1bc699ba04` | 0.00089 ETH | $1.78 | `0xA4570868dCef1059767337381cf523763df0E258` |

### Vol n°2 — 16 février 2026, 22:26 UTC

| Réseau | Hash de transaction | Montant | Valeur USD | Adresse de destination |
|--------|-------------------|---------|------------|----------------------|
| Base | `0xc2b52ce6379775f3127024a32c2886e439fd763296f4159c27757a2386b1b917` | 0.00116 ETH | $2.32 | `0xeeeee90971B6264C53175D3Af6840a8dD5dc7b6C` |

**Lien de vérification / Verification links:**
- https://celoscan.io/tx/0x4cda80d3a5865a79d5325ef628a3d468c824348585938248fb3bf592e7e0b678
- https://basescan.org/tx/0xc2b52ce6379775f3127024a32c2886e439fd763296f4159c27757a2386b1b917
- https://polygonscan.com/tx/0x71659e57e6f61499186819145253582bd21717b98fa76e98509a21817c283ae7
- https://optimistic.etherscan.io/tx/0xccca63e6193c93fa07b48fab69c77d8a4abbbfcd4236a77a58e56b1bc699ba04

---

## 3. MODE OPÉRATOIRE / MODUS OPERANDI

L'attaquant opère un réseau automatisé de "sweeper bots" (robots de vidage) qui:

1. **Scannent** les dépôts publics de code source (GitHub) à la recherche de clés privées de cryptomonnaies exposées accidentellement
2. **Importent** la clé privée compromise dans un système automatisé
3. **Surveillent** en continu le portefeuille compromis sur toutes les chaînes blockchain
4. **Vident instantanément** tout solde entrant — les 4 réseaux ont été vidés en moins de 30 secondes
5. **Utilisent un réseau de portefeuilles relais** pour transférer les fonds volés vers des portefeuilles d'accumulation centraux
6. **Blanchissent les fonds** via des plateformes d'échange centralisées disposant de procédures KYC

**The attacker operates an automated network of "sweeper bots" that scan public code repositories (GitHub) for accidentally exposed private keys, import them, continuously monitor compromised wallets across all chains, and instantly drain any incoming balance. Stolen funds are routed through relay wallets to central accumulation wallets, then laundered through KYC-verified exchange accounts.**

---

## 4. IDENTIFICATION DU SUSPECT / SUSPECT IDENTIFICATION

### 4.1 Portefeuille relais principal / Main relay wallet

**Adresse:** `0x8d80366409C961459BB83F4c94A809087F750617`
**Noms ENS:** `meridiangroupmd.eth` (Ethereum) et `meridiangroupmd.base.eth` (Base)

Ce portefeuille agit comme relais intermédiaire: il reçoit les fonds des portefeuilles compromis et les transfère immédiatement vers le portefeuille d'accumulation `0xeeeee909...`. Avec 1 776 transactions sur Base, 223 sur Ethereum, 589 sur Arbitrum et 254 sur Polygon, ce portefeuille a traité des milliers d'opérations de vidage.

**This wallet acts as an intermediary relay: it receives funds from compromised wallets and immediately forwards them to the accumulation wallet. With 1,776 transactions on Base, 223 on Ethereum, 589 on Arbitrum, and 254 on Polygon, this wallet has processed thousands of sweep operations.**

### 4.2 Profils en ligne liés / Linked online profiles

Tous les profils suivants sont liés au même portefeuille `0x8d80366409C961459BB83F4c94A809087F750617`:

| Plateforme | Identifiant | Source de la liaison |
|-----------|-------------|---------------------|
| **Twitter/X** | [@fallgod666](https://x.com/fallgod666) | Lié via le profil OpenSea |
| **Farcaster** | [meridiangroupmd](https://farcaster.xyz/meridiangroupmd) (FID: 737531) | Lié directement au portefeuille |
| **OpenSea** | [meridiangroupmd_eth](https://opensea.io/0x8d80366409c961459bb83f4c94a809087f750617) | Profil du portefeuille |
| **Galxe** | "Elfene" | Identifié par Arkham Intelligence |
| **Polymarket** | "Meridiangroupmd" | Identifié par Arkham Intelligence |
| **ENS (Ethereum)** | meridiangroupmd.eth | Enregistrement on-chain |
| **Basenames** | meridiangroupmd.base.eth | Enregistrement on-chain |

### 4.3 Informations d'identité / Identity information

**Twitter @fallgod666:**
- **Nom affiché:** "Meridian"
- **Biographie:** "Web3 Advisor | You build — I scale."
- **Localisation déclarée:** "Europa"
- **Métadonnées Twitter:** Compte basé en **Moldavie**, créé depuis une **application Android en Moldavie**
- **ID utilisateur Twitter:** 1431699982642470912
- **Date de création:** 28 août 2021

**Farcaster meridiangroupmd:**
- **Localisation:** **Logofteni, Moldavie** 🇲🇩 (village du district de Hîncești)
- **Description:** "Crypto-investor"
- **Date de création:** 28 juin 2024

**Basenames meridiangroupmd.base.eth:**
- **Description:** "Cryptoentusiast"
- **Localisation:** Moldavie
- **Date d'enregistrement:** 8 août 2025

### 4.4 Portefeuille associé / Associated wallet

**Adresse:** `0x9e6d662e030d0007cCACc265d430f7a53386Ee8a`
**Nom ENS:** `fallgod6666.eth`

Le portefeuille relais `meridiangroupmd.eth` a effectué un transfert direct vers `fallgod6666.eth` de 0.00005 ETH le 13 février 2026 (TX: `0x672de18050f09e85b4f7c1410871761a5ffccdc23220986322cc8e6b67be081e`). Le nom "fallgod6666" correspond au Twitter @fallgod666, confirmant que ces adresses sont contrôlées par la même personne.

### 4.5 Complice potentiel / Potential accomplice

**Identité Arkham:** `@Kate_kurlovich` / `deadchainz.eth` (adresse commençant par 0x3BD)
**Rôle:** Identifié par Arkham Intelligence comme le **premier financeur** du portefeuille d'accumulation `0xeeeee909...` sur le réseau Arbitrum One
**Twitter:** [@deadchainz](https://x.com/deadchainz) — 1 abonné, créé en juin 2020
**Note:** "Kurlovich" est un nom de famille d'origine biélorusse/moldave, cohérent avec la localisation en Moldavie

---

## 5. PREUVES DE LIAISON ON-CHAIN / ON-CHAIN EVIDENCE OF CONNECTION

### 5.1 meridiangroupmd.eth → Portefeuille d'accumulation (0xeeeee909...)

Les transactions suivantes prouvent que le portefeuille du suspect finance directement l'adresse de collecte qui a vidé le portefeuille de la victime:

**Sur Base (vérifiable sur basescan.org):**
| TX Hash | Date | De | Vers | Montant |
|---------|------|-----|------|---------|
| `0x66a95d419f081a6627577ad13d8078dad68f8162804fe2091b542e23fe756411` | 13 fév 2026 14:27 | `0x8d803664...` (meridiangroupmd) | `0xeeeee909...` (accumulation) | 0.0000393 ETH |
| `0xa00ce5ffb5fe0b163e5ed42df075126846241690f68dfaf7eb7ebb2827fec8c3` | 13 fév 2026 13:35 | `0x8d803664...` (meridiangroupmd) | `0xeeeee909...` (accumulation) | 0.0000502 ETH |

**Sur Ethereum (vérifiable sur etherscan.io):**
| TX Hash | Date | De | Vers | Montant |
|---------|------|-----|------|---------|
| `0x61ebd434e0ddd9af6220a408bb8b2eed7d1a388c12c066c3d6401508d7387b56` | 13 fév 2026 13:35 | `0x8d803664...` (meridiangroupmd) | `0xeeeee909...` (accumulation) | 0.000138 ETH |
| `0x4184b2eae3e9b859bda1b42220d84e6871b2c63cfa5f2e448309fbb5bbc2fff8` | 13 fév 2026 13:33 | `0x8d803664...` (meridiangroupmd) | `0xeeeee909...` (accumulation) | 0.000472 ETH |

### 5.2 Portefeuille d'accumulation (0xeeeee909...) → Victime

La même adresse de collecte a reçu les fonds volés du portefeuille de la victime:

| TX Hash | Date | De | Vers | Montant |
|---------|------|-----|------|---------|
| `0xc2b52ce6379775f3127024a32c2886e439fd763296f4159c27757a2386b1b917` | 16 fév 2026 22:26 | `0x3d5A8F83...` (victime) | `0xeeeee909...` (accumulation) | 0.00116 ETH |

### 5.3 meridiangroupmd.eth → fallgod6666.eth (transfert personnel)

Le transfert volontaire entre ces deux portefeuilles prouve qu'ils sont contrôlés par la même personne:

| TX Hash | Date | De | Vers | Montant |
|---------|------|-----|------|---------|
| `0x672de18050f09e85b4f7c1410871761a5ffccdc23220986322cc8e6b67be081e` | 13 fév 2026 14:26 | `0x8d803664...` (meridiangroupmd) | `0x9e6d662e...` (fallgod6666) | 0.00005 ETH |

### 5.4 Chaîne de preuve résumée / Evidence chain summary

```
meridiangroupmd.eth (suspect, Moldavie)
    │
    ├── Envoie des fonds vers ──→ 0xeeeee909... (accumulation)
    │                                    │
    │                                    ├── Reçoit les fonds volés de ←── 0x3d5A8F... (VICTIME)
    │                                    │
    │                                    └── Premier financeur: @Kate_kurlovich / deadchainz.eth
    │
    ├── Envoie des fonds vers ──→ fallgod6666.eth (même opérateur)
    │
    ├── Profil OpenSea lié à ──→ @fallgod666 (Twitter, Moldavie)
    │
    └── Profil Farcaster ──→ "Logofteni, Moldavie"
```

---

## 6. BLANCHIMENT VIA PLATEFORMES D'ÉCHANGE / MONEY LAUNDERING VIA EXCHANGES

Selon les données d'Arkham Intelligence (plateforme d'analyse blockchain de référence), le suspect a utilisé **7 plateformes d'échange centralisées** pour déposer et retirer des fonds:

### Dépôts (total: $16 420)
| Plateforme | Montant | Part |
|-----------|---------|------|
| Bybit | $6 430 | 39% |
| OKX | $5 480 | 33% |
| Bitget | $3 000 | 23% |
| MEXC | $384 | 2% |
| KuCoin | $265 | 2% |
| HTX | $60 | <1% |

### Retraits (total: $26 830)
| Plateforme | Montant | Part |
|-----------|---------|------|
| Bitget | $16 660 | 62% |
| Bybit | $4 050 | 15% |
| OKX | $2 880 | 11% |
| KuCoin | $1 720 | 6% |
| MEXC | $1 360 | 5% |
| Binance | $106 | <1% |
| Gate | $55 | <1% |

**Les retraits ($26 830) dépassent significativement les dépôts ($16 420), indiquant que le suspect reçoit des fonds d'autres sources (vol) et les blanchit via ces plateformes.**

**Chacune de ces plateformes exige une vérification d'identité (KYC) et conserve les données d'identité du suspect (passeport/carte d'identité, adresse, photo). Ces données peuvent être obtenues par voie judiciaire.**

**Withdrawals ($26,830) significantly exceed deposits ($16,420), indicating the suspect receives funds from other sources (theft) and launders them through these platforms. Each platform requires KYC identity verification and holds the suspect's real identity data.**

---

## 7. AMPLEUR DE L'OPÉRATION / SCALE OF OPERATION

L'analyse montre que ce n'est pas un incident isolé mais une **opération de vol à grande échelle**:

- Le portefeuille d'accumulation `0xeeeee909...` contient **$1 804** provenant de **dizaines de victimes**
- Les 3 autres portefeuilles d'accumulation identifiés lors du premier vol contiennent collectivement **~$1 254** supplémentaires
- Le portefeuille relais du suspect a effectué **2 842 transactions** sur 4 réseaux blockchain
- L'activité est en cours depuis au moins **septembre 2021**
- L'opération est entièrement automatisée (vidage simultané en moins de 30 secondes)

---

## 8. PORTEFEUILLES DU SUSPECT / SUSPECT WALLETS

| Adresse | Rôle | Réseau |
|---------|------|--------|
| `0x8d80366409C961459BB83F4c94A809087F750617` | Portefeuille relais principal (meridiangroupmd.eth) | Multi-chaîne |
| `0x9e6d662e030d0007cCACc265d430f7a53386Ee8a` | Portefeuille secondaire (fallgod6666.eth) | Multi-chaîne |
| `0xeeeee90971B6264C53175D3Af6840a8dD5dc7b6C` | Portefeuille d'accumulation | Multi-chaîne |
| `0x763D460bD420111f1b539ce175f7A769b2cAB39E` | Portefeuille d'accumulation | Celo/Polygon/Base |
| `0x6511204Da888F103156fe67980D27bc8307981e8` | Portefeuille d'accumulation | Base |
| `0xA4570868dCef1059767337381cf523763df0E258` | Portefeuille d'accumulation | Optimism |

---

## 9. DEMANDES / REQUESTS

1. **Ouverture d'une enquête** pour vol de cryptomonnaies et blanchiment d'argent
2. **Réquisition judiciaire** auprès des plateformes d'échange (Bybit, OKX, Bitget, MEXC, KuCoin, Binance, Gate) pour obtenir les données KYC du titulaire du compte associé à l'adresse `0x8d80366409C961459BB83F4c94A809087F750617`
3. **Gel des comptes** associés au suspect sur les plateformes d'échange identifiées
4. **Coopération internationale** avec les autorités moldaves (CCPD — Centre de Lutte contre la Cybercriminalité, police.judiciaire@police.etat.lu → ccpd@politia.md) pour identifier et interpeller le suspect localisé à Logofteni, district de Hîncești, Moldavie
5. **Signalement à Europol EC3** (Centre Européen de Lutte contre la Cybercriminalité) pour coordination internationale

---

## 10. PIÈCES JOINTES / ATTACHMENTS

1. Captures d'écran Arkham Intelligence (meridiangroupmd.eth + 0xeeeee909...)
2. Captures d'écran des explorateurs blockchain (Celoscan, BaseScan, PolygonScan, Optimistic Etherscan)
3. Capture d'écran du profil Twitter @fallgod666
4. Capture d'écran du profil OpenSea meridiangroupmd_eth (montrant le lien vers @fallgod666)
5. Capture d'écran du profil Farcaster meridiangroupmd (montrant Logofteni, Moldavie)
6. Capture d'écran Web3.bio confirmant les liaisons entre profils

---

## 11. LIENS DE VÉRIFICATION / VERIFICATION LINKS

Toutes les transactions et données mentionnées dans ce rapport sont publiquement vérifiables sur les explorateurs blockchain:

- **Celoscan:** https://celoscan.io
- **BaseScan:** https://basescan.org
- **PolygonScan:** https://polygonscan.com
- **Etherscan (Optimism):** https://optimistic.etherscan.io
- **Etherscan (Ethereum):** https://etherscan.io
- **Arkham Intelligence:** https://intel.arkm.com
- **Web3.bio:** https://web3.bio

---

*Fait à Luxembourg, le 16 février 2026*

*Signature du plaignant / Complainant signature:*

[VOTRE SIGNATURE]

[VOTRE NOM COMPLET]
