import { createWalletClient, createPublicClient, http, parseUnits, encodeFunctionData } from 'viem';
import { base } from 'viem/chains';
import { privateKeyToAccount } from 'viem/accounts';

const PRIVATE_KEY = '0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901';
const MY_ADDRESS = '0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB';

// Tokens
const WETH = '0x4200000000000000000000000000000000000006'; // WETH on Base
const OPENWORK = '0x299c30DD5974BF4D5bFE42C340CA40462816AB07'; // $OPENWORK on Base
const UNISWAP_V3_ROUTER = '0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD'; // Uniswap V3 SwapRouter on Base

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

async function swapETHForOPENWORK() {
  console.log('Starting swap...');

  const amountIn = parseUnits('0.001', 18); // 0.001 ETH
  const fee = 3000; // 0.3% standard fee tier

  console.log(`Swapping 0.001 ETH for OPENWORK...`);

  try {
    // Use encodeFunctionData from viem for exactInputSingle
    const data = encodeFunctionData({
      abi: [{
        name: 'exactInputSingle',
        type: 'function',
        stateMutability: 'payable',
        inputs: [{
            name: 'params',
            type: 'tuple(address tokenIn, address tokenOut, uint24 fee, address recipient, uint256 deadline, uint256 amountIn, uint256 amountOutMinimum, uint160 sqrtPriceLimitX96)'
        }]
      }],
      functionName: 'exactInputSingle',
      args: [{
        tokenIn: WETH,
        tokenOut: OPENWORK,
        fee: fee,
        recipient: MY_ADDRESS,
        deadline: Math.floor(Date.now() / 1000) + 3600, // 1 hour from now
        amountIn: amountIn,
        amountOutMinimum: 0n,
        sqrtPriceLimitX96: 0n
      }]
    });

    console.log('Encoded data:', data);

    const hash = await client.sendTransaction({
      to: UNISWAP_V3_ROUTER,
      data: data,
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
