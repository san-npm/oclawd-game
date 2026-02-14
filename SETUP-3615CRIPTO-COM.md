# Setup Guide: 3615crypto.com Agent Endpoints

## Overview
This guide explains how to set up the public endpoints for Clawdberg agent on your 3615crypto.com domain.

## Files to Upload

### 1. A2A Agent Card
**Location:** `/root/openclaw/agent-card/index.json`

**Upload to:** `https://3615crypto.com/agent-card/index.json`

This file contains:
- Agent name, description, image
- A2A endpoint (version 0.3.0)
- MCP endpoint (version 2025-06-18)
- Tailscale IP address
- Capabilities, protocols, trust models

### 2. MCP Endpoint
**Location:** `/root/openclaw/mcp/index.html`

**Upload to:** `https://3615crypto.com/mcp/`

This is the MCP server endpoint for Model Context Protocol communication.

## Setup Steps

### Option A: Using FTP/SFTP
1. Connect to your server hosting 3615crypto.com
2. Navigate to the web root directory
3. Create `agent-card` directory (regular folder, no dot):
   ```bash
   mkdir -p agent-card
   ```
4. Upload `index.json` to `agent-card/` directory
5. Create `mcp` directory:
   ```bash
   mkdir mcp
   ```
6. Upload `index.html` to `mcp/` directory

### Option B: Using SSH/SCP
```bash
# Upload agent card
scp /root/openclaw/agent-card/index.json user@your-server:/var/www/3615crypto.com/agent-card/

# Upload MCP page
scp /root/openclaw/mcp/index.html user@your-server:/var/www/3615crypto.com/mcp/
```

### Option C: Using Git (if 3615crypto.com is git-deployed)
```bash
# Clone the repo
git clone https://github.com/your-org/3615crypto.com.git
cd 3615crypto.com

# Create directories
mkdir -p agent-card mcp

# Copy files
cp /root/openclaw/agent-card/index.json agent-card/
cp /root/openclaw/mcp/index.html mcp/

# Commit and push
git add .
git commit -m "Add Clawdberg agent endpoints"
git push
```

## File Structure After Setup
```
/var/www/3615crypto.com/
├── agent-card/
│   └── index.json    ← Your agent registration
├── mcp/
│   └── index.html    ← MCP endpoint
└── ... (your existing files)
```

## Verify Setup
After uploading, verify the endpoints are accessible:

```bash
# Test A2A agent card
curl https://3615crypto.com/agent-card/index.json

# Test MCP endpoint
curl https://3615crypto.com/mcp/
```

## Registration Steps

### 1. Deploy Identity Registry NFT
1. Visit: https://basescan.io/address/0x8004A818BFB912233c491871b3d84c89A494BD9e
2. Connect your wallet (0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB)
3. Call `createAgent()` to mint the NFT
4. Call `setAgentURI()` with the data URI from `erc8004-datauri-registration.json`

### 2. Submit to 8004scan.io
Once on-chain, submit your agent to 8004scan.io for public listing.

## Notes
- Make sure the domain is HTTPS (SSL certificate required)
- The `.well-known` directory is a standard location for agent cards
- Tailscale IP is for agents on your network, not public access
- Update the image URL to point to your actual agent image on IPFS

## Final Check
After setup, other agents should be able to:
1. Discover Clawdberg via Identity Registry
2. Fetch registration from `.well-known/agent-card.json`
3. Connect via A2A or MCP protocols