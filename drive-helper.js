const fs = require('fs');
const path = require('path');

// Load Google Drive credentials from config
const configPath = path.join('/root/openclaw', 'gmail-imap-config.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

const CLIENT_ID = config.clientId;
const CLIENT_SECRET = config.clientSecret;
const REFRESH_TOKEN = config.refreshToken;
const REDIRECT_URI = 'http://localhost/callback';

// Google Drive API endpoint
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
  return data.access_token;
}

async function uploadFile(fileName, content, mimeType = 'text/markdown') {
  const accessToken = await getAccessToken();

  // First, check if file exists
  const searchResponse = await fetch(
    `https://www.googleapis.com/drive/v3/files?q=name='${fileName}' and mimeType='${mimeType}'`,
    {
      headers: { 'Authorization': `Bearer ${accessToken}` }
    }
  );

  let fileId = null;
  const searchData = await searchResponse.json();

  if (searchData.files && searchData.files.length > 0) {
    fileId = searchData.files[0].id;
  }

  const body = JSON.stringify({
    name: fileName,
    mimeType: mimeType,
    parents: ['root'] // Upload to root folder
  });

  const headers = {
    'Authorization': `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  };

  const uploadResponse = await fetch(
    `https://www.googleapis.com/upload/drive/v3/files${fileId ? `/${fileId}` : ''}?uploadType=multipart`,
    {
      method: fileId ? 'PATCH' : 'POST',
      headers,
      body: JSON.stringify({
        name: fileName,
        mimeType: mimeType,
        parents: ['root']
      }),
      body: JSON.stringify(body)
    }
  );

  return fileId;
}

async function listFiles() {
  const accessToken = await getAccessToken();

  const response = await fetch('https://www.googleapis.com/drive/v3/files', {
    headers: { 'Authorization': `Bearer ${accessToken}` },
    params: { q: "mimeType='text/markdown' or mimeType='application/pdf'" }
  });

  const data = await response.json();
  return data.files || [];
}

module.exports = {
  uploadFile,
  listFiles,
  getAccessToken
};
