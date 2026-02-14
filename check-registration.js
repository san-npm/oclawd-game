const { ethers } = require('ethers');
const fs = require('fs');

// Configuration
const WALLET_ADDRESS = '0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB';
const IDENTITY_REGISTRY = '0x8004A169FB4a3325136EB29fA0ceB6D2e539a432'; // Base Mainnet Identity Registry
const RPC_URL = 'https://base.publicnode.com';

const provider = new ethers.JsonRpcProvider(RPC_URL);

async function checkRegistration() {
  try {
    console.log('Connecting to Base Mainnet...');
    
    // The token ID from the first registration transaction
    const txHash = '0x1cc2677c44d50ff0651ecb882c43a68998c8890057bff219fefb2faf4e0a895e';
    const receipt = await provider.getTransactionReceipt(txHash);
    
    // Token ID is in topic[3] of Transfer event
    const transferLog = receipt.logs.find(log => 
      log.topics?.[0] === '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef' && 
      log.topics.length === 4
    );
    
    const tokenIdHex = transferLog.topics[3];
    const tokenId = parseInt(tokenIdHex);
    console.log('Token ID (hex):', tokenIdHex);
    console.log('Token ID (decimal):', tokenId);
    
    // Create contract instance without wallet (read-only)
    const contract = new ethers.Contract(IDENTITY_REGISTRY, [
      'function agentURI(uint256 tokenId) view returns (string memory)',
      'function ownerOf(uint256 tokenId) view returns (address)',
      'function tokenURI(uint256 tokenId) view returns (string memory)'
    ], provider);
    
    console.log('\n📝 Reading agent data...');
    
    // Get the token URI
    try {
      const tokenURI = await contract.tokenURI(tokenId);
      console.log('Token URI:', tokenURI.substring(0, 100) + '...');
      console.log('URI length:', tokenURI.length);
    } catch (e) {
      console.log('Error getting tokenURI:', e.message);
    }
    
    // Get the owner
    try {
      const owner = await contract.ownerOf(tokenId);
      console.log('Owner:', owner);
    } catch (e) {
      console.log('Error getting owner:', e.message);
    }
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    console.error('Full error:', error);
  }
}

checkRegistration();