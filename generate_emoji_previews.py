import cairosvg
from PIL import Image
import io
import os

OUT_DIR = "/home/user/Claude/previews"
SIZE = 200

def svg_to_img(path):
    with open(path, 'rb') as f:
        png = cairosvg.svg2png(file_obj=f, output_width=SIZE, output_height=SIZE)
    return Image.open(io.BytesIO(png)).convert("RGBA")

pairs = [
    ("Twemoji Tiger Face + Goat", "twemoji_tiger_face.svg", "twemoji_goat.svg", "emoji_twemoji_face.png"),
    ("Twemoji Tiger Body + Goat", "twemoji_tiger_body.svg", "twemoji_goat.svg", "emoji_twemoji_body.png"),
    ("OpenMoji Tiger Face + Goat", "openmoji_tiger_face.svg", "openmoji_goat.svg", "emoji_openmoji_face.png"),
    ("OpenMoji Tiger Body + Goat", "openmoji_tiger_body.svg", "openmoji_goat.svg", "emoji_openmoji_body.png"),
]

for label, tiger_file, goat_file, out_file in pairs:
    try:
        tiger = svg_to_img(f"{OUT_DIR}/{tiger_file}")
        goat = svg_to_img(f"{OUT_DIR}/{goat_file}")
        combined = Image.new("RGBA", (SIZE * 2 + 60, SIZE + 40), (26, 26, 46, 255))
        combined.paste(tiger, (20, 20), tiger)
        combined.paste(goat, (SIZE + 40, 20), goat)
        combined.save(f"{OUT_DIR}/{out_file}")
        print(f"Saved {out_file}")
    except Exception as e:
        print(f"Error with {label}: {e}")

print("Done!")
