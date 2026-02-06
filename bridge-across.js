const { Wallet, JsonRpcProvider, Contract, parseEther, formatEther } = require('ethers');

async function bridgeViaAcross() {
  const privateKey = process.env.PRIVATE_KEY;
  const provider = new JsonRpcProvider('https://mainnet.base.org');
  const wallet = new Wallet(privateKey, provider);
  
  console.log('Wallet:', wallet.address);
  const balance = await provider.getBalance(wallet.address);
  console.log('Base ETH:', formatEther(balance));
  
  // Amount to bridge (0.001 ETH)
  const amount = parseEther('0.001');
  
  // Get quote from Across API
  console.log('\\nGetting bridge quote...');
  const quoteUrl = `https://across.to/api/suggested-fees?originChainId=8453&destinationChainId=10&token=0x4200000000000000000000000000000000000006&amount=${amount.toString()}`;
  
  const response = await fetch(quoteUrl);
  const quote = await response.json();
  
  console.log('Output amount:', formatEther(quote.outputAmount), 'ETH on Optimism');
  console.log('Fill time:', quote.estimatedFillTimeSec, 'seconds');
  
  // Across SpokePool V3 ABI (depositV3 for native ETH)
  const SPOKE_POOL_ABI = [
    'function depositV3(address depositor, address recipient, address inputToken, address outputToken, uint256 inputAmount, uint256 outputAmount, uint256 destinationChainId, address exclusiveRelayer, uint32 quoteTimestamp, uint32 fillDeadline, uint32 exclusivityDeadline, bytes calldata message) external payable'
  ];
  
  const spokePool = new Contract(quote.spokePoolAddress, SPOKE_POOL_ABI, wallet);
  
  const WETH = '0x4200000000000000000000000000000000000006';
  const fillDeadline = parseInt(quote.fillDeadline);
  const timestamp = parseInt(quote.timestamp);
  const exclusivityDeadline = timestamp + quote.exclusivityDeadline;
  
  console.log('\\nSending bridge transaction...');
  
  const tx = await spokePool.depositV3(
    wallet.address,                    // depositor
    wallet.address,                    // recipient  
    WETH,                              // inputToken (WETH on Base)
    WETH,                              // outputToken (WETH on Optimism)
    amount,                            // inputAmount
    quote.outputAmount,                // outputAmount
    10,                                // destinationChainId (Optimism)
    quote.exclusiveRelayer,            // exclusiveRelayer
    timestamp,                         // quoteTimestamp
    fillDeadline,                      // fillDeadline
    exclusivityDeadline,               // exclusivityDeadline
    '0x',                              // message
    { value: amount, gasLimit: 150000 }
  );
  
  console.log('TX hash:', tx.hash);
  console.log('Waiting for confirmation...');
  
  const receipt = await tx.wait();
  console.log('Confirmed! Block:', receipt.blockNumber);
  console.log('\\n✅ Bridge initiated! ETH will arrive on Optimism in ~2-10 minutes.');
  console.log('Track at: https://across.to/transactions?searchText=' + tx.hash);
}

bridgeViaAcross().catch(e => {
  console.error('Error:', e.message);
  if (e.data) console.error('Data:', e.data);
});
