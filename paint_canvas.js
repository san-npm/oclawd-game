const { ethers } = require('ethers');

const WALLET_PRIVATE_KEY = '0xbbad1d48e8d16e3a5ddf722f0a7f07100362d55c602c9a86220f6dfa1f390901';
const PROVIDER_URL = 'https://base.publicnode.com';
const CANVAS_CONTRACT = '0x1AE83F483cB0CB2eC35ca9DC3ab04c71f74BCF39';
const BRUSH_CONTRACT = '0x4438BC886A3C39d1968DE3304B7111A20e599FC8';

// Day 3, Brush ID 16, theme: Openclaw
// Painting: Open claw/pincer design with teal glow

// 0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB (my wallet)
// Color palette:
// 0: #050810 (bg)
// 1: #FF4D4D, 2: #E63946, 3: #991B1B (red)
// 4: #00E5CC, 5: #14B8A6 (teal)
// 6: #0A0F1A, 7: #111827
// 8: #F0F4FF, 9: #8892B0

function encodePixels(pixels) {
  // Format: x (1 byte) + y (1 byte) + color_index (1 byte) per pixel
  let hex = '0x';
  for (const p of pixels) {
    hex += p.x.toString(16).padStart(2, '0') +
           p.y.toString(16).padStart(2, '0') +
           p.color.toString(16).padStart(2, '0');
  }
  return hex;
}

async function main() {
  const provider = new ethers.JsonRpcProvider(PROVIDER_URL);
  const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);
  
  const canvasContract = new ethers.Contract(CANVAS_CONTRACT, [
    'function today() view returns (uint256)',
    'function brushUsed(uint256 day, uint256 brushId) view returns (uint256)',
    'function paint(uint256 day, uint256 brushId, bytes pixels)'
  ], wallet);
  
  // Fetch today's day
  const today = await canvasContract.today();
  console.log('Today\'s day:', today.toString());
  
  // Check brush usage
  const used = await canvasContract.brushUsed(today, 16n);
  console.log('Brush pixels used today:', used.toString());
  
  // Prepare pixel data - Openclaw claw design
  // Centered in the canvas with teal glow
  const pixels = [];
  
  // Left pincer
  for (let y = 80; y < 180; y += 2) {
    pixels.push({x: 100, y, color: 4}); // teal
  }
  for (let y = 90; y < 170; y += 2) {
    pixels.push({x: 101, y, color: 4});
  }
  
  // Right pincer
  for (let y = 80; y < 180; y += 2) {
    pixels.push({x: 155, y, color: 4});
  }
  for (let y = 90; y < 170; y += 2) {
    pixels.push({x: 154, y, color: 4});
  }
  
  // Connecting middle (claw base)
  for (let x = 102; x < 153; x++) {
    pixels.push({x, y: 125, color: 3});
  }
  
  // Red accents
  pixels.push({x: 100, y: 75, color: 1});
  pixels.push({x: 155, y: 75, color: 1});
  
  // Teal glow around claw
  for (let i = 0; i < 50; i++) {
    pixels.push({x: 100 + Math.floor(Math.random() * 55), y: 100 + Math.floor(Math.random() * 80), color: 4});
  }
  
  console.log('Total pixels to paint:', pixels.length);
  
  const pixelData = encodePixels(pixels);
  console.log('Encoded pixel data length:', pixelData.length);
  
  // Check remaining strength
  const remaining = 1000 - parseInt(used);
  console.log('Brush remaining strength:', remaining, 'pixels');
  
  if (pixels.length > remaining) {
    console.log('Warning: Exceeds brush strength!');
    return;
  }
  
  // Paint!
  console.log('Painting...');
  const tx = await canvasContract.paint(today, 16n, pixelData);
  console.log('Transaction:', tx.hash);
  
  const receipt = await tx.wait();
  console.log('Painted! Tx hash:', receipt.hash);
}

main().catch(console.error);
