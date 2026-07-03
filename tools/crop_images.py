import os
import sys
import glob
from PIL import Image, ImageChops
import concurrent.futures

def crop_image(file_path):
    try:
        if file_path.endswith("-crop.png"):
            return
            
        img = Image.open(file_path).convert("RGB")
        
        # Get background color from top-left pixel
        bg_color = img.getpixel((0, 0))
        bg = Image.new("RGB", img.size, bg_color)
        
        # Find difference
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        
        if bbox:
            left, top, right, bottom = bbox
            pad = 20
            
            # Apply padding
            left = max(0, left - pad)
            top = max(0, top - pad)
            right = min(img.width, right + pad)
            bottom = min(img.height, bottom + pad)
            
            cropped = img.crop((left, top, right, bottom))
            
            crop_path = file_path.replace(".png", "-crop.png")
            cropped.save(crop_path)
            # print(f"Cropped {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Failed to crop {os.path.basename(file_path)}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python crop_images.py <githubFolder>")
        sys.exit(1)
        
    githubFolder = sys.argv[1]
    target_dir = os.path.join(githubFolder, "images", "components")
    
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} not found.")
        sys.exit(1)
        
    files = [f for f in glob.glob(os.path.join(target_dir, "*.png")) if not f.endswith("-crop.png")]
    
    print(f"Found {len(files)} images to crop. Starting parallel crop...")
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(crop_image, files)
        
    print("Cropping complete!")

if __name__ == "__main__":
    main()
