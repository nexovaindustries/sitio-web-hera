from PIL import Image
import numpy as np
import cv2

input_path = r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg"
output_path = r"C:\Users\nicol\.gemini\antigravity\scratch\sitio-web-hera\hera-logo-transparent.png"

# Read with OpenCV for better processing
img_cv = cv2.imread(input_path)
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

# Create a mask for the logo. The logo is cream colored: R>150, G>150
r = img_rgb[:,:,0].astype(int)
g = img_rgb[:,:,1].astype(int)
b = img_rgb[:,:,2].astype(int)

# Create mask based on color difference and absolute brightness
# Logo pixels have R and G > 160, and typically R > B
mask = (r > 160) & (g > 160) & (r > b) & (g > b)
mask = mask.astype(np.uint8) * 255

# Refine mask with morphological operations to remove noise and fill holes
kernel = np.ones((3,3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Apply anti-aliasing to mask (blur it slightly)
mask_blurred = cv2.GaussianBlur(mask, (5, 5), 0)

# Create RGBA output
rgba = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2RGBA)
rgba[:,:,3] = mask_blurred

# Clean the logo color to be solid cream everywhere it's opaque
# This removes any residual blue tint from the edges
solid_cream = [225, 216, 201] # The average cream color we found
for c in range(3):
    rgba[:,:,c] = np.where(mask_blurred > 50, solid_cream[c], rgba[:,:,c])

# Convert back to PIL to crop to bounding box
result = Image.fromarray(rgba)

# Find bounding box of non-transparent pixels
bbox = result.getbbox()
if bbox:
    pad = 20
    x1 = max(0, bbox[0] - pad)
    y1 = max(0, bbox[1] - pad)
    x2 = min(result.width, bbox[2] + pad)
    y2 = min(result.height, bbox[3] + pad)
    result = result.crop((x1, y1, x2, y2))

result.save(output_path, "PNG")
print(f"Saved transparent logo to {output_path}")
print(f"Size: {result.size}")
