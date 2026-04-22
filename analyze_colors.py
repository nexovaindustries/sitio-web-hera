from PIL import Image
import numpy as np

# Load the image
img = Image.open(r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg")
img = img.convert("RGBA")
data = np.array(img)

# Let's find pixels that are "cream" (R and G > B, high intensity)
# or just high red component
r = data[:,:,0].astype(int)
g = data[:,:,1].astype(int)
b = data[:,:,2].astype(int)

# Background is blueish: B is dominant.
# The logo is cream: R and G are dominant, or at least much higher than in the background.
# Let's find pixels where R > 150
y_indices, x_indices = np.where(r > 150)
print(f"Found {len(y_indices)} pixels with R > 150.")

if len(y_indices) > 0:
    sample_indices = np.random.choice(len(y_indices), min(5, len(y_indices)), replace=False)
    for idx in sample_indices:
        sx, sy = x_indices[idx], y_indices[idx]
        print(f"Sample at ({sx}, {sy}): {data[sy, sx]}")

# Let's find the bounding box
if len(y_indices) > 0:
    min_x, max_x = np.min(x_indices), np.max(x_indices)
    min_y, max_y = np.min(y_indices), np.max(y_indices)
    print(f"Bounding box: x: {min_x}-{max_x}, y: {min_y}-{max_y}")
