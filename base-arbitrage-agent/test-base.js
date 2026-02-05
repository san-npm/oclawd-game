const axios = require('axios');
const { ethers } = require('ethers');

async function testBaseScan() {
  try {
    const response = await axios.get('https://api.basescan.org/api', {
      params: {
        module: 'stats',
        action: 'ethprice',
        apikey: 'YourApiKeyToken' // Would need actual API key
      }
    });
    
    console.log('BaseScan ETH Price:', response.data);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

testBaseScan();
