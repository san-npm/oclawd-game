#!/usr/bin/env node

/**
 * Simple Gmail IMAP Helper
 */

const Imap = require('imap');
const { simpleParser } = require('mailparser');
const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');

const CONFIG_PATH = path.join(process.env.HOME || process.env.USERPROFILE || require('os').homedir(), '.openclaw', 'gmail-imap-config.json');

class GmailIMAPSimple {
  constructor() {
    this.imap = null;
    this.transporter = null;
    this.config = this.loadConfig();
  }

  loadConfig() {
    if (fs.existsSync(CONFIG_PATH)) {
      return JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
    }
    return null;
  }

  async connectIMAP() {
    return new Promise((resolve, reject) => {
      this.imap = new Imap({
        user: this.config.email,
        password: this.config.appPassword,
        host: 'imap.gmail.com',
        port: 993,
        tls: true,
        tlsOptions: { rejectUnauthorized: false }
      });

      this.imap.once('ready', () => {
        console.log('✅ Connected to Gmail IMAP');
        resolve();
      });

      this.imap.once('error', (err) => {
        console.error('❌ IMAP connection error:', err.message);
        reject(err);
      });

      this.imap.connect();
    });
  }

  async setupSMTP() {
    this.transporter = nodemailer.createTransport({
      host: 'smtp.gmail.com',
      port: 587,
      secure: false,
      auth: {
        user: this.config.email,
        pass: this.config.appPassword
      },
      tls: { rejectUnauthorized: false }
    });
    console.log('✅ SMTP configured');
  }

  async listMessages(count = 10) {
    return new Promise((resolve, reject) => {
      this.imap.openBox('INBOX', false, (err, box) => {
        if (err) return reject(err);

        console.log(`📬 Total messages in INBOX: ${box.messages.total}`);

        if (box.messages.total === 0) {
          console.log('📭 Inbox is empty');
          resolve([]);
          return;
        }

        // Fetch the most recent messages
        const startSeq = Math.max(1, box.messages.total - count + 1);
        console.log(`Fetching messages ${startSeq}:${box.messages.total}`);

        const fetch = this.imap.seq.fetch(`${startSeq}:*`, {
          bodies: '',
          struct: true
        });

        const messages = [];

        fetch.on('message', (msg, seqno) => {
          console.log(`Processing message ${seqno}`);
          let buffer = '';

          msg.on('body', (stream) => {
            stream.on('data', (chunk) => buffer += chunk.toString('utf8'));
          });

          msg.once('end', () => {
            console.log(`Message ${seqno} end event, buffer length: ${buffer.length}`);
            if (!buffer || buffer.length < 10) {
              console.log(`Skipping message ${seqno} - no data`);
              return;
            }
            simpleParser(buffer).then(parsed => {
              messages.push({
                seqno,
                from: parsed.from?.text || 'Unknown',
                subject: parsed.subject || 'No Subject',
                date: parsed.date || 'Unknown',
                text: parsed.text?.substring(0, 100) || ''
              });
              console.log(`Successfully parsed message ${seqno}`);
            }).catch(e => {
              console.error(`Parse error for message ${seqno}:`, e.message);
            });
          });
        });

        fetch.once('error', reject);
        fetch.once('end', () => {
          // Wait a bit for async parsing to complete
          setTimeout(() => {
            console.log(`📬 Found ${messages.length} messages`);
            messages.reverse().slice(0, count).forEach((msg, idx) => {
              console.log(`\n${idx + 1}. From: ${msg.from}`);
              console.log(`   Subject: ${msg.subject}`);
              console.log(`   Date: ${msg.date}`);
            });
            resolve(messages);
          }, 500);
        });
      });
    });
  }

  async sendMessage(to, subject, body) {
    try {
      const info = await this.transporter.sendMail({
        from: this.config.email,
        to: to,
        subject: subject,
        text: body
      });

      console.log('✅ Email sent successfully!');
      console.log(`📬 Message ID: ${info.messageId}`);
      return info;
    } catch (error) {
      console.error('❌ Error sending email:', error.message);
      throw error;
    }
  }

  async disconnect() {
    if (this.imap) {
      this.imap.end();
    }
  }
}

// CLI Interface
if (require.main === module) {
  const args = process.argv.slice(2);
  const command = args[0];

  const helper = new GmailIMAPSimple();

  (async () => {
    if (!helper.config) {
      console.log('❌ Gmail IMAP config not found. Run setup first.');
      process.exit(1);
    }

    try {
      await helper.connectIMAP();
      await helper.setupSMTP();

      switch (command) {
        case 'list':
          await helper.listMessages(parseInt(args[1]) || 10);
          break;

        case 'send':
          await helper.sendMessage(args[1], args[2], args.slice(3).join(' '));
          break;

        default:
          console.log('📧 Gmail IMAP Helper');
          console.log('');
          console.log('Commands:');
          console.log('  list [count]   - List recent messages');
          console.log('  send <to> <subject> <body> - Send email');
      }

      await helper.disconnect();
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  })();
}

module.exports = GmailIMAPSimple;
