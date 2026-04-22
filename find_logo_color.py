from PIL import Image
import numpy as np

# Load the image
img = Image.open(r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg")
img = img.convert("RGBA")
data = np.array(img)

# Find brightest pixels
brightness = data[:,:,0].astype(int) + data[:,:,1].astype(int) + data[:,:,2].astype(int)
max_brightness = np.max(brightness)
print(f"Max brightness: {max_brightness}")

y_indices, x_indices = np.where(brightness > max_brightness - 20)
print(f"Found {len(y_indices)} pixels near max brightness.")

if len(y_indices) > 0:
    sample_x, sample_y = x_indices[0], y_indices[0]
    print(f"Sample bright pixel at ({sample_x}, {sample_y}): {data[sample_y, sample_x]}")
    
    # Find bounding box of bright pixels
    print(f"Bright pixels bounding box: x: {np.min(x_indices)}-{np.max(x_indices)}, y: {np.min(y_indices)}-{np.max(y_indices)}")
