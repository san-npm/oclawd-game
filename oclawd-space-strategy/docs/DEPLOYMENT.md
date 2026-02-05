# Deployment Guide

## Base Testnet Setup

### Prerequisites

1. **Node.js 18+**: 
```bash
node --version
npm --version
```

2. **MetaMask Wallet**:
   - Install MetaMask browser extension
   - Add Base Sepolia testnet
   - Obtain test ETH from Base Sepolia faucet

3. **Environment Variables**:
   - Base Sepolia RPC URL
   - Private key (for contracts)
   - Gas price estimates

### Environment Configuration

Create `.env` file in each directory:

**Root `.env`**:
```bash
# Base Sepolia Testnet
BASE_SEPOLIA_RPC_URL=https://sepolia.base.org
BASE_SEPOLIA_CHAIN_ID=84532
BASE_SEPOLIA_EXPLORER=https://sepolia.basescan.org

# Development
NEXT_PUBLIC_API_URL=http://localhost:3001

# Wallet (for deployments)
PRIVATE_KEY=your_private_key_here
```

**Backend `.env`**:
```bash
PORT=3001
DATABASE_URL=postgresql://user:password@localhost:5432/oclawd_game
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_jwt_secret
ETHEREUM_PROVIDER=https://sepolia.base.org

# Contract addresses (after deployment)
CONTRACT_GAME_CONTROLLER=
CONTRACT_ASSET_NFT=
CONTRACT_ECONOMY_TOKEN=
CONTRACT_TERRITORY_MANAGER=
CONTRACT_BATTLE_SYSTEM=
```

**Frontend `.env`**:
```bash
NEXT_PUBLIC_API_URL=http://localhost:3001

# Contract addresses
NEXT_PUBLIC_CONTRACT_GAME_CONTROLLER=
NEXT_PUBLIC_CONTRACT_ASSET_NFT=
NEXT_PUBLIC_CONTRACT_ECONOMY_TOKEN=
NEXT_PUBLIC_CONTRACT_TERRITORY_MANAGER=
NEXT_PUBLIC_CONTRACT_BATTLE_SYSTEM=
```

## Contract Deployment

### 1. Install Dependencies

```bash
cd contracts
npm install
```

### 2. Configure Hardhat

Edit `hardhat.config.js`:
```javascript
require("@nomicfoundation/hardhat-toolbox");
require("@nomicfoundation/hardhat-ethers");
require("@openzeppelin/hardhat-upgrades");

const BASE_SEPOLIA_URL = process.env.BASE_SEPOLIA_RPC_URL || "https://sepolia.base.org";

module.exports = {
  solidity: "0.8.20",
  networks: {
    base_sepolia: {
      url: BASE_SEPOLIA_URL,
      chainId: 84532,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      gasPrice: 20000000000,
    },
  },
  etherscan: {
    apiKey: process.env.BASESCAN_API_KEY,
    apiKey: process.env.BASESCAN_API_KEY,
  },
};
```

### 3. Deploy Contracts

```bash
# Deploy all contracts to Base Sepolia
npx hardhat run scripts/deploy.js --network base_sepolia

# Or deploy individually
npx hardhat run scripts/deploy/GameController.js --network base_sepolia
npx hardhat run scripts/deploy/AssetNFT.js --network base_sepolia
```

### 4. Verify Contracts

```bash
# Verify on BaseScan
npx hardhat verify --network base_sepolia \
  CONTRACT_ADDRESS \
  "ConstructorArg1" \
  "ConstructorArg2"
```

### 5. Update Environment Variables

Copy the deployed contract addresses from the deployment logs and update `.env` files.

## Backend Deployment

### 1. Install Dependencies

```bash
cd backend
npm install
```

### 2. Database Setup

```bash
# Create PostgreSQL database
createdb oclawd_game

# Run migrations
npm run migrate

# Seed initial data (optional)
npm run seed
```

### 3. Start Backend

```bash
# Development mode
npm run dev

# Production mode
npm run start
```

### 4. Test API

```bash
# Health check
curl http://localhost:3001/health

# Contract addresses
curl http://localhost:3001/api/contracts
```

## Frontend Deployment

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Build for Production

```bash
npm run build
```

### 3. Start Server

```bash
npm start
```

### 4. Deploy to Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

## Base Mainnet Deployment (Warning)

⚠️ **ONLY FOR PRODUCTION USE - HIGH RISK**

### Prerequisites

1. Base mainnet RPC access
2. Sufficient ETH for gas
3. Verified contracts
4. Security audit
5. Team approval

### 1. Update Environment Variables

Use mainnet RPC URLs and addresses.

### 2. Update Contract Addresses

Replace all Base Sepolia addresses with mainnet addresses.

### 3. Deploy to Mainnet

```bash
cd contracts
npx hardhat run scripts/deploy.js --network base_mainnet
```

### 4. Verify on BaseScan

```bash
npx hardhat verify --network base_mainnet \
  CONTRACT_ADDRESS \
  "ConstructorArg1" \
  "ConstructorArg2"
```

### 5. Update Frontend

Deploy updated frontend and update contract addresses.

### 6. Test Thoroughly

Run full test suite on mainnet.

## CI/CD Pipeline

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Base Sepolia

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install Dependencies
        run: |
          cd contracts && npm install
          cd ../backend && npm install
          cd ../frontend && npm install
          
      - name: Deploy Contracts
        env:
          PRIVATE_KEY: ${{ secrets.PRIVATE_KEY }}
          BASE_SEPOLIA_RPC_URL: https://sepolia.base.org
        run: |
          cd contracts
          npx hardhat run scripts/deploy.js --network base_sepolia
          
      - name: Update Environment
        run: |
          # Update contract addresses in .env files
          
      - name: Deploy Backend
        run: |
          cd backend
          npm run build
          npm start &
          
      - name: Deploy Frontend
        run: |
          cd frontend
          npm run build
          npm start
```

## Monitoring

### Smart Contract Monitoring

```bash
# Watch for events
npx hardhat watch --network base_sepolia --logs
```

### Backend Monitoring

```bash
# Logs
tail -f logs/app.log

# Metrics
npm run monitor
```

### Frontend Monitoring

```bash
# Browser console logs
# Check network requests
# Monitor MetaMask transactions
```

## Troubleshooting

### Contract Deployment Fails

1. Check RPC URL connectivity
2. Verify gas price
3. Check account balance
4. Verify contract code syntax

### API Errors

1. Check backend logs
2. Verify database connection
3. Check contract addresses
4. Review API documentation

### Frontend Issues

1. Check console for errors
2. Verify API URL
3. Check contract address configuration
4. Review deployment logs

## Security Checklist

- [ ] Private keys stored in secrets
- [ ] Environment variables not committed
- [ ] Contracts audited
- [ ] API rate limiting enabled
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] HTTPS enforced
- [ ] CORS properly configured
- [ ] Input validation complete
- [ ] Error handling robust
- [ ] Database backups configured
- [ ] Monitoring and alerts set up

## Rollback Procedure

### Contract Rollback

```bash
# Use multi-sig for governance if needed
# Consider implementation changes only
```

### Database Rollback

```bash
# Restore from backup
pg_restore database.dump
```

### Frontend Rollback

```bash
git revert <commit-hash>
vercel rollback
```

---

**Last Updated**: February 2026
**Version**: 1.0.0
