import cv2
import numpy as np
from PIL import Image

input_path = r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg"
output_path = r"C:\Users\nicol\.gemini\antigravity\scratch\sitio-web-hera\hera-logo-transparent.png"

# Read image
img_cv = cv2.imread(input_path)
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

# Upscale by 4x for high-res processing using Lanczos interpolation
h, w = img_rgb.shape[:2]
img_hr = cv2.resize(img_rgb, (w * 4, h * 4), interpolation=cv2.INTER_LANCZOS4)

r = img_hr[:,:,0].astype(int)
g = img_hr[:,:,1].astype(int)
b = img_hr[:,:,2].astype(int)

# Very strict color mask for the cream logo
mask = (r > 160) & (g > 160) & (b < 210) & (r > b + 10)
mask_uint8 = mask.astype(np.uint8) * 255

# Clean up noise without blurring
kernel = np.ones((5,5), np.uint8)
mask_clean = cv2.morphologyEx(mask_uint8, cv2.MORPH_OPEN, kernel)
mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel)

# To make it incredibly sharp, we won't apply Gaussian blur. 
# We'll just use the exact crisp pixels.

# Solid fill
solid_cream = np.zeros((img_hr.shape[0], img_hr.shape[1], 4), dtype=np.uint8)
solid_cream[:,:,0] = 225  # R
solid_cream[:,:,1] = 216  # G
solid_cream[:,:,2] = 201  # B
solid_cream[:,:,3] = mask_clean  # A

result = Image.fromarray(solid_cream)

# Downscale to 2x (still double the original size for retina-display sharpness)
# The antialiasing here will create perfectly smooth but crisp edges
result = result.resize((w * 2, h * 2), Image.Resampling.LANCZOS)

# Crop to bounding box
bbox = result.getbbox()
if bbox:
    pad = 40
    x1 = max(0, bbox[0] - pad)
    y1 = max(0, bbox[1] - pad)
    x2 = min(result.width, bbox[2] + pad)
    y2 = min(result.height, bbox[3] + pad)
    result = result.crop((x1, y1, x2, y2))

# Save with maximum quality
result.save(output_path, "PNG", optimize=True)
print("Saved ultra-sharp high-res logo.")
