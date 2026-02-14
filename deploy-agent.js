const { ethers } = require('ethers');
const fs = require('fs');

// Configuration
const WALLET_ADDRESS = '0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB';
const PRIVATE_KEY = '0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901';
const IDENTITY_REGISTRY = '0x8004A169FB4a3325136EB29fA0ceB6D2e539a432'; // Base Mainnet Identity Registry
const RPC_URL = 'https://base.publicnode.com';

const provider = new ethers.JsonRpcProvider(RPC_URL);

async function setAgentURI() {
  try {
    console.log('Connecting to Base Mainnet...');
    
    // Create wallet
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
    console.log('Wallet address:', wallet.address);
    
    // Read the base64 data URI from the registration file
    const fullRegistration = JSON.parse(fs.readFileSync('/root/openclaw/erc8004-registration-full.json', 'utf8'));
    const base64Data = Buffer.from(JSON.stringify(fullRegistration)).toString('base64');
    const dataUri = `data:application/json;base64,${base64Data}`;
    
    console.log('Data URI length:', dataUri.length);
    
    // Get the token ID from the first registration transaction
    const txHash = '0x1cc2677c44d50ff0651ecb882c43a68998c8890057bff219fefb2faf4e0a895e';
    const receipt = await provider.getTransactionReceipt(txHash);
    
    // Find the Transfer event to get the token ID
    let tokenId = null;
    for (const log of receipt.logs) {
      if (log.topics?.[0] === '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef' && log.topics.length === 4) {
        // Transfer event - third topic is the token ID
        tokenId = log.topics[2];
        console.log('Found Transfer event, token ID:', tokenId);
        break;
      }
    }
    
    if (!tokenId) {
      console.log('❌ Could not find token ID in transaction logs');
      return;
    }
    
    // Simple register function using raw transaction
    const contractAddress = IDENTITY_REGISTRY;
    
    // Encode the function call data for setAgentURI
    const iface = new ethers.Interface([
      'function setAgentURI(uint256 tokenId, string agentURI) public'
    ]);
    
    const data = iface.encodeFunctionData('setAgentURI', [tokenId, dataUri]);
    console.log('Encoded data:', data.substring(0, 100) + '...');
    
    // Get gas estimate
    const txParams = {
      to: contractAddress,
      data: data,
      from: WALLET_ADDRESS
    };
    
    const gasEstimate = await provider.estimateGas(txParams);
    console.log('Gas estimate:', gasEstimate.toString());
    
    const feeData = await provider.getFeeData();
    const gasPrice = feeData.gasPrice;
    console.log('Gas price:', gasPrice.toString());
    
    // Build transaction
    const tx = {
      to: contractAddress,
      data: data,
      gasLimit: gasEstimate * 12n / 10n,
      gasPrice: gasPrice,
      nonce: await provider.getTransactionCount(WALLET_ADDRESS)
    };
    
    console.log('\nSending transaction...');
    const sendTx = await wallet.sendTransaction(tx);
    console.log('Transaction sent:', sendTx.hash);
    
    console.log('Waiting for confirmation...');
    const receipt2 = await sendTx.wait();
    console.log('\n✅ Transaction confirmed!');
    console.log('Transaction hash:', receipt2.hash);
    console.log('Block number:', receipt2.blockNumber);
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    console.error('Full error:', error);
    console.error('Stack:', error.stack);
  }
}

setAgentURI();