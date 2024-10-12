import argparse
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image

def hex_to_rgb(hex_str):
    """Convert hex string to RGB tuple."""
    hex_str = hex_str.removeprefix("0x").lstrip("#")
    if len(hex_str) == 6:
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    else:
        raise ValueError(f"Invalid hex color: {hex_str}")

def posterize_tricolor_classic(image_rgb, dark_color, mid_color, light_color, dark_thresh=85, mid_thresh=170):
    """Posterizes an image by dividing it into three color regions based on intensity thresholds."""
    gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    posterized_image = np.zeros_like(image_rgb)
    posterized_image[gray_image <= dark_thresh] = dark_color
    posterized_image[(gray_image > dark_thresh) & (gray_image <= mid_thresh)] = mid_color
    posterized_image[gray_image > mid_thresh] = light_color
    return posterized_image

def process_image(image_path, colors, plot=False):
    """Process the image with the tricolor posterization and optionally create a plot."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image {image_path}")
        return
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Sort colors by brightness
    sorted_colors = sort_palette_by_brightness(colors)
    
    # Apply the new posterization algorithm
    posterized_image = posterize_tricolor_classic(image_rgb, *sorted_colors)
    
    # Save the processed image
    filename_base = os.path.splitext(os.path.basename(image_path))[0]
    color_hex = "_".join(f"0x{c[0]:02X}{c[1]:02X}{c[2]:02X}" for c in sorted_colors)
    output_filename = f"{filename_base}_{color_hex}.png"
    result_bgr = cv2.cvtColor(posterized_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_filename, result_bgr)
    print(f"Saved: {output_filename}")

    # If plot flag is set, generate the comparative plot
    if plot:
        plot_filename = f"{filename_base}_plot_{color_hex}.png"
        fig, axes = plt.subplots(1, 3, figsize=(20, 7))
        axes[0].imshow(image_rgb)
        axes[0].set_title("Original")

        axes[1].imshow(posterized_image)
        axes[1].set_title("Tricolor Posterization")

        # Display color swatches with HEX values
        swatch = np.zeros((100, len(sorted_colors) * 100, 3), dtype=np.uint8)
        for kdx, color in enumerate(sorted_colors):
            swatch[:, kdx * 100:(kdx + 1) * 100] = color
            hex_value = f"0x{color[0]:02X}{color[1]:02X}{color[2]:02X}"
            contrast_color = "white" if sum(color) / 3 < 128 else "black"
            axes[2].text(10 + 100 * kdx, 75, hex_value, color=contrast_color, fontsize=12, ha="left")
        
        axes[2].imshow(swatch)
        axes[2].set_title("Color Swatches with HEX Values")
        
        for ax in axes:
            ax.axis("off")
        plt.tight_layout()
        plt.savefig(plot_filename)
        plt.close(fig)
        print(f"Saved plot: {plot_filename}")

def sort_palette_by_brightness(palette):
    """Sort a color palette by brightness."""
    brightness = [0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2] for color in palette]
    sorted_palette = [color for _, color in sorted(zip(brightness, palette))]
    return sorted_palette

def main():
    parser = argparse.ArgumentParser(
        description="Apply tricolor posterization to images with specified colors and optional plotting."
    )
    parser.add_argument("images", nargs="+", help="Paths to input image files.")
    parser.add_argument("--color", action="append", required=True, help="Hex color code (e.g., 0x1E2761). Specify exactly three times.")
    parser.add_argument("--plot", action="store_true", help="If set, generates a plot with the original, tricolor image, and color swatches.")
    args = parser.parse_args()
    
    if len(args.color) != 3:
        parser.error("Exactly three colors must be specified with --color.")
    
    try:
        colors_rgb = [hex_to_rgb(color) for color in args.color]
    except ValueError as e:
        parser.error(str(e))

    for image_path in args.images:
        process_image(image_path, colors_rgb, plot=args.plot)

if __name__ == "__main__":
    main()
