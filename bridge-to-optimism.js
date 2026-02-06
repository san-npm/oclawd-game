const { Wallet, JsonRpcProvider, Contract, parseEther, formatEther } = require('ethers');

// Across Protocol SpokePool on Base
const ACROSS_BASE = '0x09aea4b2242abC8bb4BB78D537A67a245A7bEC64';

// Minimal ABI for Across deposit
const ACROSS_ABI = [
  'function depositV3(address depositor, address recipient, address inputToken, address outputToken, uint256 inputAmount, uint256 outputAmount, uint256 destinationChainId, address exclusiveRelayer, uint32 quoteTimestamp, uint32 fillDeadline, uint32 exclusivityDeadline, bytes message) payable'
];

async function bridgeToOptimism() {
  const privateKey = process.env.PRIVATE_KEY;
  if (!privateKey) {
    console.error('Set PRIVATE_KEY env var');
    process.exit(1);
  }

  const provider = new JsonRpcProvider('https://mainnet.base.org');
  const wallet = new Wallet(privateKey, provider);
  
  console.log('Wallet:', wallet.address);
  
  const balance = await provider.getBalance(wallet.address);
  console.log('Base ETH balance:', formatEther(balance));
  
  // Bridge 0.001 ETH (enough for Farcaster registration)
  const amountToBridge = parseEther('0.001');
  
  if (balance < amountToBridge + parseEther('0.0005')) {
    console.error('Not enough ETH. Need at least 0.0015 ETH for bridge + gas');
    process.exit(1);
  }

  const across = new Contract(ACROSS_BASE, ACROSS_ABI, wallet);
  
  // WETH addresses (ETH is represented as address(0) for input, WETH for output)
  const WETH_BASE = '0x4200000000000000000000000000000000000006';
  const WETH_OPTIMISM = '0x4200000000000000000000000000000000000006';
  const ZERO_ADDRESS = '0x0000000000000000000000000000000000000000';
  
  // Calculate timestamps
  const now = Math.floor(Date.now() / 1000);
  const fillDeadline = now + 7200; // 2 hours
  
  console.log('Bridging', formatEther(amountToBridge), 'ETH from Base to Optimism...');
  
  try {
    const tx = await across.depositV3(
      wallet.address,           // depositor
      wallet.address,           // recipient
      WETH_BASE,               // inputToken (WETH on Base)
      WETH_OPTIMISM,           // outputToken (WETH on Optimism)
      amountToBridge,          // inputAmount
      amountToBridge * 99n / 100n, // outputAmount (1% slippage)
      10,                       // destinationChainId (Optimism)
      ZERO_ADDRESS,            // exclusiveRelayer (none)
      now,                     // quoteTimestamp
      fillDeadline,            // fillDeadline
      0,                       // exclusivityDeadline
      '0x',                    // message (empty)
      { value: amountToBridge, gasLimit: 200000 }
    );
    
    console.log('Transaction sent:', tx.hash);
    console.log('Waiting for confirmation...');
    
    const receipt = await tx.wait();
    console.log('Confirmed in block:', receipt.blockNumber);
    console.log('Bridge initiated! ETH should arrive on Optimism in ~2-10 minutes');
    
  } catch (error) {
    console.error('Bridge failed:', error.message);
    
    // Try alternative: direct native ETH bridge via Across
    console.log('\\nTrying native ETH deposit...');
    
    // Simplified native deposit
    const ACROSS_NATIVE_ABI = [
      'function deposit(address recipient, address originToken, uint256 amount, uint256 destinationChainId, int64 relayerFeePct, uint32 quoteTimestamp) payable'
    ];
    
    const acrossNative = new Contract(ACROSS_BASE, ACROSS_NATIVE_ABI, wallet);
    
    try {
      const tx2 = await acrossNative.deposit(
        wallet.address,
        ZERO_ADDRESS, // Native ETH
        amountToBridge,
        10, // Optimism
        10000000n, // 0.1% relayer fee (in 18 decimals)
        now,
        { value: amountToBridge, gasLimit: 200000 }
      );
      
      console.log('Transaction sent:', tx2.hash);
      await tx2.wait();
      console.log('Bridge initiated!');
    } catch (e2) {
      console.error('Native deposit also failed:', e2.message);
    }
  }
}

bridgeToOptimism().catch(console.error);
