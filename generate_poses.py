import cairosvg
from PIL import Image
import io
import os

OUT_DIR = "/home/user/Claude/previews"
os.makedirs(OUT_DIR, exist_ok=True)

SIZE = 200

# ============ TIGER STANDING (front-facing, full body) ============
tiger_standing = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="ts1" cx="50%" cy="35%" r="50%"><stop offset="0%" stop-color="#f0a030"/><stop offset="100%" stop-color="#c07010"/></radialGradient></defs>
<!-- Body -->
<ellipse cx="32" cy="36" rx="16" ry="12" fill="url(#ts1)"/>
<!-- Belly -->
<ellipse cx="32" cy="38" rx="10" ry="8" fill="#ffe8cc" opacity="0.7"/>
<!-- Body stripes -->
<path d="M20 30 Q22 36 20 42" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M26 28 Q27 36 26 44" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M38 28 Q37 36 38 44" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M44 30 Q42 36 44 42" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<!-- Front legs -->
<rect x="22" y="44" width="5" height="12" rx="2" fill="#d08020"/>
<rect x="37" y="44" width="5" height="12" rx="2" fill="#d08020"/>
<!-- Back legs (slightly behind) -->
<rect x="18" y="43" width="5" height="13" rx="2" fill="#b06010"/>
<rect x="41" y="43" width="5" height="13" rx="2" fill="#b06010"/>
<!-- Paws -->
<ellipse cx="20.5" cy="56" rx="3.5" ry="2" fill="#b06010"/>
<ellipse cx="24.5" cy="56" rx="3.5" ry="2" fill="#d08020"/>
<ellipse cx="39.5" cy="56" rx="3.5" ry="2" fill="#d08020"/>
<ellipse cx="43.5" cy="56" rx="3.5" ry="2" fill="#b06010"/>
<!-- Head -->
<circle cx="32" cy="18" r="12" fill="#e89030"/>
<!-- Ears -->
<circle cx="22" cy="8" r="5" fill="#d07820"/>
<circle cx="42" cy="8" r="5" fill="#d07820"/>
<circle cx="22" cy="8" r="3" fill="#ffb060"/>
<circle cx="42" cy="8" r="3" fill="#ffb060"/>
<!-- Head stripes -->
<path d="M26 6 L27 14" stroke="#4a2000" stroke-width="2.5" stroke-linecap="round"/>
<path d="M32 4 L32 12" stroke="#4a2000" stroke-width="3" stroke-linecap="round"/>
<path d="M38 6 L37 14" stroke="#4a2000" stroke-width="2.5" stroke-linecap="round"/>
<!-- Cheek patches -->
<ellipse cx="32" cy="22" rx="9" ry="6" fill="#ffe0b0" opacity="0.8"/>
<!-- Eyes -->
<ellipse cx="26" cy="16" rx="3.5" ry="3" fill="white"/>
<ellipse cx="38" cy="16" rx="3.5" ry="3" fill="white"/>
<ellipse cx="26.5" cy="16" rx="2" ry="2.5" fill="#ffd700"/>
<ellipse cx="38.5" cy="16" rx="2" ry="2.5" fill="#ffd700"/>
<ellipse cx="27" cy="16" rx="1" ry="2.5" fill="#111"/>
<ellipse cx="39" cy="16" rx="1" ry="2.5" fill="#111"/>
<circle cx="25.5" cy="14.5" r="1" fill="white" opacity="0.9"/>
<circle cx="37.5" cy="14.5" r="1" fill="white" opacity="0.9"/>
<!-- Nose -->
<path d="M29 21 L32 19 L35 21 Q33 23 31 23 Q29 23 29 21Z" fill="#2a1200"/>
<!-- Mouth -->
<path d="M32 23 L32 25" stroke="#2a1200" stroke-width="1.2"/>
<path d="M29 25.5 Q32 27.5 35 25.5" stroke="#2a1200" stroke-width="1.2" fill="none"/>
<!-- Whiskers -->
<line x1="24" y1="22" x2="14" y2="20" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<line x1="24" y1="23" x2="14" y2="24" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<line x1="40" y1="22" x2="50" y2="20" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<line x1="40" y1="23" x2="50" y2="24" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<!-- Tail -->
<path d="M48 34 Q54 30 56 24 Q58 20 56 18" stroke="#d08020" stroke-width="3.5" fill="none" stroke-linecap="round"/>
<path d="M56 18 Q54 16 56 15" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
</svg>'''

# ============ TIGER WALKING ============
tiger_walking = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="tw1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0a030"/><stop offset="100%" stop-color="#c07010"/></linearGradient></defs>
<!-- Tail -->
<path d="M8 24 Q2 18 4 12 Q6 8 8 10" stroke="#d08020" stroke-width="3.5" fill="none" stroke-linecap="round"/>
<path d="M4 12 Q5 9 7 10" stroke="#4a2000" stroke-width="1.5" fill="none"/>
<!-- Body -->
<ellipse cx="30" cy="30" rx="20" ry="11" fill="url(#tw1)"/>
<!-- Belly -->
<ellipse cx="30" cy="33" rx="14" ry="6" fill="#ffe8cc" opacity="0.6"/>
<!-- Body stripes -->
<path d="M16 24 Q18 30 16 36" stroke="#4a2000" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<path d="M22 22 Q23 30 22 38" stroke="#4a2000" stroke-width="2.2" fill="none" stroke-linecap="round"/>
<path d="M28 21 Q29 30 28 39" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M34 22 Q35 30 34 38" stroke="#4a2000" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M40 24 Q41 30 40 36" stroke="#4a2000" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<!-- Back legs (walking) -->
<path d="M14 38 L10 52" stroke="#b06010" stroke-width="4.5" fill="none" stroke-linecap="round"/>
<path d="M20 38 L24 52" stroke="#c07818" stroke-width="4.5" fill="none" stroke-linecap="round"/>
<!-- Front legs (walking) -->
<path d="M36 38 L32 52" stroke="#c07818" stroke-width="4.5" fill="none" stroke-linecap="round"/>
<path d="M42 37 L46 50" stroke="#b06010" stroke-width="4.5" fill="none" stroke-linecap="round"/>
<!-- Paws -->
<ellipse cx="10" cy="53" rx="3" ry="2" fill="#b06010"/>
<ellipse cx="24" cy="53" rx="3" ry="2" fill="#c07818"/>
<ellipse cx="32" cy="53" rx="3" ry="2" fill="#c07818"/>
<ellipse cx="46" cy="51" rx="3" ry="2" fill="#b06010"/>
<!-- Head -->
<circle cx="50" cy="22" r="11" fill="#e89030"/>
<!-- Ears -->
<circle cx="44" cy="12" r="4" fill="#d07820"/>
<circle cx="56" cy="12" r="4" fill="#d07820"/>
<circle cx="44" cy="12" r="2.5" fill="#ffb060"/>
<circle cx="56" cy="12" r="2.5" fill="#ffb060"/>
<!-- Head stripes -->
<path d="M46 8 L47 14" stroke="#4a2000" stroke-width="2" stroke-linecap="round"/>
<path d="M50 6 L50 14" stroke="#4a2000" stroke-width="2.5" stroke-linecap="round"/>
<path d="M54 8 L53 14" stroke="#4a2000" stroke-width="2" stroke-linecap="round"/>
<!-- Muzzle -->
<ellipse cx="50" cy="26" rx="7" ry="5" fill="#ffe0b0" opacity="0.8"/>
<!-- Eye -->
<ellipse cx="46" cy="20" rx="3" ry="2.5" fill="white"/>
<ellipse cx="55" cy="20" rx="2.5" ry="2" fill="white"/>
<ellipse cx="46.5" cy="20" rx="1.8" ry="2" fill="#ffd700"/>
<ellipse cx="55" cy="20" rx="1.5" ry="1.5" fill="#ffd700"/>
<ellipse cx="47" cy="20" rx="0.8" ry="2" fill="#111"/>
<ellipse cx="55.2" cy="20" rx="0.7" ry="1.5" fill="#111"/>
<circle cx="45.5" cy="18.5" r="0.8" fill="white" opacity="0.9"/>
<!-- Nose -->
<path d="M49 24 L51 22.5 L53 24 Q52 25.5 50 25.5 Q49 25.5 49 24Z" fill="#2a1200"/>
<!-- Mouth -->
<path d="M48 27 Q50 28.5 53 27" stroke="#2a1200" stroke-width="1" fill="none"/>
<!-- Whiskers -->
<line x1="56" y1="24" x2="64" y2="22" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
<line x1="56" y1="25" x2="64" y2="26" stroke="#4a2000" stroke-width="0.8" opacity="0.5"/>
</svg>'''

# ============ GOAT STANDING (front-facing, full body) ============
goat_standing = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><radialGradient id="gs1" cx="50%" cy="40%" r="50%"><stop offset="0%" stop-color="#f5f0e8"/><stop offset="100%" stop-color="#c8c0b0"/></radialGradient></defs>
<!-- Horns -->
<path d="M24 10 Q20 0 16 -4" stroke="#887766" stroke-width="3.5" fill="none" stroke-linecap="round"/>
<path d="M40 10 Q44 0 48 -4" stroke="#887766" stroke-width="3.5" fill="none" stroke-linecap="round"/>
<path d="M23 8 Q20 1 17 -3" stroke="#bbaa99" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M41 8 Q44 1 47 -3" stroke="#bbaa99" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<!-- Head -->
<ellipse cx="32" cy="16" rx="11" ry="10" fill="#e8e0d4"/>
<!-- Ears -->
<ellipse cx="18" cy="16" rx="6" ry="3" fill="#d8c8b8" transform="rotate(-20 18 16)"/>
<ellipse cx="46" cy="16" rx="6" ry="3" fill="#d8c8b8" transform="rotate(20 46 16)"/>
<ellipse cx="18" cy="16" rx="4" ry="2" fill="#f0c0b0" transform="rotate(-20 18 16)"/>
<ellipse cx="46" cy="16" rx="4" ry="2" fill="#f0c0b0" transform="rotate(20 46 16)"/>
<!-- Tuft on head -->
<path d="M28 8 Q30 4 32 8 Q34 4 36 8" stroke="#d4ccc0" stroke-width="1.5" fill="none"/>
<!-- Eyes -->
<ellipse cx="26" cy="14" rx="3.5" ry="3" fill="white"/>
<ellipse cx="38" cy="14" rx="3.5" ry="3" fill="white"/>
<ellipse cx="26" cy="14" rx="2.5" ry="2.5" fill="#886633"/>
<ellipse cx="38" cy="14" rx="2.5" ry="2.5" fill="#886633"/>
<rect x="24" y="13" width="4" height="2" rx="0.3" fill="#332211"/>
<rect x="36" y="13" width="4" height="2" rx="0.3" fill="#332211"/>
<circle cx="25" cy="12.5" r="1" fill="white" opacity="0.8"/>
<circle cx="37" cy="12.5" r="1" fill="white" opacity="0.8"/>
<!-- Nose/Nostrils -->
<path d="M29 20 Q28 22 29.5 22.5" stroke="#6a4a3a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M35 20 Q36 22 34.5 22.5" stroke="#6a4a3a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<!-- Mouth -->
<path d="M29 24 Q32 26 35 24" stroke="#6a4a3a" stroke-width="1" fill="none"/>
<!-- Body -->
<ellipse cx="32" cy="36" rx="14" ry="12" fill="url(#gs1)"/>
<!-- Belly -->
<ellipse cx="32" cy="38" rx="9" ry="8" fill="white" opacity="0.3"/>
<!-- Front legs -->
<rect x="24" y="44" width="4" height="14" rx="1.5" fill="#d0c8bc"/>
<rect x="36" y="44" width="4" height="14" rx="1.5" fill="#d0c8bc"/>
<!-- Back legs -->
<rect x="20" y="43" width="4" height="15" rx="1.5" fill="#b8b0a4"/>
<rect x="40" y="43" width="4" height="15" rx="1.5" fill="#b8b0a4"/>
<!-- Hooves -->
<rect x="19" y="56" width="6" height="3" rx="1" fill="#555"/>
<rect x="23" y="56" width="6" height="3" rx="1" fill="#555"/>
<rect x="35" y="56" width="6" height="3" rx="1" fill="#555"/>
<rect x="39" y="56" width="6" height="3" rx="1" fill="#555"/>
<!-- Beard -->
<path d="M30 25 Q28 32 27 36" stroke="#c0b8a8" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M32 26 Q31 33 30 38" stroke="#c0b8a8" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.5"/>
<path d="M34 25 Q36 32 37 36" stroke="#c0b8a8" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
<!-- Tail -->
<path d="M46 32 Q50 28 48 24" stroke="#c0b8a8" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</svg>'''

# ============ GOAT WALKING ============
goat_walking = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="gw1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f0ece4"/><stop offset="100%" stop-color="#c8c0b0"/></linearGradient></defs>
<!-- Tail -->
<path d="M8 26 Q4 22 6 18" stroke="#c0b8a8" stroke-width="2.5" fill="none" stroke-linecap="round"/>
<!-- Body -->
<ellipse cx="28" cy="30" rx="18" ry="10" fill="url(#gw1)"/>
<!-- Belly -->
<ellipse cx="28" cy="33" rx="12" ry="5" fill="white" opacity="0.3"/>
<!-- Back legs (walking) -->
<path d="M14 38 L10 52" stroke="#b8b0a4" stroke-width="4" fill="none" stroke-linecap="round"/>
<path d="M20 38 L24 52" stroke="#c8c0b4" stroke-width="4" fill="none" stroke-linecap="round"/>
<!-- Front legs (walking) -->
<path d="M34 37 L30 52" stroke="#c8c0b4" stroke-width="4" fill="none" stroke-linecap="round"/>
<path d="M40 36 L44 50" stroke="#b8b0a4" stroke-width="4" fill="none" stroke-linecap="round"/>
<!-- Hooves -->
<rect x="8" y="52" width="5" height="3" rx="1" fill="#555"/>
<rect x="22" y="52" width="5" height="3" rx="1" fill="#555"/>
<rect x="28" y="52" width="5" height="3" rx="1" fill="#555"/>
<rect x="42" y="50" width="5" height="3" rx="1" fill="#555"/>
<!-- Head -->
<ellipse cx="48" cy="22" rx="10" ry="9" fill="#e8e0d4"/>
<!-- Horns -->
<path d="M44 14 Q40 6 38 0" stroke="#887766" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M52 12 Q56 4 58 -2" stroke="#887766" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M43 12 Q40 6 39 1" stroke="#bbaa99" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<path d="M53 11 Q56 5 57 -1" stroke="#bbaa99" stroke-width="1.5" fill="none" stroke-linecap="round"/>
<!-- Ear -->
<ellipse cx="40" cy="18" rx="5" ry="2.5" fill="#d8c8b8" transform="rotate(-15 40 18)"/>
<ellipse cx="40" cy="18" rx="3.5" ry="1.5" fill="#f0c0b0" transform="rotate(-15 40 18)"/>
<!-- Eye -->
<ellipse cx="45" cy="20" rx="3" ry="2.5" fill="white"/>
<ellipse cx="53" cy="20" rx="2.5" ry="2" fill="white"/>
<ellipse cx="45" cy="20" rx="2" ry="2" fill="#886633"/>
<ellipse cx="53" cy="20" rx="1.8" ry="1.5" fill="#886633"/>
<rect x="44" y="19.5" width="3" height="1.5" rx="0.2" fill="#332211"/>
<rect x="52" y="19.5" width="2.5" height="1.3" rx="0.2" fill="#332211"/>
<circle cx="44" cy="19" r="0.8" fill="white" opacity="0.8"/>
<!-- Nose -->
<ellipse cx="56" cy="24" rx="2" ry="1.5" fill="#8a6a5a"/>
<!-- Mouth -->
<path d="M54 27 Q56 28.5 58 27" stroke="#6a4a3a" stroke-width="1" fill="none"/>
<!-- Beard -->
<path d="M50 28 Q48 34 46 38" stroke="#c0b8a8" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
<path d="M52 29 Q50 35 49 40" stroke="#c0b8a8" stroke-width="2.5" fill="none" stroke-linecap="round" opacity="0.5"/>
</svg>'''

poses = [
    ("Tiger Standing", tiger_standing, "Goat Standing", goat_standing, "standing"),
    ("Tiger Walking", tiger_walking, "Goat Walking", goat_walking, "walking"),
]

for tname, tsvg, gname, gsvg, fname in poses:
    tiger_png = cairosvg.svg2png(bytestring=tsvg.encode(), output_width=SIZE, output_height=SIZE)
    tiger_img = Image.open(io.BytesIO(tiger_png)).convert("RGBA")
    goat_png = cairosvg.svg2png(bytestring=gsvg.encode(), output_width=SIZE, output_height=SIZE)
    goat_img = Image.open(io.BytesIO(goat_png)).convert("RGBA")

    combined = Image.new("RGBA", (SIZE * 2 + 60, SIZE + 40), (26, 26, 46, 255))
    combined.paste(tiger_img, (20, 20), tiger_img)
    combined.paste(goat_img, (SIZE + 40, 20), goat_img)
    combined.save(f"{OUT_DIR}/pose_{fname}.png")
    print(f"Saved pose_{fname}.png")

print("Done!")
