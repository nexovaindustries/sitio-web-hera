import cv2
import numpy as np

def create_video(img_path, out_path, duration=5, fps=30):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not read {img_path}")
        return
        
    h, w = img.shape[:2]
    # target size for vertical video
    target_w, target_h = 720, 1280
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path, fourcc, fps, (target_w, target_h))
    
    frames = duration * fps
    
    for i in range(frames):
        # Scale up the image slightly over time (Ken Burns effect)
        scale = 1.0 + (i / frames) * 0.15
        
        # Calculate new size
        new_w = int(w * scale)
        new_h = int(h * scale)
        
        resized = cv2.resize(img, (new_w, new_h))
        
        # Crop center
        start_y = max(0, new_h//2 - target_h//2)
        start_x = max(0, new_w//2 - target_w//2)
        
        cropped = resized[start_y:start_y+target_h, start_x:start_x+target_w]
        
        # If image is too small to crop, pad it
        if cropped.shape[0] < target_h or cropped.shape[1] < target_w:
            padded = np.zeros((target_h, target_w, 3), dtype=np.uint8)
            pad_y = (target_h - cropped.shape[0]) // 2
            pad_x = (target_w - cropped.shape[1]) // 2
            padded[pad_y:pad_y+cropped.shape[0], pad_x:pad_x+cropped.shape[1]] = cropped
            cropped = padded
            
        out.write(cropped)
        
    out.release()
    print(f"Created {out_path}")

create_video('ig1.jpg', 'reel1.mp4')
create_video('ig2.jpg', 'reel2.mp4')
