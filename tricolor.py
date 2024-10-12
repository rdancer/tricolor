import argparse
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def hex_to_rgb(hex_str):
    """Convert hex string to RGB tuple."""
    hex_str = hex_str.lstrip("0x").lstrip("#")
    if len(hex_str) == 6:
        return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    else:
        raise ValueError(f"Invalid hex color: {hex_str}")

def rgb_to_lab(color_rgb):
    """Convert RGB color to LAB color space."""
    color = np.uint8([[color_rgb]])
    color_lab = cv2.cvtColor(color, cv2.COLOR_RGB2LAB)
    return color_lab[0][0]

def normalize_color_distribution(lab_image, palette_rgb, target_fraction=1/3):
    """Normalize color assignment so each color occupies roughly one-third of the image."""
    palette_lab = [rgb_to_lab(color) for color in palette_rgb]
    distances = np.zeros((lab_image.shape[0], lab_image.shape[1], 3))
    for i in range(3):
        distances[:, :, i] = np.linalg.norm(lab_image - palette_lab[i], axis=2)
    assignments = np.argmin(distances, axis=2)
    target_pixels = int(target_fraction * lab_image.size / 3)
    for i in range(3):
        excess_pixels = np.sum(assignments == i) - target_pixels
        if excess_pixels > 0:
            reassign_indices = np.argwhere(assignments == i)
            reassign_distances = distances[reassign_indices[:, 0], reassign_indices[:, 1]]
            reassign_colors = np.argsort(reassign_distances[:, (i+1) % 3] + reassign_distances[:, (i+2) % 3])
            for j in reassign_colors[:excess_pixels]:
                assignments[reassign_indices[j][0], reassign_indices[j][1]] = (i + 1) % 3
    normalized_image = np.zeros((lab_image.shape[0], lab_image.shape[1], 3), dtype=np.uint8)
    for i in range(3):
        normalized_image[assignments == i] = palette_rgb[i]
    return normalized_image

def process_image(image_path, colors, plot=False):
    """Process the image with the tricolor normalization and optionally create a plot."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image {image_path}")
        return
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2LAB)
    normalized_image = normalize_color_distribution(image_lab, colors)
    
    # Save the processed image
    filename_base = os.path.splitext(os.path.basename(image_path))[0]
    color_hex = "_".join(f"0x{c[0]:02X}{c[1]:02X}{c[2]:02X}" for c in colors)
    output_filename = f"{filename_base}_{color_hex}.png"
    result_bgr = cv2.cvtColor(normalized_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_filename, result_bgr)
    print(f"Saved: {output_filename}")

    # If plot flag is set, generate the comparative plot
    if plot:
        plot_filename = f"{filename_base}_plot_{color_hex}.png"
        fig, axes = plt.subplots(1, 3, figsize=(20, 7))
        axes[0].imshow(image_rgb)
        axes[0].set_title("Original")

        axes[1].imshow(normalized_image)
        axes[1].set_title("Tricolor")

        # Display color swatches with HEX values
        swatch = np.zeros((100, len(colors) * 100, 3), dtype=np.uint8)
        for kdx, color in enumerate(colors):
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
