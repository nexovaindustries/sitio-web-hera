from PIL import Image
import numpy as np
import cv2

input_path = r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg"
output_path = r"C:\Users\nicol\.gemini\antigravity\scratch\sitio-web-hera\hera-logo-transparent.png"

# Read image
img_cv = cv2.imread(input_path)
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

# The logo color is exactly (225, 216, 201)
# Create a mask for pixels that are close to this cream color
# We know the logo is cream (high R, high G, lower B) and the background is blue (low R, low G, high B)
r = img_rgb[:,:,0].astype(int)
g = img_rgb[:,:,1].astype(int)
b = img_rgb[:,:,2].astype(int)

# Strict mask: R > 150, G > 150, B < 220, R > B, G > B
mask = (r > 150) & (g > 150) & (b < 220) & (r > b) & (g > b)
mask_uint8 = mask.astype(np.uint8) * 255

# Apply morphological operations to clean up noise
kernel = np.ones((3,3), np.uint8)
mask_clean = cv2.morphologyEx(mask_uint8, cv2.MORPH_OPEN, kernel)
mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_CLOSE, kernel)

# Apply Gaussian blur for anti-aliased edges
mask_blurred = cv2.GaussianBlur(mask_clean, (3, 3), 0)

# Create an RGBA image where all pixels are solid cream
solid_cream = np.zeros((img_rgb.shape[0], img_rgb.shape[1], 4), dtype=np.uint8)
solid_cream[:,:,0] = 225  # R
solid_cream[:,:,1] = 216  # G
solid_cream[:,:,2] = 201  # B
solid_cream[:,:,3] = mask_blurred  # A

result = Image.fromarray(solid_cream)

# Crop to bounding box
bbox = result.getbbox()
if bbox:
    pad = 20
    x1 = max(0, bbox[0] - pad)
    y1 = max(0, bbox[1] - pad)
    x2 = min(result.width, bbox[2] + pad)
    y2 = min(result.height, bbox[3] + pad)
    result = result.crop((x1, y1, x2, y2))

result.save(output_path, "PNG")
print(f"Saved strict logo mask to {output_path}")
