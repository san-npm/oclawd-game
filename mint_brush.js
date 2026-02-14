const { ethers } = require('ethers');

// Config
const WALLET_PRIVATE_KEY = '0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901';
const PROVIDER_URL = 'https://base.publicnode.com';
const BRUSH_CONTRACT = '0x4438BC886A3C39d1968DE3304B7111A20e599FC8';

async function main() {
  const provider = new ethers.JsonRpcProvider(PROVIDER_URL);
  const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);
  
  const brushContract = new ethers.Contract(BRUSH_CONTRACT, [
    'function mint() payable',
    'function strengths(uint256 tokenId) view returns (uint256)',
    'function ownerOf(uint256 tokenId) view returns (address)'
  ], wallet);
  
  console.log('Connecting to Base...');
  console.log('Wallet:', wallet.address);
  
  // Check balance
  const balance = await provider.getBalance(wallet.address);
  console.log('Wallet balance:', ethers.formatEther(balance), 'ETH');
  
  // Mint brush (0.004 ETH)
  console.log('Minting Brush NFT...');
  const tx = await brushContract.mint({
    value: ethers.parseEther('0.004')
  });
  console.log('Transaction:', tx.hash);
  
  const receipt = await tx.wait();
  console.log('Minted! Tx hash:', receipt.hash);
  
  // Get the minted token ID from Transfer event
  const transferEvent = receipt.logs.find(log => 
    log.topics[0] === '0xddf252ad1be2c89b69c2b068fc378daa952ba7f1132f8e0161297e07485c80'
  );
  
  if (transferEvent) {
    const tokenID = ethers.toBigInt(transferEvent.data);
    console.log('Brush NFT Token ID:', tokenID.toString());
  }
  
  // Check brush strength
  const strength = await brushContract.strengths(0n);
  console.log('Brush strength:', strength.toString(), 'pixels/day');
}

main().catch(console.error);
