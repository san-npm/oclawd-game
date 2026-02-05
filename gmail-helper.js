#!/usr/bin/env node

/**
 * Gmail Helper for OpenClaw
 * Provides email reading and sending capabilities
 */

const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');
const os = require('os');

// Configuration
const CREDENTIALS_PATH = path.join(process.env.HOME || process.env.USERPROFILE || os.homedir(), '.openclaw', 'gmail-credentials.json');
const TOKEN_PATH = path.join(process.env.HOME || process.env.USERPROFILE || os.homedir(), '.openclaw', 'gmail-token.json');

class GmailHelper {
  constructor() {
    this.gmail = null;
    this.oAuth2Client = null;
  }

  async initialize() {
    // Load credentials
    if (!fs.existsSync(CREDENTIALS_PATH)) {
      console.error('❌ Gmail credentials not found. Please set up OAuth2 first.');
      console.log('📝 To set up Gmail access:');
      console.log('1. Go to https://console.cloud.google.com/');
      console.log('2. Create a project and enable Gmail API');
      console.log('3. Create OAuth 2.0 credentials (Desktop application)');
      console.log('4. Download credentials as JSON');
      console.log('5. Save as ~/.openclaw/gmail-credentials.json');
      return false;
    }

    const credentials = JSON.parse(fs.readFileSync(CREDENTIALS_PATH));
    const { client_secret, client_id, redirect_uris } = credentials.installed || credentials.web;

    this.oAuth2Client = new google.auth.OAuth2(
      client_id,
      client_secret,
      redirect_uris[0]
    );

    // Check if we have a stored token
    if (fs.existsSync(TOKEN_PATH)) {
      const token = JSON.parse(fs.readFileSync(TOKEN_PATH));
      this.oAuth2Client.setCredentials(token);
    }

    this.gmail = google.gmail({ version: 'v1', auth: this.oAuth2Client });
    return true;
  }

  async authenticate() {
    if (!this.oAuth2Client) {
      await this.initialize();
    }

    const authUrl = this.oAuth2Client.generateAuthUrl({
      access_type: 'offline',
      scope: ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']
    });

    console.log('🔗 Please authenticate with Gmail:');
    console.log(authUrl);
    console.log('\nCopy the authorization code from the browser and paste it here...');

    // For CLI usage, we'd need to get the code interactively
    // This is a placeholder for the authentication flow
    return authUrl;
  }

  async listMessages(maxResults = 10) {
    try {
      const res = await this.gmail.users.messages.list({
        userId: 'me',
        maxResults: maxResults
      });

      const messages = res.data.messages || [];
      console.log(`📬 Found ${messages.length} recent messages`);

      return messages;
    } catch (error) {
      console.error('❌ Error listing messages:', error.message);
      throw error;
    }
  }

  async getMessage(messageId) {
    try {
      const res = await this.gmail.users.messages.get({
        userId: 'me',
        id: messageId,
        format: 'full'
      });

      const message = res.data;
      const headers = message.payload.headers;
      const subject = headers.find(h => h.name === 'Subject')?.value || 'No Subject';
      const from = headers.find(h => h.name === 'From')?.value || 'Unknown';
      const date = headers.find(h => h.name === 'Date')?.value || '';

      console.log(`📧 From: ${from}`);
      console.log(`📋 Subject: ${subject}`);
      console.log(`📅 Date: ${date}`);

      // Extract body (simplified)
      let body = '';
      if (message.payload.body?.data) {
        body = Buffer.from(message.payload.body.data, 'base64').toString();
      }

      return { subject, from, date, body };
    } catch (error) {
      console.error('❌ Error getting message:', error.message);
      throw error;
    }
  }

  async sendMessage(to, subject, body) {
    try {
      const email = [
        `To: ${to}`,
        `Subject: ${subject}`,
        '',
        body
      ].join('\r\n');

      const encodedEmail = Buffer.from(email).toString('base64');
      const encodedEmailSafe = encodedEmail.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');

      const res = await this.gmail.users.messages.send({
        userId: 'me',
        resource: {
          raw: encodedEmailSafe
        }
      });

      console.log('✅ Email sent successfully!');
      console.log(`📬 Message ID: ${res.data.id}`);

      return res.data;
    } catch (error) {
      console.error('❌ Error sending message:', error.message);
      throw error;
    }
  }

  async searchMessages(query) {
    try {
      const res = await this.gmail.users.messages.list({
        userId: 'me',
        q: query
      });

      const messages = res.data.messages || [];
      console.log(`🔍 Found ${messages.length} messages matching "${query}"`);

      return messages;
    } catch (error) {
      console.error('❌ Error searching messages:', error.message);
      throw error;
    }
  }
}

// CLI Interface
if (require.main === module) {
  const args = process.argv.slice(2);
  const command = args[0];

  const helper = new GmailHelper();

  (async () => {
    const initialized = await helper.initialize();
    if (!initialized) {
      process.exit(1);
    }

    switch (command) {
      case 'list':
        await helper.listMessages(parseInt(args[1]) || 10);
        break;

      case 'get':
        await helper.getMessage(args[1]);
        break;

      case 'send':
        await helper.sendMessage(args[1], args[2], args.slice(3).join(' '));
        break;

      case 'search':
        await helper.searchMessages(args[1]);
        break;

      case 'auth':
        await helper.authenticate();
        break;

      default:
        console.log('📧 Gmail Helper');
        console.log('');
        console.log('Commands:');
        console.log('  auth           - Get authentication URL');
        console.log('  list [count]   - List recent messages');
        console.log('  get <id>       - Get message details');
        console.log('  search <query> - Search messages');
        console.log('  send <to> <subject> <body> - Send email');
    }
  })();
}

module.exports = GmailHelper;
