import sys
import os

def hex_to_rgba(hex_color: str):
    """Convert hex color (#RRGGBB or RRGGBB) to normalized RGBA tuple."""
    hex_color = hex_color.strip().lstrip("#")
    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color: {hex_color}")
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return (r, g, b, 1.0)


def convert_hex_file_to_tres(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as f:
        hex_colors = [line.strip() for line in f if line.strip()]

    colors = []
    for hex_color in hex_colors:
        rgba = hex_to_rgba(hex_color)
        colors.extend(rgba)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write('[gd_resource type="ColorPalette" format=3 uid=""]\n\n')
        f.write("[resource]\n")
        f.write("colors = PackedColorArray(")
        f.write(", ".join(f"{c:.6f}" for c in colors))
        f.write(")\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python hex2tres.py <input_file.hex> [output_file.tres]")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: file '{input_file}' not found.")
        sys.exit(1)

    output_file = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(input_file)[0] + ".tres"

    convert_hex_file_to_tres(input_file, output_file)
    print(f"Converted '{input_file}' -> '{output_file}'")
