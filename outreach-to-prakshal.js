const nodemailer = require('nodemailer');

async function sendEmail() {
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'fermaudclement@gmail.com',
      pass: 'hkhy ryhf mcon cvnw'
    }
  });

  const mailOptions = {
    from: 'fermaudclement@gmail.com',
    to: 'prakshal.jain@gmail.com',
    subject: 'Aleph Cloud - Decentralized VMs for AI Agent Infrastructure',
    html: `
      <p>Hi Prakshal,</p>
      <p>I noticed your work on ClawdBody - looks like an exciting project for AI agent infrastructure.</p>
      <p>I'm reaching out from Aleph Cloud because we specialize in decentralized web3 cloud infrastructure. We offer VMs specifically designed for AI agents like OpenClaw.</p>
      <p><strong>Why we think we're a good fit:</strong></p>
      <ul>
        <li>Decentralized compute for autonomous agents</li>
        <li>Web3-native infrastructure</li>
        <li>Developer-friendly APIs</li>
        <li>Built for the AI agent ecosystem</li>
      </ul>
      <p>If you're building AI agent infrastructure, we'd love to chat about how our cloud could support your projects.</p>
      <p>Feel free to reply here or reach out directly at clement@aleph.cloud.</p>
      <p>Best,<br>Clément<br>CMO @ Aleph Cloud<br><a href="https://aleph.cloud">https://aleph.cloud</a></p>
    `
  };

  try {
    await transporter.sendMail(mailOptions);
    console.log('✅ Email sent successfully!');
  } catch (error) {
    console.error('❌ Error sending email:', error);
  }
}

sendEmail();
