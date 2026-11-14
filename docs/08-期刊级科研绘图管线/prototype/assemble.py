#!/usr/bin/env python3
"""Append a footer strip (source / projection / software line) to a PNG figure.

Used as the pipeline's assembly step: GMT/Cartopy render the map, this script
adds the 8 pt footer below the map area instead of fighting GMT text placement
(fig.text with a negative offset falls outside the saved page; positive offset
lands on top of Antarctica). Pure Pillow, no extra dependency.
Usage: python3 prototype/assemble.py <in.png> <footer text> <out.png>
"""
import sys
from PIL import Image, ImageDraw, ImageFont


def assemble(in_path: str, footer: str, out_path: str, strip_h: int = 60,
             font_px: int = 22) -> None:
    """footer may contain one '\\n' for a second line. font_px is in pixels at
    the figure's dpi: at dpi=200, 22 px = 8 pt at the 15 cm print width."""
    img = Image.open(in_path).convert("RGB")
    w, h = img.size
    canvas = Image.new("RGB", (w, h + strip_h), "white")
    canvas.paste(img, (0, 0))
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_px)
    except OSError:
        font = ImageFont.load_default()
    for i, line in enumerate(footer.split("\n")):
        draw.text((16, h + 5 + i * (font_px + 6)), line, fill="black",
                  font=font)
    canvas.save(out_path)
    print("saved", out_path, canvas.size)


if __name__ == "__main__":
    assemble(sys.argv[1], sys.argv[2], sys.argv[3])
