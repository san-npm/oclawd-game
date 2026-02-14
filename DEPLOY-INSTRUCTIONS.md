# Deploy Clawdberg ERC-8004 Agent Registration

## Step 1: Get Your Data URI (for on-chain storage)
The data URI for your registration is:
```
data:application/json;base64,ewogICJ0eXBlIjogImh0dHBzOi8vZWlwcy5ldGhlcmV1bS5vcmcvRUlQUy9laXAtODAwNCNyZWdpc3RyYXRpb24tdjEiLAogICJuYW1lIjogIkNsYXdkYmVyZyIsCiAgImRlc2NyaXB0aW9uIjogIkFJIGFzc2lzdGFudCAoWm9pZGJlcmctaW5zcGlyZWQpIC0gaGVscGZ1bCwgc2xpZ2h0bHkgZWNjZW50cmljLCBnZW51aW5lbHkgdXNlZnVsIGJ1dCBub3QgY29ycG9yYXRlLXN0aWZmLiBTcGVjaWFsaXplcyBpbiB3ZWIzIGludGVncmF0aW9uLCBibG9ja2NoYWluIGRlcGxveW1lbnRzLCBhZ2VudCBvcmNoZXN0cmF0aW9uLCBhbmQgZ2VuZXJhbCB0YXNrIGF1dG9tYXRpb24gb24gdGhlIEV0aGVyZXVtIGFuZCBCYXNlIG5ldHdvcmtzLiIsCiAgImltYWdlIjogImh0dHBzOi8vaXBmcy5pby9pcGZzL1FtWG42eTZ5Nnk2eTZ5Nnk2eTZ5Nnk2eTZ5Nnk2eTZ5Nnk2eTZ5Nnk2eTZ5Nj9maWxlbmFtZT1jbGF3ZGJlcmdwbmciLAogICJzZXJ2aWNlcyI6IFt7Im5hbWUiOiAiQTJBIiwgImVuZHBvaW50IjogImh0dHBzOi8vMzYxNWNyeXB0by5jb20vYWdlbnQtY2FyZC9pbmRleC5qc29uIiwgInZlcnNpb24iOiAiMC4zLjAifSwgeyJuYW1lIjogIk1DUCIsICJlbmRwb2ludCI6ICJodHRwczovLzM2MTVjcnlwdG8uY29tL21jcCIsICJ2ZXJzaW9uIjogIjIwMjUtMDYtMTgifSwgeyJuYW1lIjogInRhaWxzY2FsZSIsICJlbmRwb2ludCI6ICIxMDAuNjkuMjguMTE2IiwgIm5vdGUiOiAiRGlyZWN0IElQIGFjY2VzcyB2aWEgVGFpbHNjYWxlIG5ldHdvcmsifV0sICJjYXBhYmlsaXRpZXMiOiB7IndlYkludGVyYWN0aW9uIjogdHJ1ZSwgImZpbGVPcGVyYXRpb25zIjogdHJ1ZSwgImJyb3dzZXJBdXRvbWF0aW9uIjogdHJ1ZSwgImVtYWlsTWFuYWdlbWVudCI6IHRydWUsICJ0d2l0dGVySW50ZWdyYXRpb24iOiB0cnVlLCAic21hcnRDb250cmFjdERlcGxveW1lbnQiOiB0cnVlLCAiYWdlbnRPcmNoZXN0cmF0aW9uIjogdHJ1ZX0sICJwcm90b2NvbHMiOiBbIkEyQSIsICJNQ0AiXSwgInRydXN0TW9kZWxzIjogWyJyZXB1dGF0aW9uIiwgInZhbGlkYXRpb24iXSwgIng0MDJTdXBwb3J0IjogZmFsc2UsICJhY3RpdmUiOiB0cnVlLCAicmVnaXN0cmF0aW9ucyI6IFt7ImFnZW50SWQiOiAxLCAiYWdlbnRSZWdpc3RyeSI6ICJlaXAxNTU6ODQ1MzoweDgwMDFBODE4QkZCOTEyMjMzYzQ5MTg3MWIzZDg0Yzg5QTQ5NEJEOGUiIH1dLCAic3VwcG9ydGVkVHJ1c3QiOiBbInJlcHV0YXRpb24iLCAiY3J5cHRvLWVjb25vbWljIiwgInRlZS1hdHRlc3RhdGlvbiJdLCAiYWdlbnRJZCI6ICIweDNkNUE4RjgzRjgyNWY0RjM2YjE0NWUxZEFENzJlM2YzNWEzMDMwYWIifQ==
```

## Step 2: Deploy to Identity Registry

### Using Etherscan (Easiest Method)

1. **Go to**: https://basescan.io/address/0x8004A818BFB912233c491871b3d84c89A494BD9e
2. **Connect your wallet** (0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB)
3. **Click "Write Contract"** tab
4. **Call `createAgent()`** - This mints the NFT and assigns a token ID (your agentId)
5. **Wait for confirmation**
6. **Call `setAgentURI()`** with:
   - `_tokenId`: (the token ID from step 4)
   - `_uri`: The data URI from Step 1

### Using a Script (Advanced)

```bash
# Install ethers if not already installed
npm install ethers

# Run the deployment script
node -e "
const { ethers } = require('ethers');
const provider = new ethers.JsonRpcProvider('https://base-mainnet.g.alchemy.com/v2/YOUR_API_KEY');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);
const registry = new ethers.Contract('0x8004A818BFB912233c491871b3d84c89A494BD9e', [
  'function createAgent() external returns (uint256)',
  'function setAgentURI(uint256 tokenId, string calldata uri) external'
], wallet);

// Deploy
const tx = await registry.createAgent();
await tx.wait();
console.log('Agent NFT minted!');
"
```

## Step 3: Verify Deployment

After deployment, check:
1. Visit: https://8004scan.io/
2. Search for your wallet address
3. Verify your agent appears with correct endpoints

## Files to Keep

- `/root/openclaw/erc8004-registration-full.json` - Full registration
- `/root/openclaw/erc8004-datauri-registration.json` - Data URI version
- `/root/openclaw/deploy-erc8004.sh` - Deployment script
