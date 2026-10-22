"""
Preprocess product reference images into clean 1024x1024 RGB studio cards
for high-accuracy Gemini (Veo) & Google Flow (Omni 1.1 Flash) video generation.
"""
import sys
import shutil
from pathlib import Path
from PIL import Image, ImageOps

TEMP_DIR = Path(r"C:\Users\User\AppData\Local\Temp")


def preprocess_for_ai(in_path: str, out_path: str, crop_box: tuple = None, bg_color=(248, 248, 248)):
    """
    Loads a product image, optionally crops out promotional banners/text (`crop_box`),
    composites onto a clean RGB background (preventing RGBA black-screen bugs),
    centers onto a 1024x1024 studio canvas, and copies to Windows Temp for Chrome MCP upload.
    """
    src = Path(in_path)
    dst = Path(out_path)
    dst.parent.mkdir(parents=True, exist_ok=True)

    im = Image.open(src)
    if crop_box:
        im = im.crop(crop_box)

    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, bg_color)
        bg.paste(im, mask=im.split()[3])
        im = bg
    else:
        im = im.convert("RGB")

    # Fit cleanly inside 1024x1024 canvas with subtle padding so AI sees full frame geometry
    canvas = Image.new("RGB", (1024, 1024), bg_color)
    im.thumbnail((920, 920), Image.Resampling.LANCZOS)
    offset_x = (1024 - im.width) // 2
    offset_y = (1024 - im.height) // 2
    canvas.paste(im, (offset_x, offset_y))

    canvas.save(dst, "JPEG", quality=95)

    # Also copy to Temp whitelist directory
    temp_dst = TEMP_DIR / dst.name
    shutil.copy2(dst, temp_dst)
    print(f"[OK] Saved clean RGB AI reference image: {dst} (and {temp_dst})")
    return dst, temp_dst


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python preprocess_ai_ref.py <input_image> <output_image> [left,top,right,bottom]")
        sys.exit(1)
    in_p = sys.argv[1]
    out_p = sys.argv[2]
    box = tuple(map(int, sys.argv[3].split(","))) if len(sys.argv) > 3 else None
    preprocess_for_ai(in_p, out_p, box)
