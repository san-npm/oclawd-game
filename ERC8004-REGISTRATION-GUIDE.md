# ERC-8004 Identity Registration for Clawdberg

## Overview
This document details the ERC-8004 identity registration for Clawdberg, an AI assistant agent registered on the 8004scan.io platform.

## Registration Details

### Agent Identity
- **Name:** Clawdberg
- **Agent ID (Wallet):** `0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB`
- **Chain:** Base Mainnet (Chain ID: 8453)
- **Identity Registry:** `0x8004A818BFB912233c491871b3d84c89A494BD9e`
- **Agent URI:** `https://3615crypto.com/.well-known/agent-card.json`

### Agent Profile
Clawdberg is a Zoidberg-inspired AI assistant specialized in:
- Web3 integration and blockchain deployments
- Agent orchestration and task automation
- Social media integration (Twitter/X, Farcaster)
- Browser automation and file operations

### Capabilities
- Web interaction and browser automation
- File operations
- Email management (Gmail integration)
- Twitter/X integration
- Smart contract deployment
- Agent orchestration

### Protocols Supported
- A2A (Agent-to-Agent)
- MCP (Model Context Protocol)

### Trust Models
- Reputation-based validation
- Validation registry integration
- Crypto-economic trust

## Agent Endpoints

| Service | Endpoint | Purpose |
|---------|----------|---------|
| **A2A** | `https://3615crypto.com/.well-known/agent-card.json` | Agent-to-Agent communication card |
| **MCP** | `https://3615crypto.com/mcp` | Model Context Protocol endpoint |
| **Tailscale** | `100.69.28.116` | Direct IP access via Tailscale network |

## Registration Files

### 1. Full Registration JSON
Location: `/root/openclaw/erc8004-registration-full.json`

Contains the complete agent registration with:
- Agent name, description, image
- Services array (A2A, MCP, Tailscale)
- Capabilities and protocols
- Trust models and configurations
- Agent ID and registration reference

### 2. Data URI Registration
Location: `/root/openclaw/erc8004-datauri-registration.json`

Contains the full registration with services as a base64-encoded data URI for on-chain storage.

### 3. Deployment Script
Location: `/root/openclaw/deploy-erc8004.sh`

Bash script to deploy the registration to the Identity Registry.

## Deployment Instructions

### Option 1: Using the Deployment Script
```bash
./deploy-erc8004.sh
```

### Option 2: Manual Deployment via Etherscan
1. Visit: https://basescan.io/address/0x8004A818BFB912233c491871b3d84c89A494BD9e
2. Connect your wallet
3. Use the write contract functionality to:
   - Call `createAgent()` to mint the NFT
   - Call `setAgentURI()` with the data URI

## ERC-8004 Agent Format

The registration file follows the ERC-8004 specification:

```json
{
  "type": "https://eips.ethereum.org/EIPS/eip-8004#registration-v1",
  "name": "Clawdberg",
  "description": "AI assistant description...",
  "image": "https://...",
  "services": [
    {
      "name": "A2A",
      "endpoint": "https://3615crypto.com/.well-known/agent-card.json",
      "version": "0.3.0"
    },
    {
      "name": "MCP",
      "endpoint": "https://3615crypto.com/mcp",
      "version": "2025-06-18"
    }
  ],
  "capabilities": {...},
  "protocols": ["A2A", "MCP"],
  "trustModels": ["reputation", "validation"],
  "x402Support": false,
  "active": true,
  "registrations": [...],
  "supportedTrust": [...]
}
```

## Agent Discovery

Other agents can discover Clawdberg by:
1. Querying the Identity Registry contract
2. Reading the agentURI from the ERC-721 token
3. Fetching the registration file from `https://3615crypto.com/.well-known/agent-card.json`
4. Verifying the agent through the Reputation and Validation registries

## Agent Interaction

Agents can interact with Clawdberg via:
- **A2A protocol** - Message `.well-known/agent-card.json` endpoint
- **MCP protocol** - Use `/mcp` endpoint for tool access
- **Tailscale network** - Direct connection to `100.69.28.116`

## Agent Identity Format

The agent's unique identifier follows the ERC-8004 format:
```
eip155:8453:0x8004A818BFB912233c491871b3d84c89A494BD9e
```

Where:
- `eip155` = chain family (EVM chains)
- `8453` = chain ID (Base Mainnet)
- `0x8004A818BFB912233c491871b3d84c89A494BD9e` = Identity Registry address
- The token ID is assigned when the agent is registered

## Files Summary

| File | Purpose |
|------|---------|
| `erc8004-registration-full.json` | Complete registration file |
| `erc8004-datauri-registration.json` | Registration with data URI for on-chain |
| `deploy-erc8004.sh` | Deployment script |
| `ERC8004-REGISTRATION-GUIDE.md` | This documentation |

## Next Steps

1. Deploy the Identity Registry NFT
2. Set the agentURI with the registration data
3. Register with Reputation and Validation registries
4. Submit to 8004scan.io for public listing
