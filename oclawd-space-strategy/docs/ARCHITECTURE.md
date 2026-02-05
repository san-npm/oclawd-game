# Architecture Documentation

## Overview

Oclawd Space Strategy is a blockchain-powered game built on the Base layer-2 scaling solution. The architecture follows a modular approach with clear separation between frontend, backend, and smart contracts.

## System Architecture

### High-Level Components

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend Layer                           │
│  (React/Next.js + TypeScript + Web3.js)                     │
└────────────┬────────────────────────────────────────────────┘
             │ HTTP/WebSockets
             ▼
┌─────────────────────────────────────────────────────────────┐
│                   Backend Layer                              │
│  (Node.js + Express + TypeORM + Web3.js)                    │
└────┬──────────────┬──────────────┬──────────────┬───────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ DB      │  │ Web3    │  │ Queue   │  │ Cache   │
│ PostgreSQL│ │ Node    │  │ Redis   │  │ Memcached│
└────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘
     │             │             │             │
     └─────────────┴─────────────┴─────────────┘
                   │
             ┌─────▼─────┐
             │ Base RPC  │
             └───────────┘
```

## Smart Contract Architecture

### Contract Hierarchy

```
┌─────────────────────────────────────┐
│        GameController (Main)         │
│  - Game state management             │
│  - Player session handling           │
│  - Global game configuration         │
└─────────────────┬───────────────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ AssetNFT │ │Economy   │ │Territory │
│          │ │ Token    │ │ Manager  │
└────┬─────┘ └────┬─────┘ └────┬─────┘
     │            │            │
     ▼            ▼            ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ FleetNFT │ │Battle    │ │ Trade    │
│          │ │ System   │ │ Market   │
└──────────┘ └──────────┘ └──────────┘
```

### Smart Contract Details

#### GameController
- **Purpose**: Central game orchestration
- **Key Functions**:
  - `createPlayer(address)`: Initialize player account
  - `startGame(address)`: Begin game session
  - `updateGameState(uint8)`: Update game state
- **Events**:
  - `PlayerCreated`
  - `GameStarted`
  - `StateUpdated`

#### AssetNFT
- **Purpose**: Unique in-game assets as NFTs
- **Features**:
  - ERC-721 compliant
  - Tiered rarity system
  - Metadata on-chain
- **Asset Types**:
  - Buildings
  - Spaceships
  - Resources
  - Upgrades

#### EconomyToken
- **Purpose**: In-game currency and governance
- **Features**:
  - ERC-20 compliant
  - Deflationary mechanics
  - Staking and rewards
- **Tokenomics**:
  - Initial supply: 1,000,000,000
  - Inflation rate: 5% annually
  - Reward distribution: 70% for players

#### TerritoryManager
- **Purpose**: Land and territory management
- **Features**:
  - Grid-based territory system
  - Ownership tracking
  - Development bonuses
- **Territory Types**:
  - Desert: High resources, low defense
  - Forest: Balanced stats
  - Mountain: Low resources, high defense
  - Space: Unique bonuses

#### BattleSystem
- **Purpose**: Combat and conquest mechanics
- **Features**:
  - Turn-based battles
  - Fleet composition
  - Resource consumption
- **Battle Results**:
  - Win: Territory gain, loot
  - Loss: Resource loss, territory loss

## Data Flow

### Game Initialization
1. User connects wallet via MetaMask
2. Frontend calls `GameController.createPlayer()`
3. Player contract address created
4. Player receives initial resources
5. Game state initialized to "LOBBY"

### Gameplay Loop
1. Player claims territory via `TerritoryManager.claim()`
2. Player deploys fleet via `AssetNFT.deployFleet()`
3. Player initiates battle via `BattleSystem.fight()`
4. Battle resolved, results written to smart contract
5. Rewards distributed via `EconomyToken`
6. Game state updated

### Economy Flow
1. Resources mined on-chain
2. Traded via `TradeMarket` contract
3. Converted to `EconomyToken` tokens
4. Used for upgrades and purchases
5. Rewarded for achievements

## Technical Stack

### Frontend
- **Framework**: Next.js 14 (React 18)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Blockchain**: Web3.js
- **State Management**: Zustand
- **Forms**: React Hook Form

### Backend
- **Runtime**: Node.js 20+
- **Framework**: Express.js
- **Database**: PostgreSQL
- **ORM**: TypeORM
- **Blockchain**: ethers.js
- **Authentication**: JWT
- **Caching**: Redis

### Smart Contracts
- **Language**: Solidity 0.8.20+
- **Development**: Hardhat 2.20
- **Testing**: Hardhat Gas Reporter
- **Audits**: Slither, MythX
- **Standards**: ERC-20, ERC-721, ERC-1155

## Security Considerations

### Smart Contract Security
- Audited contracts with Slither
- Gas optimization reviews
- Reentrancy guards implemented
- Access controls via Ownable pattern
- Safe math operations (SafeMath)

### Backend Security
- API rate limiting
- Input validation
- SQL injection prevention (TypeORM)
- CORS configuration
- HTTPS enforcement

### Frontend Security
- Environment variables for secrets
- HTTPS for all requests
- Input sanitization
- XSS prevention
- Web3 transaction signing validation

## Performance Optimization

### Smart Contracts
- Gas-efficient operations
- Batch transactions
- Minimal storage writes
- Efficient event emissions
- Lazy evaluation where possible

### Backend
- Database indexing
- Query optimization
- Connection pooling
- Caching strategies
- API response pagination

### Frontend
- Code splitting
- Lazy loading
- Service worker caching
- Image optimization
- CDN integration

## Deployment Architecture

### Base Sepolia Testnet
- **RPC**: https://sepolia.base.org
- **Chain ID**: 84532
- **Explorer**: https://sepolia.basescan.org
- **Block Explorer**: BaseScan

### Deployment Pipeline
1. **Testing**: Local and CI tests
2. **Verification**: Static analysis
3. **Deployment**: Base Sepolia testnet
4. **Verification**: Contract verification
5. **Testing**: Integration tests
6. **Production**: Base mainnet (optional)

## Monitoring & Observability

### Smart Contracts
- Event logs for all major actions
- Gas usage tracking
- Failed transaction monitoring
- Contract state verification

### Backend
- Application logs (Winston)
- Error tracking (Sentry)
- Performance metrics (Prometheus)
- Database query monitoring

### Frontend
- Console logs with structured data
- API request/response logging
- User error handling
- Performance monitoring

## Scalability Considerations

### Current Architecture
- Designed for ~10,000 active players
- 100,000+ transactions per day
- Real-time battle processing

### Future Scaling
- Horizontal scaling of backend services
- Sharding of territory management
- Layer 2 optimization
- Off-chain computation where applicable

## Testing Strategy

### Unit Tests
- Contract logic (Hardhat)
- Backend services (Jest)
- Frontend components (React Testing Library)

### Integration Tests
- Smart contract interactions
- Backend API endpoints
- Database operations

### E2E Tests
- Complete user flows
- Transaction simulations
- Network conditions

### Security Tests
- Code audits
- Penetration testing
- Bug bounty program

---

**Last Updated**: February 2026
**Version**: 1.0.0
