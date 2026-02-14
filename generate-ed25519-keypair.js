/**
 * Generate Ed25519 keypair for SelfClaw verification
 *
 * This script generates an Ed25519 keypair in the formats required by SelfClaw:
 * - Public key: SPKI DER format (base64)
 * - Private key: PKCS8 DER format (base64)
 *
 * Usage:
 *   node generate-ed25519-keypair.js
 */

const { generateKeyPairSync } = require('crypto');

console.log('🦎 Generating Ed25519 keypair for SelfClaw verification...\n');

// Generate Ed25519 keypair
const { publicKey, privateKey } = generateKeyPairSync("ed25519");

// Export public key in SPKI DER format (base64) for SelfClaw registration
const publicKeySpki = publicKey.export({ type: "spki", format: "der" }).toString("base64");

// Export private key in PKCS8 DER format (base64) - keep this secure!
const privateKeyPkcs8 = privateKey.export({ type: "pkcs8", format: "der" }).toString("base64");

console.log('✅ Key generated successfully!\n');
console.log('═══════════════════════════════════════════════════════════════');
console.log('PUBLIC KEY (SPKI DER - base64):');
console.log('═══════════════════════════════════════════════════════════════');
console.log(publicKeySpki);
console.log('═══════════════════════════════════════════════════════════════\n');

console.log('═══════════════════════════════════════════════════════════════');
console.log('PRIVATE KEY (PKCS8 DER - base64) - KEEP SECRET!');
console.log('═══════════════════════════════════════════════════════════════');
console.log(privateKeyPkcs8);
console.log('═══════════════════════════════════════════════════════════════\n');

// Save to files for safety
const fs = require('fs');
const path = require('path');

const workspaceDir = '/root/openclaw';
const publicKeyFile = path.join(workspaceDir, 'selfclaw-public-key.txt');
const privateKeyFile = path.join(workspaceDir, 'selfclaw-private-key.txt');

fs.writeFileSync(publicKeyFile, publicKeySpki);
fs.writeFileSync(privateKeyFile, privateKeyPkcs8);

console.log('💾 Keys saved to:');
console.log(`   📄 Public:  ${publicKeyFile}`);
console.log(`   🔐 Private: ${privateKeyFile}\n`);

console.log('📋 Next steps:');
console.log('   1. Copy the PUBLIC KEY above');
console.log('   2. Visit https://selfclaw.ai');
console.log('   3. Enter the public key');
console.log('   4. Add agent name (optional): "Clawdberg"');
console.log('   5. Click "Start Verification"');
console.log('   6. Scan QR code with Self.xyz app\n');

console.log('⚠️  IMPORTANT:');
console.log('   - NEVER share your private key with anyone');
console.log('   - Store it securely (you need it for signing)');
console.log('   - Back it up safely\n');
