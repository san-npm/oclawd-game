// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title VoidBoosts
 * @dev Token utility contract for Void Conquest
 * @notice Manages protection shields, speed boosts, and other $VOID utilities
 * @notice Tokenomics: 100% of spent VOID goes to resources (buy VOID, sell VOID)
 */
contract VoidBoosts is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // ========== CONSTANTS ==========

    uint256 public constant VOID_SHIELD_COST = 1000 * 10**18;      // 1000 $VOID
    uint256 public constant VOID_SHIELD_DURATION = 48 hours;

    uint256 public constant ACCELERATOR_25_COST = 100 * 10**18;   // 100 $VOID
    uint256 public constant ACCELERATOR_50_COST = 250 * 10**18;   // 250 $VOID
    uint256 public constant ACCELERATOR_DURATION = 24 hours;

    uint256 public constant INSTANT_BUILD_COST = 500 * 10**18;    // 500 $VOID

    uint256 public constant YIELD_AMPLIFIER_COST = 200 * 10**18;  // 200 $VOID
    uint256 public constant YIELD_AMPLIFIER_DURATION = 24 hours;

    uint256 public constant EMERGENCY_RECALL_COST = 50 * 10**18;  // 50 $VOID

    uint256 public constant STEALTH_MODE_COST = 150 * 10**18;     // 150 $VOID
    uint256 public constant STEALTH_MODE_DURATION = 24 hours;

    uint256 public constant COLONY_PERMIT_COST = 2000 * 10**18;   // 2000 $VOID

    // ========== ENUMS ==========

    enum BoostType {
        VoidShield,
        Accelerator25,
        Accelerator50,
        YieldAmplifier,
        StealthMode
    }

    // ========== STRUCTS ==========

    struct ActiveBoost {
        BoostType boostType;
        uint256 activatedAt;
        uint256 expiresAt;
        uint256 multiplier; // basis points (10000 = 100%)
    }

    struct PlayerBoosts {
        mapping(BoostType => ActiveBoost) activeBoosts;
        uint256 extraColonySlots;
        uint256 instantBuildsUsed;
        uint256 emergencyRecallsUsed;
    }

    // ========== STATE ==========

    IERC20 public voidToken;
    address public gameContract;

    mapping(address => PlayerBoosts) private playerBoosts;
    mapping(address => bool) public hasVoidShield;
    mapping(address => uint256) public voidShieldExpiry;

    uint256 public totalSpentOnVoidShield;
    uint256 public totalSpentOnAccelerators;
    uint256 public totalSpentOnYieldAmplifier;
    uint256 public totalSpentOnInstantBuild;
    uint256 public totalSpentOnStealthMode;
    uint256 public totalSpentOnEmergencyRecall;
    uint256 public totalSpentOnColonyPermit;
    uint256 public totalSpentOnResources; // Generic resource trading

    // ========== EVENTS ==========

    event BoostActivated(address indexed player, BoostType boostType, uint256 expiresAt);
    event VoidShieldActivated(address indexed player, uint256 expiresAt);
    event InstantBuildUsed(address indexed player, uint256 colonyId, uint256 facilityId);
    event EmergencyRecallUsed(address indexed player, uint256 fleetId);
    event ColonyPermitPurchased(address indexed player, uint256 totalSlots);
    event TokensSpent(address indexed player, BoostType boostType, uint256 amount);
    event TokensSpentGeneric(address indexed player, uint256 amount, string reason);
    event TokensRedeemed(address indexed player, uint256 amount);

    // ========== CONSTRUCTOR ==========

    constructor(
        address _voidToken,
        address _gameContract
    ) Ownable(msg.sender) {
        voidToken = IERC20(_voidToken);
        gameContract = _gameContract;
    }

    // ========== MODIFIERS ==========

    modifier onlyGameContract() {
        require(msg.sender == gameContract, "Only game contract");
        _;
    }

    // ========== BOOST FUNCTIONS ==========

    /**
     * @dev Activate Void Shield - 48h protection from attacks
     */
    function activateVoidShield() external nonReentrant {
        require(!isShieldActive(msg.sender), "Shield already active");

        _processVoidSpending(msg.sender, VOID_SHIELD_COST);

        uint256 expiry = block.timestamp + VOID_SHIELD_DURATION;
        hasVoidShield[msg.sender] = true;
        voidShieldExpiry[msg.sender] = expiry;

        emit VoidShieldActivated(msg.sender, expiry);
    }

    /**
     * @dev Activate Accelerator - faster construction
     * @param level 25 or 50 for percentage boost
     */
    function activateAccelerator(uint256 level) external nonReentrant {
        require(level == 25 || level == 50, "Invalid level");

        BoostType boostType = level == 25 ? BoostType.Accelerator25 : BoostType.Accelerator50;
        uint256 cost = level == 25 ? ACCELERATOR_25_COST : ACCELERATOR_50_COST;

        _processVoidSpending(msg.sender, cost);

        uint256 expiry = block.timestamp + ACCELERATOR_DURATION;
        playerBoosts[msg.sender].activeBoosts[boostType] = ActiveBoost({
            boostType: boostType,
            activatedAt: block.timestamp,
            expiresAt: expiry,
            multiplier: level == 25 ? 12500 : 15000 // 125% or 150% speed
        });

        emit BoostActivated(msg.sender, boostType, expiry);
    }

    /**
     * @dev Activate Yield Amplifier - +50% resource production
     */
    function activateYieldAmplifier() external nonReentrant {
        _processVoidSpending(msg.sender, YIELD_AMPLIFIER_COST);

        uint256 expiry = block.timestamp + YIELD_AMPLIFIER_DURATION;
        playerBoosts[msg.sender].activeBoosts[BoostType.YieldAmplifier] = ActiveBoost({
            boostType: BoostType.YieldAmplifier,
            activatedAt: block.timestamp,
            expiresAt: expiry,
            multiplier: 15000 // 150% production
        });

        emit BoostActivated(msg.sender, BoostType.YieldAmplifier, expiry);
    }

    /**
     * @dev Activate Stealth Mode - block espionage
     */
    function activateStealthMode() external nonReentrant {
        _processVoidSpending(msg.sender, STEALTH_MODE_COST);

        uint256 expiry = block.timestamp + STEALTH_MODE_DURATION;
        playerBoosts[msg.sender].activeBoosts[BoostType.StealthMode] = ActiveBoost({
            boostType: BoostType.StealthMode,
            activatedAt: block.timestamp,
            expiresAt: expiry,
            multiplier: 0
        });

        emit BoostActivated(msg.sender, BoostType.StealthMode, expiry);
    }

    /**
     * @dev Use instant build - complete current construction
     * @param colonyId The colony ID
     * @param facilityId The facility being built
     */
    function useInstantBuild(uint256 colonyId, uint256 facilityId) external nonReentrant {
        _processVoidSpending(msg.sender, INSTANT_BUILD_COST);

        playerBoosts[msg.sender].instantBuildsUsed++;

        emit InstantBuildUsed(msg.sender, colonyId, facilityId);
        // Game contract will handle the actual completion
    }

    /**
     * @dev Use emergency recall - instantly recall fleet
     * @param fleetId The fleet ID to recall
     */
    function useEmergencyRecall(uint256 fleetId) external nonReentrant {
        _processVoidSpending(msg.sender, EMERGENCY_RECALL_COST);

        playerBoosts[msg.sender].emergencyRecallsUsed++;

        emit EmergencyRecallUsed(msg.sender, fleetId);
        // Game contract will handle the actual recall
    }

    /**
     * @dev Purchase colony permit - permanent +1 colony slot
     */
    function purchaseColonyPermit() external nonReentrant {
        _processVoidSpending(msg.sender, COLONY_PERMIT_COST);

        playerBoosts[msg.sender].extraColonySlots++;

        emit ColonyPermitPurchased(msg.sender, playerBoosts[msg.sender].extraColonySlots);
    }

    // ========== VOID/RESOURCE TRADING ==========

    /**
     * @dev Buy resources with VOID tokens (spend VOID, get resources in game)
     * @param amount Amount of VOID to spend (in wei)
     * @param resourceType Type of resource to purchase (0=metal, 1=crystal, 2=deuterium)
     * @param quantity Quantity of resources to purchase
     */
    function buyResources(uint256 amount, uint256 resourceType, uint256 quantity) external nonReentrant {
        _processVoidSpending(msg.sender, amount);

        // Validate resource type
        require(resourceType <= 2, "Invalid resource type");
        require(quantity > 0, "Quantity must be > 0");

        totalSpentOnResources += amount;
        emit TokensSpentGeneric(msg.sender, amount, "Buy resources");

        // Game contract will handle the actual resource transfer
        // This is just for VOID spending tracking - actual resource exchange happens in game logic
    }

    /**
     * @dev Sell resources for VOID tokens (spend resources, get VOID)
     * @param amount Amount of VOID to receive (in wei)
     * @param resourceType Type of resource to sell (0=metal, 1=crystal, 2=deuterium)
     * @param quantity Quantity of resources to sell
     */
    function sellResources(uint256 amount, uint256 resourceType, uint256 quantity) external nonReentrant {
        // Validate input
        require(resourceType <= 2, "Invalid resource type");
        require(quantity > 0, "Quantity must be > 0");

        // In the new tokenomics, selling resources for VOID would work like this:
        // 1. Game contract verifies player has the required resources
        // 2. Resources are burned (removed from game state)
        // 3. VOID tokens are transferred to player

        emit TokensRedeemed(msg.sender, amount);
    }

    // ========== INTERNAL ==========

    /**
     * @dev Process VOID spending (100% goes to VOID, no burn/staking)
     */
    function _processVoidSpending(address player, uint256 amount) internal {
        voidToken.safeTransferFrom(player, address(this), amount);

        // Track spending by type
        totalSpentOnVoidShield += amount;

        emit TokensSpent(player, BoostType.VoidShield, amount);
    }

    // ========== VIEW FUNCTIONS ==========

    /**
     * @dev Check if player has active void shield
     */
    function isShieldActive(address player) public view returns (bool) {
        return hasVoidShield[player] && voidShieldExpiry[player] > block.timestamp;
    }

    /**
     * @dev Get player's accelerator multiplier (basis points)
     */
    function getAcceleratorMultiplier(address player) external view returns (uint256) {
        ActiveBoost storage boost25 = playerBoosts[player].activeBoosts[BoostType.Accelerator25];
        ActiveBoost storage boost50 = playerBoosts[player].activeBoosts[BoostType.Accelerator50];

        if (boost50.expiresAt > block.timestamp) {
            return boost50.multiplier;
        }
        if (boost25.expiresAt > block.timestamp) {
            return boost25.multiplier;
        }
        return 10000; // 100% = no boost
    }

    /**
     * @dev Get player's yield multiplier (basis points)
     */
    function getYieldMultiplier(address player) external view returns (uint256) {
        ActiveBoost storage boost = playerBoosts[player].activeBoosts[BoostType.YieldAmplifier];

        if (boost.expiresAt > block.timestamp) {
            return boost.multiplier;
        }
        return 10000; // 100% = no boost
    }

    /**
     * @dev Check if player has stealth mode active
     */
    function isStealthActive(address player) external view returns (bool) {
        return playerBoosts[player].activeBoosts[BoostType.StealthMode].expiresAt > block.timestamp;
    }

    /**
     * @dev Get player's extra colony slots
     */
    function getExtraColonySlots(address player) external view returns (uint256) {
        return playerBoosts[player].extraColonySlots;
    }

    // ========== ADMIN ==========

    function setGameContract(address _gameContract) external onlyOwner {
        gameContract = _gameContract;
    }
}
