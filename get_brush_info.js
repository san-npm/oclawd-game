const { ethers } = require('ethers');

const WALLET_ADDRESS = '0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB';
const BRUSH_CONTRACT = '0x4438BC886A3C39d1968DE3304B7111A20e599FC8';
const PROVIDER_URL = 'https://base.publicnode.com';

async function main() {
  const provider = new ethers.JsonRpcProvider(PROVIDER_URL);
  const contract = new ethers.Contract(BRUSH_CONTRACT, [
    'function totalSupply() view returns (uint256)',
    'function ownerOf(uint256 tokenId) view returns (address)',
    'function balanceOf(address owner) view returns (uint256)',
    'function tokenOfOwnerByIndex(address owner, uint256 index) view returns (uint256)',
    'function strengths(uint256 tokenId) view returns (uint256)'
  ], provider);
  
  console.log('Total supply:', (await contract.totalSupply()).toString());
  console.log('Owner balance:', (await contract.balanceOf(WALLET_ADDRESS)).toString());
  
  const balance = parseInt(await contract.balanceOf(WALLET_ADDRESS));
  for (let i = 0; i < balance; i++) {
    const tokenId = await contract.tokenOfOwnerByIndex(WALLET_ADDRESS, BigInt(i));
    const strength = await contract.strengths(tokenId);
    console.log(`Token ${tokenId.toString()} - Strength: ${strength.toString()}`);
  }
}

main().catch(console.error);
