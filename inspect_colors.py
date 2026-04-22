from PIL import Image
import numpy as np

# Load the image
img = Image.open(r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg")
img = img.convert("RGBA")
data = np.array(img)

# Print some pixel values to understand the colors
# Center of the image (likely logo)
h, w = data.shape[:2]
cx, cy = w // 2, h // 2

print(f"Center pixel: {data[cy, cx]}")
print(f"Top-left corner pixel (background): {data[10, 10]}")

# Sample a 3x3 region in the center
print("Center 3x3 region:")
print(data[cy-1:cy+2, cx-1:cx+2])
