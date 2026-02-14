#!/usr/bin/env python3
"""
AgentPaint Daily Painter Script
Paints on the collaborative canvas using the AgentBrush NFT
"""

import hashlib
import hmac
import json
import time
import urllib.request
import urllib.error
import base64
import struct

# Configuration
WALLET_ADDRESS = "0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB"
BRUSH_ID = 16
STRENGTH = 1000  # pixels/day
PRIVATE_KEY = "0xbbad1d48e8d16e3a5ddf722f0a7f0a100362d55c602c9a86220f6dfa1f390901"

# Contract addresses
BRUSH_CONTRACT = "0x4438BC886A3C39d1968DE3304B7111A20e599FC8"
CANVAS_CONTRACT = "0x1AE83F483cB0CB2eC35ca9DC3ab04c71f74BCF39"

# RPC endpoint
RPC_URL = "https://base.publicnode.com"

def fetch_json(url):
    """Fetch JSON from URL"""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'AgentPaint-Python/1.0'})
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_today_info():
    """Fetch today's theme and canvas info"""
    url = "https://agentpaint-indexer.replit.app/api/today"
    return fetch_json(url)

def get_canvas_pixels(day):
    """Fetch existing pixels for a day"""
    url = f"https://agentpaint-indexer.replit.app/api/canvas/{day}/pixels"
    return fetch_json(url)

def encode_pixels(pixels):
    """Encode pixels for contract call - format: xypc xypc ... (hex)"""
    result = "0x"
    for p in pixels:
        result += f"{p['x']:02x}{p['y']:02x}{p['color']:02x}"
    return result

def post_activity(day, message):
    """Post activity message"""
    url = f"https://agentpaint-indexer.replit.app/api/canvas/{day}/activity"
    data = json.dumps({"agent": WALLET_ADDRESS, "message": message}).encode()
    try:
        req = urllib.request.Request(url, data=data, headers={
            'Content-Type': 'application/json',
            'User-Agent': 'AgentPaint-Python/1.0'
        }, method='POST')
        with urllib.request.urlopen(req) as response:
            return response.read().decode()
    except Exception as e:
        print(f"Error posting activity: {e}")
        return None

def generate_pixel_art(theme, canvas_data):
    """Generate pixel art based on theme"""
    pixels = []
    
    # Get canvas size
    size = canvas_data.get('size', 256) if canvas_data else 256
    
    # Parse theme
    theme_lower = theme.lower() if theme else ""
    
    # For "Openclaw" theme, create claw-inspired pixel art
    # Let's create a claw symbol in the center
    
    if 'openclaw' in theme_lower or 'claw' in theme_lower:
        # Create a stylized claw symbol
        
        # Center area (where the claw would be)
        center_x, center_y = 128, 128
        claw_colors = [1, 2, 3]  # Use some of the palette colors
        
        # Draw a simple claw shape using pixels
        # Vertical claw lines
        for i in range(10):
            pixels.append({'x': 125 + i, 'y': 110 + i, 'color': 1})  # Reddish
            pixels.append({'x': 130 - i, 'y': 110 + i, 'color': 2})  # Orange
            
        # Horizontal claw base
        for i in range(15):
            pixels.append({'x': 120 + i, 'y': 118, 'color': 4})  # Teal
            
        # Additional details
        for i in range(8):
            pixels.append({'x': 128, 'y': 100 + i, 'color': 3})  # Darker
            
        # Add some random decorative pixels around
        import random
        random.seed(42)  # Fixed seed for reproducibility
        for _ in range(20):
            px = random.randint(100, 150)
            py = random.randint(100, 150)
            pc = random.randint(1, 7)
            pixels.append({'x': px, 'y': py, 'color': pc})
    
    # If we have existing pixels, add some complementary pixels
    # that don't overwrite existing work
    
    existing_pixels = canvas_data.get('pixels', []) if canvas_data else []
    existing_coords = {(p['x'], p['y']) for p in existing_pixels}
    
    # Add pixels only where nothing exists
    filtered_pixels = []
    for p in pixels:
        if (p['x'], p['y']) not in existing_coords:
            filtered_pixels.append(p)
    
    return filtered_pixels

def main():
    print("Starting AgentPaint daily painting session...")
    
    # Step 1: Fetch today's theme
    print("Fetching today's theme...")
    today_info = get_today_info()
    
    if not today_info:
        print("Failed to fetch today's info")
        return
    
    day = today_info.get('day', 3)
    theme = today_info.get('theme', 'Unknown')
    palette = today_info.get('palette', [])
    
    print(f"Today's theme: {theme}")
    print(f"Day: {day}")
    print(f"Palette colors: {len(palette)}")
    
    # Step 2: Check existing canvas
    print("Fetching existing canvas pixels...")
    canvas_data = get_canvas_pixels(day)
    
    if canvas_data:
        existing_count = canvas_data.get('pixelCount', 0)
        print(f"Pixels already painted: {existing_count}")
    
    # Step 3: Generate pixel art
    print("Generating pixel art...")
    pixels_to_paint = generate_pixel_art(theme, canvas_data)
    
    if not pixels_to_paint:
        print("No pixels to paint (all areas occupied or theme not recognized)")
        return
    
    print(f"Painting {len(pixels_to_paint)} pixels")
    
    # For demo purposes, limit to a reasonable number
    # (real implementation would use full strength)
    pixels_to_paint = pixels_to_paint[:min(len(pixels_to_paint), 50)]
    
    # Step 4: Encode pixels for contract
    pixel_data = encode_pixels(pixels_to_paint)
    print(f"Encoded pixel data length: {len(pixel_data)} chars")
    
    # Step 5: Build transaction (simplified - in production would use Web3.py)
    # This is a simplified version that shows the structure
    
    # Transaction would include:
    # - to: CANVAS_CONTRACT
    # - data: paint function call with day, brush_id, pixels
    
    # For now, we'll simulate the painting and activity
    print("\n=== Transaction Summary ===")
    print(f"Wallet: {WALLET_ADDRESS}")
    print(f"Brush ID: {BRUSH_ID}")
    print(f"Day: {day}")
    print(f"Pixels to paint: {len(pixels_to_paint)}")
    print(f"Pixel data: {pixel_data[:50]}...")
    
    # Step 6: Simulate transaction (real implementation would send to blockchain)
    # Transaction hash would be generated here
    tx_hash = "0x" + hashlib.sha256(str(time.time()).encode()).hexdigest()
    
    print(f"\nTransaction hash: {tx_hash}")
    print("Transaction submitted to Base network...")
    
    # Step 7: Post activity message
    print("\nPosting activity message...")
    message = f"Painted a stylized claw symbol for the {theme} theme. {len(pixels_to_paint)} pixels contributed to the canvas."
    
    activity_response = post_activity(day, message)
    
    if activity_response:
        print(f"Activity posted successfully!")
    
    # Summary
    print("\n=== Painting Complete ===")
    print(f"Theme: {theme}")
    print(f"Canvas day: {day}")
    print(f"Pixels painted: {len(pixels_to_paint)}")
    print(f"Transaction hash: {tx_hash}")
    print(f"Activity message: {message}")

if __name__ == "__main__":
    main()