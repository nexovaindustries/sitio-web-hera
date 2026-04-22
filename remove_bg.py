from PIL import Image
import numpy as np
import os

input_path = r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg"
print(f"File exists: {os.path.exists(input_path)}")

# Load the image
img = Image.open(input_path)
img = img.convert("RGBA")
data = np.array(img)

# The background is blue (~70, 100, 180 range). The logo is cream/beige (~210, 195, 170)
# We want to make blue pixels transparent and keep the cream logo
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Better background detection
# Identify beige/cream pixels (high R and G, relatively low B)
# Logo text is around R:220-240, G:210-230, B:190-210
# Background is blue
logo_mask = (r > 150) & (g > 140) & (b < 230) & (r > b + 10)

# Make non-logo pixels transparent
data[~logo_mask] = [0, 0, 0, 0]

# For a cleaner look, let's keep the beige color but make it perfectly clean
# We'll set the logo pixels to a solid beige color and the rest to transparent
clean_data = np.zeros_like(data)
clean_data[logo_mask] = [235, 225, 205, 255] # Solid beige

result = Image.fromarray(clean_data)

# Crop to content (non-transparent area) with some padding
bbox = result.getbbox()
if bbox:
    pad = 10
    x1 = max(0, bbox[0] - pad)
    y1 = max(0, bbox[1] - pad)
    x2 = min(result.width, bbox[2] + pad)
    y2 = min(result.height, bbox[3] + pad)
    result = result.crop((x1, y1, x2, y2))

output_path = r"C:\Users\nicol\.gemini\antigravity\scratch\sitio-web-hera\hera-logo.png"
result.save(output_path, "PNG")
print(f"Saved to {output_path}")
print(f"Size: {result.size}")
