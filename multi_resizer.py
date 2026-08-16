#!/usr/bin/env python3
import argparse
import os
from PIL import Image

def resize_image(image_path, target_widths, output_dir=None):
    """Resizes a single image into multiple widths, maintaining aspect ratio."""
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    # Set output folder to the same directory as the image if not specified
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(image_path))
    else:
        os.makedirs(output_dir, exist_ok=True)

    filename, ext = os.path.splitext(os.path.basename(image_path))

    try:
        with Image.open(image_path) as img:
            orig_width, orig_height = img.size
            
            for width in target_widths:
                # Calculate height proportionally to maintain aspect ratio
                ratio = width / float(orig_width)
                height = int(float(orig_height) * float(ratio))
                
                # Resize the image using high-quality resampling
                # Note: Resampling=Image.Resampling.LANCZOS replaces deprecated Image.ANTIALIAS
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Create descriptive output filename (e.g., photo_800px.jpg)
                output_name = f"{filename}_{width}px{ext}"
                output_path = os.path.join(output_dir, output_name)
                
                resized_img.save(output_path)
                print(f"Saved: {output_path} ({width}x{height})")
                
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Resize an image into multiple sizes proportionally.")
    
    parser.add_argument(
        "-i", "--image", 
        required=True, 
        help="Path to the input image file"
    )
    parser.add_argument(
        "-s", "--sizes", 
        required=True, 
        help="Comma-separated list of target widths (e.g., 300,600,1200)"
    )
    parser.add_argument(
        "-o", "--output", 
        default=None, 
        help="Directory to save resized images (defaults to input image directory)"
    )

    args = parser.parse_args()

    # Convert comma-separated string argument into a list of integers
    try:
        widths_list = [int(w.strip()) for w in args.sizes.split(",")]
    except ValueError:
        print("Error: Sizes must be a comma-separated list of integers (e.g., 400,800).")
        exit(1)

    resize_image(args.image, widths_list, args.output)

if __name__ == "__main__":
    main()
