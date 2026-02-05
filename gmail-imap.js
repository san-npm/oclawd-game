#!/usr/bin/env node

/**
 * Gmail IMAP Helper for OpenClaw
 * Uses IMAP for reading emails and SMTP for sending
 */

const Imap = require('imap');
const { simpleParser } = require('mailparser');
const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');

const CONFIG_PATH = path.join(process.env.HOME || process.env.USERPROFILE || require('os').homedir(), '.openclaw', 'gmail-imap-config.json');

class GmailIMAP {
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

  saveConfig(config) {
    fs.writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2));
  }

  async connectIMAP() {
    return new Promise((resolve, reject) => {
      this.imap = new Imap({
        user: this.config.email,
        password: this.config.appPassword,
        host: 'imap.gmail.com',
        port: 993,
        tls: true,
        tlsOptions: {
          rejectUnauthorized: false,
          servername: 'imap.gmail.com'
        }
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
      tls: {
        rejectUnauthorized: false
      }
    });
    console.log('✅ SMTP configured');
  }

  async listMessages(count = 10) {
    return new Promise((resolve, reject) => {
      this.imap.openBox('INBOX', false, (err, box) => {
        if (err) return reject(err);

        const searchCriteria = ['1:*'];
        const fetchOptions = {
          bodies: '',
          markSeen: false,
          struct: true
        };

        this.imap.search(searchCriteria, (err, results) => {
          if (err) return reject(err);

          const messages = results.slice(-count).reverse();
          const fetch = this.imap.fetch(messages, fetchOptions);

          const processedMessages = [];

          fetch.on('message', (msg, seqno) => {
            let messageData = '';
            let attributes = null;

            msg.on('body', (stream, info) => {
              stream.on('data', (chunk) => {
                messageData += chunk.toString('utf8');
              });
            });

            msg.on('attributes', (attrs) => {
              attributes = attrs;
            });

            msg.once('end', () => {
              if (attributes && messageData) {
                processedMessages.push({
                  seqno: seqno,
                  uid: attributes.uid,
                  date: attributes.date,
                  flags: attributes.flags,
                  envelope: attributes.envelope,
                  preview: messageData.substring(0, 200)
                });
              }
            });
          });

          fetch.once('error', (err) => {
            reject(err);
          });

          fetch.once('end', () => {
            console.log(`📬 Found ${processedMessages.length} messages`);
            processedMessages.forEach((msg, idx) => {
              console.log(`\n${idx + 1}. From: ${msg.envelope?.from?.[0]?.address || 'Unknown'}`);
              console.log(`   Subject: ${msg.envelope?.subject || 'No Subject'}`);
              console.log(`   Date: ${msg.date}`);
            });
            resolve(processedMessages);
          });
        });
      });
    });
  }

  async getMessage(uid) {
    return new Promise((resolve, reject) => {
      this.imap.openBox('INBOX', false, (err, box) => {
        if (err) return reject(err);

        const fetch = this.imap.fetch([uid], {
          bodies: '',
          struct: true
        });

        fetch.on('message', (msg, seqno) => {
          let messageData = '';

          msg.on('body', (stream, info) => {
            stream.on('data', (chunk) => {
              messageData += chunk.toString('utf8');
            });
          });

          msg.once('end', async () => {
            try {
              const parsed = await simpleParser(messageData);
              console.log(`📧 From: ${parsed.from.text}`);
              console.log(`📋 Subject: ${parsed.subject}`);
              console.log(`📅 Date: ${parsed.date}`);
              console.log(`\n${parsed.text}`);
              resolve(parsed);
            } catch (err) {
              reject(err);
            }
          });
        });

        fetch.once('error', reject);
        fetch.once('end', () => {});
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

  async searchMessages(query) {
    return new Promise((resolve, reject) => {
      this.imap.openBox('INBOX', false, (err, box) => {
        if (err) return reject(err);

        // Simple search - you can extend this
        const searchCriteria = ['SUBJECT', query];
        const fetchOptions = {
          bodies: '',
          markSeen: false,
          struct: true
        };

        this.imap.search(searchCriteria, (err, results) => {
          if (err) return reject(err);

          console.log(`🔍 Found ${results.length} messages matching "${query}"`);

          const fetch = this.imap.fetch(results, fetchOptions);

          const processedMessages = [];

          fetch.on('message', (msg, seqno) => {
            let attributes = null;

            msg.on('attributes', (attrs) => {
              attributes = attrs;
            });

            msg.once('end', () => {
              if (attributes) {
                processedMessages.push({
                  seqno: seqno,
                  uid: attributes.uid,
                  date: attributes.date,
                  envelope: attributes.envelope
                });
              }
            });
          });

          fetch.once('error', reject);
          fetch.once('end', () => {
            resolve(processedMessages);
          });
        });
      });
    });
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

  const helper = new GmailIMAP();

  (async () => {
    // Handle setup command first
    if (command === 'setup' && args.length >= 3) {
      helper.config = {
        email: args[1],
        appPassword: args[2]
      };
      helper.saveConfig(helper.config);
      console.log('✅ Gmail IMAP configured!');
      console.log(`📧 Email: ${helper.config.email}`);
      process.exit(0);
    }

    if (!helper.config) {
      console.log('❌ Gmail IMAP config not found.');
      console.log('📝 To set up Gmail IMAP access:');
      console.log('1. Go to https://myaccount.google.com/apppasswords');
      console.log('2. Generate an app password for Mail');
      console.log('3. Run setup with your email and app password:');
      console.log('   node gmail-imap.js setup <email> <app-password>');
      process.exit(1);
    }

    try {
      await helper.connectIMAP();
      await helper.setupSMTP();

      switch (command) {
        case 'list':
          await helper.listMessages(parseInt(args[1]) || 10);
          break;

        case 'get':
          await helper.getMessage(parseInt(args[1]));
          break;

        case 'send':
          await helper.sendMessage(args[1], args[2], args.slice(3).join(' '));
          break;

        case 'search':
          await helper.searchMessages(args[1]);
          break;

        case 'setup': {
          helper.config = {
            email: args[1],
            appPassword: args[2]
          };
          helper.saveConfig(helper.config);
          console.log('✅ Gmail IMAP configured!');
          console.log(`📧 Email: ${helper.config.email}`);
          break;
        }

        default:
          console.log('📧 Gmail IMAP Helper');
          console.log('');
          console.log('Commands:');
          console.log('  setup <email> <app-password> - Set up IMAP access');
          console.log('  list [count]   - List recent messages');
          console.log('  get <uid>      - Get message details');
          console.log('  search <query> - Search messages');
          console.log('  send <to> <subject> <body> - Send email');
      }

      await helper.disconnect();
    } catch (error) {
      console.error('❌ Error:', error.message);
      process.exit(1);
    }
  })();
}

module.exports = GmailIMAP;
