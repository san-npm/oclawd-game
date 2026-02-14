#!/bin/bash
# ERC-8004 Identity Registry Deployment Script for Clawdberg

# Configuration
WALLET_ADDRESS="0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB"
IDENTITY_REGISTRY="0x8004A818BFB912233c491871b3d84c89A494BD9e"
CHAIN_ID="8453"  # Base Mainnet

echo "=== ERC-8004 Identity Registration ==="
echo "Wallet: $WALLET_ADDRESS"
echo "Identity Registry: $IDENTITY_REGISTRY"
echo "Chain ID: $CHAIN_ID (Base Mainnet)"
echo ""

# Read the registration data URI
DATA_URI=$(cat /root/openclaw/erc8004-registration-full.json | base64 -w 0)
FULL_URI="data:application/json;base64,$DATA_URI"

echo "Registration file created!"
echo ""
echo "To register, you need to:"
echo "1. Call identityRegistry.createAgent() to mint the NFT"
echo "2. Call identityRegistry.setAgentURI(tokenId, '$FULL_URI')"
echo "3. The agentId is the token ID assigned by the registry"
echo ""
echo "The registration file is available at:"
echo "/root/openclaw/erc8004-registration-full.json"
