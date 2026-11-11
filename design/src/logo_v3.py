"""Build the monochrome Satsuma logo from the traced original (design/logo/traced.json).

Keeps the original's curves: the peel swoosh, the inner swish that loops into the heart,
the leaf and stem, the voxel half and the leaves on the "t". Colour is dropped: everything
is `currentColor`, so the logo takes the colour of the text around it. The wordmark is
Space Grotesk Bold, converted to outlines by Inkscape so it needs no web font.

    python3 -I design/src/logo.py   # needs trace_logo.py run first, plus inkscape and Space Grotesk
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOGO = ROOT / "design/logo"
TRACED = json.loads((LOGO / "traced.json").read_text())

ICON_MAX_X = 1100          # source px: anything right of this is the old wordmark
BIG, SMALL = 56, 37        # voxel sizes in source px (pitch 75)
LEAF_GAP = 14              # knockout between overlapping shapes, source px

# Lockup, in source px. The wordmark keeps the old cap height (~340, baseline 871); the mark is
# scaled down beside it and centred on the letters' x-height band.
WORD_SIZE = 470
WORD_WEIGHT = 600
WORD_BASELINE = 871
MARK_SCALE = 0.72
MARK_RIGHT = 1080          # right edge of the mark's art (voxels)
MARK_CENTRE_Y = 756       # centre of the fruit body (peel spans y 252-1261)
MARK_GAP = 70             # space between mark and wordmark
WORD_X = MARK_RIGHT * MARK_SCALE + MARK_GAP
WORD = "Satsuma"
TRACKING = -14                 # added between every pair, source px
KERN = {"at": 14}              # per-pair optical corrections (Space Grotesk's t crowds the a)
# Leaves on the "t": where the front leaf's base-left corner sits, as fractions of the t's bbox.
T_LEAF_AT = (0.6, 0.05)
PAD = 20  # viewBox margin, source px
COMPACT_PEEL = 44   # extra stroke that thickens the peel in the small-size mark
COMPACT_GAP = 34    # gap between the merged voxels


def shapes(colour, icon):
    return [s for s in TRACED["shapes"] if s["colour"] == colour and (s["bbox"][0] < ICON_MAX_X) == icon]


def voxels():
    rects = []
    for v in TRACED["voxels"]:
        if v["x"] >= ICON_MAX_X:
            continue
        size = BIG if v["w"] > (BIG + SMALL) / 2 else SMALL
        rects.append(f'<rect x="{v["x"]}" y="{v["y"]}" width="{size}" height="{size}"/>')
    return "".join(rects)


def mark_body():
    peel = shapes("orange", True)[0]["d"]
    swish = shapes("yellow", True)[0]["d"]
    leaf = shapes("green", True)[0]["d"]
    stem = shapes("darkgreen", True)[0]["d"]
    return (f'<path id="peel" d="{peel}"/>'
            f'<path id="swish" d="{swish}"/>'
            f'<path id="stem" d="{stem}"/>'
            f'<path id="leaf" d="{leaf}"/>'
            f'<g id="voxels">{voxels()}</g>')


def compact_body():
    """Small-size mark (favicons, under ~48 px): the same traced peel, leaf and stem, thickened,
    with the voxels merged onto a grid twice as coarse and the inner swish and heart left out."""
    peel = shapes("orange", True)[0]["d"]
    leaf = shapes("green", True)[0]["d"]
    stem = shapes("darkgreen", True)[0]["d"]
    x0, y0, pitch = 570, 328, 75          # the original voxel grid (big squares)
    counts = {}
    for v in TRACED["voxels"]:
        if v["x"] >= ICON_MAX_X:
            continue
        cell = (round((v["x"] - x0) / pitch) // 2, round((v["y"] - y0) / pitch) // 2)
        counts[cell] = counts.get(cell, 0) + 1
    size = 2 * pitch - COMPACT_GAP
    rects = "".join(f'<rect x="{x0 + i * 2 * pitch}" y="{y0 + j * 2 * pitch}" width="{size}" height="{size}"/>'
                    for (i, j), n in sorted(counts.items()) if n >= 2)
    thick = 'stroke="currentColor" stroke-linejoin="round"'
    return (f'<path d="{peel}" {thick} stroke-width="{COMPACT_PEEL}"/>'
            f'<path d="{stem}" {thick} stroke-width="{COMPACT_PEEL * 0.8:.0f}"/>'
            f'<path d="{leaf}" {thick} stroke-width="16"/>'
            f'<g id="voxels">{rects}</g>')


def wordmark():
    """Outline 'Satsuma' with Inkscape; returns glyph paths, x shift and the t's bbox, in source px."""
    with tempfile.TemporaryDirectory() as tmp:
        src, out = Path(tmp) / "w.svg", Path(tmp) / "o.svg"
        src.write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" width="3000" height="1300" viewBox="0 0 3000 1300">'
            f'<text x="0" y="{WORD_BASELINE}" style="font-family:\'Space Grotesk\';font-weight:{WORD_WEIGHT};'
            f'font-size:{WORD_SIZE}px">{WORD}</text></svg>')
        subprocess.run(["inkscape", str(src), "--export-text-to-path", "--export-plain-svg",
                        f"--export-filename={out}"], check=True, capture_output=True)
        query = subprocess.run(["inkscape", str(out), "--query-all"], check=True,
                               capture_output=True, text=True).stdout
        paths = re.findall(r'<path\s+d="([^"]+)"', out.read_text())
    boxes = [list(map(float, line.split(",")[1:])) for line in query.splitlines() if line.startswith("path")]
    # Optical spacing on top of the font's kerning: each glyph moves by the sum of the pair
    # adjustments before it.
    offsets, total = [], 0.0
    for i in range(len(WORD)):
        if i:
            total += TRACKING + KERN.get(WORD[i - 1:i + 1], 0)
        offsets.append(total)
    shift = WORD_X - boxes[0][0]
    t = boxes[2]  # S a t s u m a
    right = max(b[0] + b[2] + o for b, o in zip(boxes, offsets)) + shift
    return paths, offsets, shift, (t[0] + offsets[2] + shift, t[1], t[2], t[3]), right


def word_body():
    paths, offsets, shift, (tx, ty, tw, th), right = wordmark()
    glyphs = "".join(f'<path transform="translate({o:.1f} 0)" d="{d}"/>' if o else f'<path d="{d}"/>'
                     for d, o in zip(paths, offsets))
    # Leaves on the t: move the traced pair so they sit on the new t.
    front, back = shapes("green", False)[0], shapes("darkgreen", False)[0]
    anchor = (front["bbox"][0], front["bbox"][1] + front["bbox"][3])  # front leaf, bottom-left
    dx = tx + tw * T_LEAF_AT[0] - anchor[0]
    dy = ty + th * T_LEAF_AT[1] - anchor[1]
    # Mono: the back leaf is knocked out around the front one so the two stay distinct.
    leaves = (f'<g id="t-leaves" transform="translate({dx:.1f} {dy:.1f})">'
              f'<mask id="sx-leafgap" maskUnits="userSpaceOnUse" x="1700" y="300" width="400" height="320">'
              f'<rect x="1700" y="300" width="400" height="320" fill="#fff"/>'
              f'<path d="{front["d"]}" fill="#000" stroke="#000" stroke-width="{LEAF_GAP * 2}" '
              f'stroke-linejoin="round"/></mask>'
              f'<path d="{back["d"]}" mask="url(#sx-leafgap)"/>'
              f'<path d="{front["d"]}"/></g>')
    return f'<g id="wordmark"><g transform="translate({shift:.1f} 0)">{glyphs}</g>{leaves}</g>', right


def svg(view, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" fill="currentColor" '
            f'role="img" aria-label="Satsuma">{body}</svg>\n')


if __name__ == "__main__":
    (LOGO / "v3" / "satsuma-mark.svg").write_text(svg(f"{-PAD} {-PAD} {1100 + 2 * PAD} {1262 + 2 * PAD}", mark_body()))
    (LOGO / "v3" / "satsuma-mark-small.svg").write_text(
        svg(f"{-PAD - 30} {-PAD - 30} {1100 + 2 * PAD + 60} {1262 + 2 * PAD + 60}", compact_body()))
    word, right = word_body()
    # Fruit centre sits a little below the middle of the capitals, as in the old lockup.
    cap_mid = WORD_BASELINE - 170
    dy = cap_mid + 50 * MARK_SCALE - MARK_CENTRE_Y * MARK_SCALE
    mark = f'<g id="mark" transform="translate(0 {dy:.1f}) scale({MARK_SCALE})">{mark_body()}</g>'
    path = LOGO / "v3" / "satsuma-logo.svg"
    path.write_text(svg("0 0 10 10", mark + word))
    # Fit the viewBox to the drawing.
    q = subprocess.run(["inkscape", str(path), "--query-all"], check=True, capture_output=True, text=True)
    x, y, w, h = map(float, q.stdout.splitlines()[0].split(",")[1:])
    path.write_text(svg(f"{x - PAD:.0f} {y - PAD:.0f} {w + 2 * PAD:.0f} {h + 2 * PAD:.0f}", mark + word))
    print("wrote satsuma-mark.svg, satsuma-mark-small.svg, satsuma-logo.svg")
