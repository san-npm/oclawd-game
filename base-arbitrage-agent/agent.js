const { ethers } = require('ethers');
const axios = require('axios');
require('dotenv').config();

const PRIVATE_KEY = process.env.PRIVATE_KEY;
const BASE_RPC_URL = process.env.BASE_RPC_URL || 'https://mainnet.base.org';
const WETH_CONTRACT = '0x4200000000000000000000000000000000000006';
const MIN_PROFIT = 0.005; // 0.5% profit
const TRADE_SIZE = ethers.parseEther('0.001'); // $2.20 worth
const DEX_ROUTERS = {
  UNISWAP_V2: '0xdef1c0ded9bec7f1a16708398fe3b2f871a03bad',
  UNISWAP_V3: '0xe592427a0aece92de3deecee1e8710b5953df3ef'
};

class ArbitrageAgent {
  constructor() {
    this.provider = new ethers.JsonRpcProvider(BASE_RPC_URL);
    this.wallet = new ethers.Wallet(PRIVATE_KEY, this.provider);
    console.log('🚀 Arbitrage Agent');
    console.log('Wallet:', this.wallet.address);
  }

  async start() {
    while (true) {
      try {
        console.log('🔍 Scanning for arbitrage...');
        
        // Get ETH price from Coingecko
        const ethPrice = await this.getETHPrice();
        console.log('💰 ETH Price:', ethPrice);
        
        // Get token data from Coingecko
        const tokens = await this.getTokens();
        
        for (const token of tokens.slice(0, 20)) {
          await this.checkToken(token, ethPrice);
        }

      } catch (error) {
        console.error('❌ Error:', error.message);
      }

      await new Promise(resolve => setTimeout(resolve, 30000));
    }
  }

  async getETHPrice() {
    try {
      const response = await axios.get('https://api.coingecko.com/api/v3/simple/price', {
        params: { ids: 'ethereum', vs_currencies: 'usd' }
      });
      return response.data.ethereum.usd;
    } catch (error) {
      console.error('Coingecko failed:', error.message);
      return 2200;
    }
  }

  async getTokens() {
    try {
      const response = await axios.get('https://api.coingecko.com/api/v3/coins/markets', {
        params: {
          vs_currency: 'usd',
          order: 'market_cap_desc',
          per_page: 100,
          page: 1
        }
      });
      return response.data;
    } catch (error) {
      console.error('Coingecko tokens failed:', error.message);
      return [];
    }
  }

  async checkToken(token, ethPrice) {
    try {
      // Get price on Uniswap V2
      const uniV2Price = await this.getUniswapV2Price(token.id);
      
      if (uniV2Price > 0 && uniV2Price < token.current_price * 1.01) {
        const profitPercent = ((token.current_price - uniV2Price) / uniV2Price) * 100;
        
        if (profitPercent > MIN_PROFIT) {
          console.log(`\n💎 ARBITRAGE: ${token.symbol}`);
          console.log(`   Buy: $${uniV2Price.toFixed(4)}`);
          console.log(`   Sell: $${token.current_price.toFixed(4)}`);
          console.log(`   Profit: ${profitPercent.toFixed(2)}%`);
          
          await this.executeTrade(token, 'Uniswap V2', uniV2Price);
        }
      }
    } catch (error) {
      // Silent fail for individual tokens
    }
  }

  async getUniswapV2Price(tokenId) {
    try {
      // Use Coingecko's token pair API
      const response = await axios.get(`https://api.coingecko.com/api/v3/coins/ethereum/contract/${tokenId}?localization=false&tickers=true&community_data=false&developer_data=false`);
      const price = response.data.market_data.current_price.usd;
      return price || 0;
    } catch (error) {
      return 0;
    }
  }

  async executeTrade(token, dex, buyPrice) {
    try {
      const router = DEX_ROUTERS.UNISWAP_V2;
      const swapInterface = new ethers.Interface([
        'function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable returns (uint[] memory amounts)'
      ]);

      console.log(`🤖 Buying ${token.symbol} on Uniswap V2...`);

      const tx = await this.wallet.sendTransaction({
        to: router,
        data: swapInterface.encodeFunctionData('swapExactETHForTokens', [
          0,
          [WETH_CONTRACT, token.id.substring(0, 42)],
          this.wallet.address,
          Math.floor(Date.now() / 1000) + 300
        ]),
        value: TRADE_SIZE
      });

      const receipt = await tx.wait();
      console.log(`✅ Buy executed! TX: ${receipt.hash}`);

    } catch (error) {
      console.error('❌ Trade failed:', error.message);
    }
  }
}

async function main() {
  const agent = new ArbitrageAgent();
  await agent.start();
}

main().catch(console.error);
