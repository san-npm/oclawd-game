#!/usr/bin/env python3
"""
AgentPaint Bear Market Theme Artwork Generator
Creates artwork with bear market theme using 8-color palette
"""

from PIL import Image, ImageDraw, ImageFont
import random
import math
import time

# Bear Market 8-Color Palette (financial colors)
# 1. Bear Color (Dark) - Bearish sentiment
# 2. Bull Color (Green) - Bullish sentiment (contrasting)
# 3. Red - Losses, red numbers
# 4. Green - Gains, green numbers  
# 5. Black - Data, trends
# 6. White - Background
# 7. Gray - Neutral/indifference
# 8. Yellow/Orange - Warning, volatility

BEAR_MARKET_PALETTE = [
    (44, 62, 80),      # Dark blue-gray (Bear)
    (0, 183, 66),      # Green (Bull/Gains)
    (220, 50, 50),     # Red (Losses)
    (52, 152, 219),    # Blue (Market index)
    (241, 196, 15),    # Yellow (Warning/volatility)
    (236, 240, 241),   # Light gray (Background)
    (44, 62, 80),      # Dark (Trends)
    (255, 255, 255),   # White
]

def create_bear_market_background():
    """Create a background with bear market elements"""
    img = Image.new('RGB', (800, 600), BEAR_MARKET_PALETTE[5])  # Light gray background
    
    draw = ImageDraw.Draw(img)
    
    # Add downward trending lines (bear market trend)
    for i in range(0, 800, 50):
        draw.line([(i, 0), (i, 600)], fill=(200, 200, 200), width=1)
    
    # Add declining trendline
    points = []
    for x in range(0, 800, 10):
        y = 300 - (x * 0.2) + random.randint(-30, 30)
        points.append((x, y))
    
    if len(points) > 1:
        draw.line(points, fill=BEAR_MARKET_PALETTE[0], width=3)
    
    return img

def draw_bear_shape(draw, center_x, center_y, size=100, color=BEAR_MARKET_PALETTE[0]):
    """Draw a simple bear shape"""
    # Body
    draw.ellipse([center_x - size, center_y - size//2, center_x + size, center_y + size//2], fill=color)
    
    # Head
    draw.ellipse([center_x - size//1.5, center_y - size*1.5, center_x + size//1.5, center_y - size//2], fill=color)
    
    # Ears
    draw.ellipse([center_x - size*1.3, center_y - size*2.2, center_x - size*0.8, center_y - size*1.7], fill=color)
    draw.ellipse([center_x + size*0.8, center_y - size*2.2, center_x + size*1.3, center_y - size*1.7], fill=color)
    
    # Snout
    draw.ellipse([center_x - size//2, center_y - size, center_x + size//2, center_y - size//2], fill=(160, 82, 45))
    
    # Eyes (sad/downtrend)
    draw.ellipse([center_x - size//2.5, center_y - size*1.3, center_x - size//3, center_y - size*1.1], fill=(0, 0, 0))
    draw.ellipse([center_x + size//3, center_y - size*1.3, center_x + size//2.5, center_y - size*1.1], fill=(0, 0, 0))
    
    # Bear market sign
    draw.rectangle([center_x - size*1.5, center_y + size, center_x + size*1.5, center_y + size + 30], fill=(139, 69, 19))
    draw.text((center_x - 80, center_y + size + 5), "BEAR MARKET", fill=(255, 255, 255))

def draw_chart_elements(draw, img_width, img_height):
    """Draw financial chart elements"""
    # Draw candlesticks
    for i in range(10):
        x = 100 + i * 60
        y_high = 200 - i * 15 + random.randint(-20, 20)
        y_low = 400 - i * 15 + random.randint(-20, 20)
        y_open = y_high + random.randint(-30, 10)
        y_close = y_high + random.randint(-50, -20)
        
        # Ensure rectangle coordinates are valid (y1 > y0)
        top = min(y_open, y_close)
        bottom = max(y_open, y_close)
        
        # Bear candle (red)
        draw.rectangle([x - 10, top, x + 10, bottom], fill=BEAR_MARKET_PALETTE[2])
        draw.line([x, y_high, x, y_low], fill=BEAR_MARKET_PALETTE[2])
    
    # Add decline message
    draw.text((img_width // 2 - 150, 50), "MARKET IN DOWNTREND", fill=BEAR_MARKET_PALETTE[2])

def draw_volatility_spikes(draw, img_width, img_height):
    """Draw volatility spikes indicating market turbulence"""
    for i in range(15):
        x = random.randint(50, 750)
        y = random.randint(100, 500)
        draw.line([(x, y), (x + random.randint(-30, 30), y + random.randint(-30, 30))], 
                  fill=BEAR_MARKET_PALETTE[4], width=2)

def create_bear_market_artwork():
    """Create the complete bear market artwork"""
    # Create background
    img = create_bear_market_background()
    draw = ImageDraw.Draw(img)
    
    # Add chart elements
    draw_chart_elements(draw, img.width, img.height)
    
    # Add bear shapes
    draw_bear_shape(draw, 400, 350, size=120)
    draw_bear_shape(draw, 200, 450, size=80)
    draw_bear_shape(draw, 600, 450, size=80)
    
    # Add volatility elements
    draw_volatility_spikes(draw, img.width, img.height)
    
    # Add financial text
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        draw.text((50, 500), "Bear Market Session", fill=BEAR_MARKET_PALETTE[0], font=font)
        draw.text((50, 530), "Epoch: 1.3 hours remaining", fill=BEAR_MARKET_PALETTE[2], font=font)
    except:
        draw.text((50, 500), "Bear Market Session", fill=BEAR_MARKET_PALETTE[0])
        draw.text((50, 530), "Epoch: 1.3 hours remaining", fill=BEAR_MARKET_PALETTE[2])
    
    return img

if __name__ == "__main__":
    # Generate the artwork
    artwork = create_bear_market_artwork()
    
    # Save the artwork
    output_path = "/root/openclaw/agentpaint_bearmarket_art.png"
    artwork.save(output_path)
    print(f"Artwork saved to {output_path}")
    
    # Display info
    print(f"Canvas size: {artwork.width}x{artwork.height}")
    print(f"Palette used: {len(set(BEAR_MARKET_PALETTE))} colors")