# Oclawd Space Strategy Game

A decentralized space strategy game built on the Base blockchain.

## Features

- **Blockchain-powered**: All game assets and logic on Base network
- **Strategic gameplay**: Build your empire, conquer territories, dominate the galaxy
- **NFT assets**: Unique space assets minted as NFTs
- **Economic system**: Tokenized economy with rewards and incentives
- **Multiplayer**: Competitive play against other players

## Architecture

```
oclawd-space-strategy/
├── contracts/          # Smart contracts (Solidity)
├── frontend/          # React/Next.js UI
├── backend/           # Node.js API server
├── docs/              # Architecture docs
└── scripts/           # Deployment scripts
```

## Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn
- MetaMask or Web3 wallet
- Base testnet RPC URL

### Setup

1. Install dependencies:
```bash
npm install
```

2. Deploy contracts to Base testnet:
```bash
npm run deploy:testnet
```

3. Start development server:
```bash
npm run dev:frontend  # Frontend
npm run dev:backend   # Backend
```

## Smart Contracts

- **GameController**: Main game logic and state management
- **AssetNFT**: Non-fungible token for unique game assets
- **EconomyToken**: Governance and reward token
- **TerritoryManager**: Land and territory management
- **BattleSystem**: Combat and conquest mechanics

## Base Testnet Deployment

The game is pre-configured for Base Sepolia testnet:
- **RPC URL**: https://sepolia.base.org
- **Chain ID**: 84532
- **Explorer**: https://sepolia.basescan.org

## Game Features

### Resource Management
- Mine resources (Energy, Materials, Data)
- Upgrade infrastructure
- Optimize production

### Territory Control
- Claim and expand territory
- Build defensive structures
- Attack enemy territories

### Fleet Building
- Construct space fleets
- Customize ship classes
- Upgrade fleet capabilities

### Trading & Economy
- Trade resources with other players
- Participate in marketplaces
- Earn rewards for achievements

## Development

### Frontend
- React 18 with TypeScript
- Next.js for routing
- Web3.js for blockchain interactions
- Tailwind CSS for styling

### Backend
- Node.js with Express
- TypeORM for database
- Web3.js integration
- REST API endpoints

### Smart Contracts
- Solidity 0.8+
- Hardhat for development
- OpenZeppelin libraries
- Gas-optimized implementations

## Deployment to Mainnet

⚠️ **Warning**: This is a hackathon project. Always test thoroughly on testnet before mainnet deployment.

1. Update environment variables with mainnet RPC URLs
2. Deploy contracts to Base mainnet
3. Configure frontend with mainnet addresses
4. Test all functionality
5. Deploy to production

## Contributing

This project is built for the [Oclawd Hackathon 2026](https://hackathon.oclawd.com)

## License

MIT License - feel free to use and modify

## Contact

For questions or support, join the Oclawd Discord community.

---

**Built for Oclawd Space Strategy Hackathon**
