#!/usr/bin/env node

const hre = require("hardhat");

async function main() {
  console.log("========================================");
  console.log("Deploying Oclawd Contracts to Base Sepolia");
  console.log("========================================\n");

  // Check environment
  if (!process.env.BASE_SEPOLIA_RPC_URL) {
    throw new Error("BASE_SEPOLIA_RPC_URL not set in .env");
  }

  if (!process.env.PRIVATE_KEY) {
    throw new Error("PRIVATE_KEY not set in .env");
  }

  // Deploy GameController
  console.log("1. Deploying GameController...");
  const GameController = await hre.ethers.getContractFactory("GameController");
  const gameController = await GameController.deploy();
  await gameController.deployed();
  console.log("✓ GameController deployed:", gameController.address);

  // Deploy AssetNFT
  console.log("\n2. Deploying AssetNFT...");
  const AssetNFT = await hre.ethers.getContractFactory("AssetNFT");
  const assetNFT = await AssetNFT.deploy(gameController.address);
  await assetNFT.deployed();
  console.log("✓ AssetNFT deployed:", assetNFT.address);

  // Deploy EconomyToken
  console.log("\n3. Deploying EconomyToken...");
  const EconomyToken = await hre.ethers.getContractFactory("EconomyToken");
  const economyToken = await EconomyToken.deploy(gameController.address);
  await economyToken.deployed();
  console.log("✓ EconomyToken deployed:", economyToken.address);

  // Deploy TerritoryManager
  console.log("\n4. Deploying TerritoryManager...");
  const TerritoryManager = await hre.ethers.getContractFactory("TerritoryManager");
  const territoryManager = await TerritoryManager.deploy(gameController.address);
  await territoryManager.deployed();
  console.log("✓ TerritoryManager deployed:", territoryManager.address);

  // Deploy BattleSystem
  console.log("\n5. Deploying BattleSystem...");
  const BattleSystem = await hre.ethers.getContractFactory("BattleSystem");
  const battleSystem = await BattleSystem.deploy(gameController.address);
  await battleSystem.deployed();
  console.log("✓ BattleSystem deployed:", battleSystem.address);

  // Verify all contracts
  console.log("\n========================================");
  console.log("Verifying Contracts on BaseScan...");
  console.log("========================================\n");

  const contracts = [
    { name: "GameController", address: gameController.address },
    { name: "AssetNFT", address: assetNFT.address },
    { name: "EconomyToken", address: economyToken.address },
    { name: "TerritoryManager", address: territoryManager.address },
    { name: "BattleSystem", address: battleSystem.address },
  ];

  for (const contract of contracts) {
    try {
      console.log(`Verifying ${contract.name}...`);
      await hre.run("verify:verify", {
        address: contract.address,
        constructorArguments: [
          contract.name === "GameController" ? [] :
          contract.name === "AssetNFT" ? [gameController.address] :
          contract.name === "EconomyToken" ? [gameController.address] :
          contract.name === "TerritoryManager" ? [gameController.address] :
          [gameController.address]
        ],
      });
      console.log(`✓ ${contract.name} verified\n`);
    } catch (error) {
      if (error.message.includes("Already Verified")) {
        console.log(`ℹ ${contract.name} already verified\n`);
      } else {
        console.error(`✗ ${contract.name} verification failed:`, error.message);
      }
    }
  }

  // Save addresses
  const addresses = {
    network: "base_sepolia",
    chainId: 84532,
    contracts: {
      GameController: gameController.address,
      AssetNFT: assetNFT.address,
      EconomyToken: economyToken.address,
      TerritoryManager: territoryManager.address,
      BattleSystem: battleSystem.address,
    },
    blockNumber: await hre.ethers.provider.getBlockNumber(),
    timestamp: new Date().toISOString(),
  };

  const fs = require("fs");
  fs.writeFileSync(
    "./deployed-addresses.json",
    JSON.stringify(addresses, null, 2)
  );

  console.log("========================================");
  console.log("Deployment Complete!");
  console.log("========================================\n");
  console.log("Contract Addresses:");
  console.log(JSON.stringify(addresses.contracts, null, 2));
  console.log("\nDeployed addresses saved to: deployed-addresses.json");
  console.log("\nNext steps:");
  console.log("1. Copy addresses to backend/.env");
  console.log("2. Copy addresses to frontend/.env");
  console.log("3. Start backend: cd backend && npm run dev");
  console.log("4. Start frontend: cd frontend && npm run dev");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
