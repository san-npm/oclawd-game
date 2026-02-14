const { ethers } = require('ethers');
const fs = require('fs');

// Configuration
const WALLET_ADDRESS = '0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB';
const PRIVATE_KEY = '0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901';
const IDENTITY_REGISTRY = '0x8004A169FB4a3325136EB29fA0ceB6D2e539a432'; // Base Mainnet Identity Registry
const RPC_URL = 'https://base.publicnode.com';

const provider = new ethers.JsonRpcProvider(RPC_URL);

async function checkTransaction() {
  const txHash = '0x1cc2677c44d50ff0651ecb882c43a68998c8890057bff219fefb2faf4e0a895e';
  
  console.log('Checking transaction:', txHash);
  
  try {
    const receipt = await provider.getTransactionReceipt(txHash);
    console.log('✅ Transaction confirmed!');
    console.log('Block number:', receipt.blockNumber);
    console.log('Gas used:', receipt.gasUsed.toString());
    console.log('Status:', receipt.status === 1 ? 'Success' : 'Failed');
    
    if (receipt.logs) {
      console.log('\n🔍 Logs found:', receipt.logs.length);
      for (const log of receipt.logs) {
        console.log('Log topic:', log.topics?.[0]);
        console.log('Log data:', log.data);
      }
    }
    
  } catch (error) {
    console.error('Error:', error.message);
  }
}

checkTransaction();