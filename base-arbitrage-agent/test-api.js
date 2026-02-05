const axios = require('axios');

async function testGraph() {
  try {
    const response = await axios.post('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2/base', {
      query: `
        {
          tokens(first: 3) {
            id
            symbol
            name
          }
        }
      `
    });
    
    console.log('✅ Success!');
    console.log(JSON.stringify(response.data, null, 2));
  } catch (error) {
    console.error('❌ Error:', error.response?.data || error.message);
  }
}

testGraph();
