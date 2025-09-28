# HEX to Godot `.tres` Palette Converter

A simple Python script that converts HEX palettes into Godot `.tres` files.  
This allows you to easily import color palettes from sites like [Lospec](https://lospec.com/palette-list) or your design tools directly into Godot.

Once converted, you can import the palette in Godot by opening the **Color Picker**, clicking the `...` button next to **Swatches**, and selecting **Open** → choose your `.tres` file.

> ⚠️ The generated file has no UID, so it might be a bit glitchy, but it works.

## Usage

1. Place the Python script next to your HEX file.  
2. Run the script from the terminal:

```bash
python hex2tres.py palette_name.hex
