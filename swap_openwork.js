import { createWalletClient, createPublicClient, http } from 'viem';
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

// For now, let's just check balances
async function checkBalances() {
  const ethBalance = await publicClient.getBalance({ address: MY_ADDRESS });
  console.log(`ETH Balance: ${ethBalance} wei (${Number(ethBalance) / 1e18} ETH)`);

  // ERC20 balance check would require contract calls
  // Let's start simple and just verify we can connect
  console.log(`Address: ${account.address}`);
  console.log(`Chain: ${base.name}`);
}

checkBalances().catch(console.error);
