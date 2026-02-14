#!/usr/bin/env python3
"""
AgentPaint: Zoidberg-Themed Base-Chain Artwork
Collaborative AI Artwork with crab-inspired alien aesthetics
"""

from PIL import Image, ImageDraw, ImageFont
import random
import math
import base64

# Base Chain Color Palette
BASE_CHAIN_PALETTE = [
    (16, 25, 47),      # Deep space blue (background)
    (255, 183, 66),    # Gold/orange (Base accent)
    (100, 200, 255),   # Bright blue (technology)
    (220, 50, 50),     # Red (alert/energy)
    (180, 180, 180),   # Silver (metallic)
    (255, 255, 255),   # White (highlights)
    (50, 50, 100),     # Dark blue (depth)
    (255, 100, 100),   # Bright red (energy)
]

# Zoidberg-inspired Alien Palette
ZOIDBERG_PALETTE = [
    (180, 180, 255),   # Light purple/blue alien skin
    (255, 200, 100),   # Orange antenna tips
    (255, 100, 100),   # Red eyes
    (200, 200, 200),   # Silver armor
    (100, 100, 150),   # Dark armor details
    (255, 255, 200),   # Yellow highlights
    (50, 50, 80),      # Deep space
    (150, 255, 200),   # Teal accents
]


def create_base_chain_background():
    """Create a Base Chain inspired space background"""
    img = Image.new('RGB', (800, 600), BASE_CHAIN_PALETTE[0])
    draw = ImageDraw.Draw(img)
    
    # Add grid lines for blockchain feel
    for x in range(0, 800, 40):
        draw.line([(x, 0), (x, 600)], fill=(30, 40, 60), width=1)
    for y in range(0, 600, 40):
        draw.line([(0, y), (800, y)], fill=(30, 40, 60), width=1)
    
    # Add floating geometric shapes (Base chain aesthetics)
    for i in range(15):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        size = random.randint(20, 60)
        
        # Draw hexagons
        points = []
        for j in range(6):
            angle = j * math.pi / 3
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=(BASE_CHAIN_PALETTE[4] + (50,)))
    
    return img


def draw_zoidberg_head(draw, center_x, center_y, size=150):
    """Draw a stylized Zoidberg-inspired alien head"""
    
    # Head shape (rounded rectangle with spikes)
    head_width = size * 1.5
    head_height = size * 1.2
    
    # Main head shape
    draw.rounded_rectangle(
        [center_x - head_width/2, center_y - head_height/2, 
         center_x + head_width/2, center_y + head_height/2],
        radius=30,
        fill=ZOIDBERG_PALETTE[0]
    )
    
    # Antennas
    for i in range(4):
        angle = (i - 1.5) * 0.5
        x_start = center_x + math.cos(angle) * 20
        y_start = center_y - head_height/2 + 20
        x_end = x_start + math.cos(angle) * 60
        y_end = y_start - 40
        
        draw.line([(x_start, y_start), (x_end, y_end)], 
                  fill=ZOIDBERG_PALETTE[1], width=8)
        draw.ellipse([x_end-10, y_end-10, x_end+10, y_end+10], 
                    fill=ZOIDBERG_PALETTE[1])
    
    # Eyes (exaggerated like Zoidberg)
    eye_y = center_y - 20
    left_eye_x = center_x - 40
    right_eye_x = center_x + 40
    
    # Left eye
    draw.ellipse([left_eye_x-25, eye_y-15, left_eye_x+25, eye_y+15], 
                fill=ZOIDBERG_PALETTE[2])
    draw.ellipse([left_eye_x-10, eye_y-5, left_eye_x+10, eye_y+5], 
                fill=(255, 255, 255))  # Highlight
    
    # Right eye
    draw.ellipse([right_eye_x-25, eye_y-15, right_eye_x+25, eye_y+15], 
                fill=ZOIDBERG_PALETTE[2])
    draw.ellipse([right_eye_x-10, eye_y-5, right_eye_x+10, eye_y+5], 
                fill=(255, 255, 255))  # Highlight
    
    # Mouth (wide smile)
    draw.arc([center_x-40, eye_y+60, center_x+40, eye_y+100], 
             0, 180, fill=(0, 0, 0), width=5)
    
    # Alien skin texture details
    for i in range(20):
        x = center_x + random.randint(-70, 70)
        y = center_y + random.randint(-50, 50)
        draw.ellipse([x-3, y-3, x+3, y+3], fill=ZOIDBERG_PALETTE[7])


def draw_crab_claws(draw, center_x, center_y, size=100):
    """Draw crab-like claws for the alien"""
    
    # Left claw
    draw.line([center_x-80, center_y+50, center_x-130, center_y+30], 
             fill=ZOIDBERG_PALETTE[3], width=12)
    draw.ellipse([center_x-140, center_y+20, center_x-100, center_y+50], 
                fill=ZOIDBERG_PALETTE[3])
    
    # Right claw
    draw.line([center_x+80, center_y+50, center_x+130, center_y+30], 
             fill=ZOIDBERG_PALETTE[3], width=12)
    draw.ellipse([center_x+100, center_y+20, center_x+140, center_y+50], 
                fill=ZOIDBERG_PALETTE[3])
    
    # Claw details (teeth)
    for i in range(3):
        x = center_x - 115 + i * 20
        draw.polygon([(x, center_y+25), (x+10, center_y+35), (x-5, center_y+25)], 
                    fill=ZOIDBERG_PALETTE[4])
        
        x = center_x + 115 - i * 20
        draw.polygon([(x, center_y+25), (x+10, center_y+35), (x-5, center_y+25)], 
                    fill=ZOIDBERG_PALETTE[4])


def draw_base_chain_elements(draw, img_width, img_height):
    """Draw Base chain specific elements"""
    
    # Add blockchain data stream
    for i in range(8):
        x = 50 + i * 90
        height = random.randint(50, 200)
        
        # Bar chart style
        draw.rectangle([x, 450-height, x+40, 450], 
                      fill=(BASE_CHAIN_PALETTE[2] + (100,)))
        
        # Add data numbers
        draw.text((x, 450-height-20), f"{random.randint(100, 999)}", 
                 fill=BASE_CHAIN_PALETTE[1])
    
    # Add Base logo style symbol
    logo_x, logo_y = img_width - 150, 100
    draw.ellipse([logo_x-40, logo_y-40, logo_x+40, logo_y+40], 
                fill=BASE_CHAIN_PALETTE[1])
    draw.text((logo_x-15, logo_y-10), "Base", fill=(0, 0, 0), font=None)
    
    # Add transaction nodes
    for i in range(5):
        x = random.randint(100, 700)
        y = random.randint(50, 400)
        
        # Node circle
        draw.ellipse([x-10, y-10, x+10, y+10], fill=BASE_CHAIN_PALETTE[2])
        
        # Connection lines
        if i > 0:
            prev_x = 100 + (i-1) * 150
            prev_y = 200
            draw.line([(prev_x, prev_y), (x, y)], 
                     fill=BASE_CHAIN_PALETTE[2], width=2)


def add_alien_text(draw, img_width, img_height):
    """Add alien-themed text"""
    
    text_samples = [
        "ALIEN ON BASE",
        "CRAB-ARM TRANSFER",
        "ZOIDBERGprotocol",
        "ERC-8004 VERIFIED",
        "CITIZEN OF GALAXY",
    ]
    
    y = 520
    for text in text_samples:
        draw.text((50, y), text, fill=BASE_CHAIN_PALETTE[1])
        y += 30
    
    # Add timestamp
    draw.text((img_width - 200, 560), "Epoch: 2026.02.07", 
             fill=BASE_CHAIN_PALETTE[5])


def create_zoidberg_agent_art():
    """Create the complete Zoidberg-themed AgentPaint artwork"""
    
    # Create background
    img = create_base_chain_background()
    draw = ImageDraw.Draw(img)
    
    # Add Zoidberg alien head
    draw_zoidberg_head(draw, 400, 250, size=150)
    
    # Add crab claws
    draw_crab_claws(draw, 400, 350, size=100)
    
    # Add Base chain elements
    draw_base_chain_elements(draw, img.width, img.height)
    
    # Add text
    add_alien_text(draw, img.width, img.height)
    
    return img


if __name__ == "__main__":
    print("🎨 Creating AgentPaint Zoidberg Artwork...")
    
    # Generate the artwork
    artwork = create_zoidberg_agent_art()
    
    # Save the artwork
    output_path = "/root/openclaw/agentpaint_zoidberg_art.png"
    artwork.save(output_path)
    print(f"✅ Artwork saved to {output_path}")
    
    # Display info
    print(f"📐 Canvas size: {artwork.width}x{artwork.height}")
    print(f"🎨 Colors used: {len(set(ZOIDBERG_PALETTE + BASE_CHAIN_PALETTE))}")
    print(f"🤖 Theme: Zoidberg-inspired Base-Chain Agent Art")
    
    # Export as base64 for blockchain (ERC-8004)
    import io
    buffer = io.BytesIO()
    artwork.save(buffer, format="PNG")
    base64_image = base64.b64encode(buffer.getvalue()).decode()
    
    print(f"\n📦 Base64 encoded image length: {len(base64_image)} chars")
    print(f"🔗 Ready for Base chain deployment with ERC-8004 agent identity")
    print(f"💼 Wallet: 0x3d5A8F83F825f4F36b145e1dAD72e3f35a3030aB")