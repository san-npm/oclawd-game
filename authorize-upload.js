#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Google Drive API credentials from Google Cloud Console
const CLIENT_ID = '870251413533-mdpid0h8fucclfq5saabmu5v0jfeghep.apps.googleusercontent.com';
const CLIENT_SECRET = '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';
const REFRESH_TOKEN = ''; // Will be generated via OAuth

// OAuth authorization URL - using correct v2 endpoint
const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?` +
  `client_id=${CLIENT_ID}` +
  `&redirect_uri=http://localhost` +
  `&response_type=token` +
  `&scope=https://www.googleapis.com/auth/drive.file`;

console.log('🔐 Google Drive OAuth Authorization\n');
console.log('===================================\n');
console.log('1. Open this URL in your browser:');
console.log(`${authUrl}\n`);

console.log('2. You will be redirected to a page with a "token" in the URL\n');
console.log('3. Copy that "access_token" value\n');
console.log('4. Paste it below when prompted\n');

async function getAccessToken() {
  const tokenResponse = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      client_id: CLIENT_ID,
      client_secret: CLIENT_SECRET,
      refresh_token: REFRESH_TOKEN,
      grant_type: 'refresh_token'
    })
  });

  const data = await tokenResponse.json();
  if (data.error) {
    throw new Error(`Failed to get access token: ${data.error}`);
  }
  return data.access_token;
}

async function uploadToDrive(filePath, accessToken) {
  const fileName = path.basename(filePath);
  const content = fs.readFileSync(filePath, 'utf8');
  const mimeType = filePath.endsWith('.md') ? 'text/markdown' : 'text/plain';

  console.log(`📄 Uploading ${fileName} to Google Drive...`);

  // First create the file
  const createResponse = await fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: fileName,
      mimeType: mimeType,
      parents: ['root']
    })
  });

  if (!createResponse.ok) {
    throw new Error(`Failed to create file: ${createResponse.status} ${createResponse.statusText}`);
  }

  const fileData = await createResponse.json();
  const fileId = fileData.id;
  const uploadUrl = fileData.webContentLink;

  // Now upload content
  const uploadContentResponse = await fetch(uploadUrl, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': mimeType,
      'Content-Length': content.length.toString()
    },
    body: content
  });

  if (!uploadContentResponse.ok) {
    throw new Error(`Failed to upload content: ${uploadContentResponse.status} ${uploadContentResponse.statusText}`);
  }

  console.log(`✅ Uploaded: ${fileName} (ID: ${fileId})\n`);
  return fileId;
}

async function main() {
  console.log('🦀 Clawdberg Google Drive Uploader\n');
  console.log('================================\n');

  const files = [
    'aleph-cloud-marketing-analysis.md',
    'aleph-cloud-seo-analysis.md',
    'space-strategy-game/README.md',
    'space-strategy-game/PROGRESS.md',
    'space-strategy-game/SETUP_SUMMARY.md',
    'space-strategy-game/PROJECT_COORDINATION.md',
    'space-strategy-game/docs/ARCHITECTURE.md',
    'space-strategy-game/docs/ECONOMY.md',
    'space-strategy-game/docs/TASKS.md'
  ];

  // Prompt for access token
  console.log('Enter your Google Drive access token:');
  console.log('Copy from the redirect URL after authorizing\n');

  const readline = require('readline');
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const accessToken = await new Promise(resolve => {
    rl.question('Access Token: ', resolve);
    rl.close();
  });

  if (!accessToken) {
    console.error('❌ No access token provided');
    process.exit(1);
  }

  let successCount = 0;

  for (const file of files) {
    const fullPath = path.join('/root/openclaw', file);
    if (!fs.existsSync(fullPath)) {
      console.log(`⚠️  Skipped (not found): ${file}\n`);
      continue;
    }

    try {
      await uploadToDrive(fullPath, accessToken);
      successCount++;
    } catch (error) {
      console.error(`❌ Error uploading ${file}: ${error.message}\n`);
    }
  }

  console.log('================================');
  console.log(`✅ Uploaded ${successCount}/${files.length} files\n`);
}

main();
