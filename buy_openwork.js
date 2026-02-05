import { createWalletClient, createPublicClient, http, parseUnits, formatUnits } from 'viem';
import { base } from 'viem/chains';
import { privateKeyToAccount } from 'viem/accounts';

const PRIVATE_KEY = '0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901';
const MY_ADDRESS = '0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB';

// Tokens
const WETH = '0x4200000000000000000000000000000000000006'; // WETH on Base
const OPENWORK = '0x299c30DD5974BF4D5bFE42C340CA40462816AB07'; // $OPENWORK on Base
const UNISWAP_V3_ROUTER = '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD'; // Uniswap V3 SwapRouter on Base
const SWAP_ROUTER_02 = '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45'; // Alternative router

const account = privateKeyToAccount(PRIVATE_KEY);

const client = createWalletClient({
  account,
  chain: base,
  transport: http(),
});

const publicClient = createPublicClient({
  chain: base,
  transport: http(),
});

// Uniswap V3 Single Swap Exact Input
const SWAP_SELECTOR = '0x414bf389'; // exactInputSingle(address tokenIn, address tokenOut, uint24 fee, address recipient, uint256 amountIn, uint256 amountOutMinimum, uint160 sqrtPriceLimitX96)

async function swapETHForOPENWORK() {
  console.log('Starting swap...');

  // Amount to swap: 0.001 ETH
  const amountIn = parseUnits('0.001', 18); // 0.001 ETH
  const fee = 3000; // 0.3% standard fee tier
  const amountOutMinimum = 0n; // Accept any amount for now
  const sqrtPriceLimitX96 = 0n; // No price limit

  console.log(`Swapping ${formatUnits(amountIn, 18)} ETH for OPENWORK...`);

  try {
    // Build the calldata for exactInputSingle
    const calldata = SWAP_SELECTOR +
      WETH.slice(2).padStart(64, '0') +
      OPENWORK.slice(2).padStart(64, '0') +
      fee.toString(16).padStart(64, '0') +
      MY_ADDRESS.slice(2).padStart(64, '0') +
      amountIn.toString(16).padStart(64, '0') +
      amountOutMinimum.toString(16).padStart(64, '0') +
      sqrtPriceLimitX96.toString(16).padStart(64, '0');

    // Send ETH to WETH first if needed (on Base, ETH = WETH)
    // For simplicity, we'll just try direct swap - Base handles ETH/WETH automatically

    const hash = await client.sendTransaction({
      to: UNISWAP_V3_ROUTER,
      data: calldata,
      value: amountIn,
    });

    console.log(`Transaction sent: ${hash}`);
    console.log('Waiting for confirmation...');

    const receipt = await publicClient.waitForTransactionReceipt({ hash });
    console.log('Swap complete!');
    console.log(`Gas used: ${receipt.gasUsed.toString()}`);

    return receipt;
  } catch (error) {
    console.error('Swap failed:', error);
    throw error;
  }
}

swapETHForOPENWORK().catch(console.error);
