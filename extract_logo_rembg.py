from PIL import Image
import io

input_path = r"C:\Users\nicol\.gemini\antigravity\brain\398bfb6b-4d0b-43da-bbe5-3100fda661f8\media__1776891242855.jpg"
output_path = r"C:\Users\nicol\.gemini\antigravity\scratch\sitio-web-hera\hera-logo-transparent.png"

try:
    from rembg import remove
    
    # Load the image
    with open(input_path, 'rb') as i:
        input_image = i.read()
        
    # Remove background
    output_image = remove(input_image)
    
    # Save output
    img = Image.open(io.BytesIO(output_image))
    
    # Crop to content (non-transparent area)
    bbox = img.getbbox()
    if bbox:
        # Add some padding
        pad = 20
        x1 = max(0, bbox[0] - pad)
        y1 = max(0, bbox[1] - pad)
        x2 = min(img.width, bbox[2] + pad)
        y2 = min(img.height, bbox[3] + pad)
        img = img.crop((x1, y1, x2, y2))
        
    img.save(output_path)
    print(f"Successfully removed background using rembg. Saved to {output_path}")

except ImportError:
    print("rembg library not installed. Please install it first.")
