"""Build the bold monochrome Satsuma logo (v4).

Mark: a solid circle (the fruit) with the old wordmark's double leaves sprouting from the top.
Wordmark: Space Grotesk SemiBold, outlined by Inkscape, with the old mark's single leaf on the t.
Leaf shapes come from the traced original (design/logo/traced.json, see trace_logo.py).
Everything is `currentColor`, so the logo takes the colour of the text around it.
The previous, traced-fruit version is design/src/logo_v3.py (output in design/logo/v3/).

    python3 -I design/src/logo.py   # needs inkscape and Space Grotesk installed
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOGO = ROOT / "design/logo"
TRACED = json.loads((LOGO / "traced.json").read_text())

# Wordmark, in source px (cap height ~340 above the baseline).
WORD = "Satsuma"
WORD_SIZE = 470
WORD_WEIGHT = 600
WORD_BASELINE = 871
TRACKING = -14                 # added between every pair
KERN = {"at": 14}              # per-pair optical corrections (Space Grotesk's t crowds the a)

# Mark: the circle sits on the baseline like a large letter.
CIRCLE_D = 380
CIRCLE_OVERSHOOT = 8           # how far the circle dips below the baseline
MARK_GAP = 80                  # space between circle and wordmark
LEAVES_HEIGHT = 0.72           # double leaves' height as a fraction of the circle diameter
LEAVES_BASE = (-0.12, 0.0)     # where the leaves' base sits: fraction of D from the circle's centre
STEM_HEIGHT = 0.5              # stem variant: the old mark's stem, as a fraction of D
STEM_BASE = (0.01, -0.03)      # stem's lower end, fraction of D from the leaves' base
KNOCKOUT = 16                  # gap cut around overlapping shapes
# How the leaves show inside the fruit: "outlined" = solid leaves ringed by a cut gap,
# "cutout" = leaves cut out of the fruit, turning solid where they leave it,
# "ring" = large solid leaves over a circular outline that breaks where they cross it.
LEAF_STYLE = "cutout"
RING_WIDTH = 44                # outline weight for the "ring" style
RING_GAP = 22                  # break in the outline either side of the leaves
RING_LEAVES_HEIGHT = 0.9       # leaves are the main element in the "ring" style
RING_LEAVES_BASE = (-0.14, -0.08)

# Single leaf on the t.
T_LEAF_HEIGHT = 150
T_LEAF_AT = (0.55, 0.04)       # leaf base as fractions of the t's bbox

PAD = 20


def shape(colour, x_min, x_max):
    return next(s for s in TRACED["shapes"] if s["colour"] == colour and x_min <= s["bbox"][0] < x_max)


SINGLE_LEAF = shape("green", 0, 1100)          # the old mark's leaf
DOUBLE_FRONT = shape("green", 1100, 9999)      # the old t's leaves
DOUBLE_BACK = shape("darkgreen", 1100, 9999)
STEM = shape("darkgreen", 0, 1100)             # the old mark's stem


def placed(shapes, anchor, to, height):
    """Transform that scales shapes to `height` and moves source point `anchor` onto `to`."""
    top = min(s["bbox"][1] for s in shapes)
    bottom = max(s["bbox"][1] + s["bbox"][3] for s in shapes)
    k = height / (bottom - top)
    return f"translate({to[0] - anchor[0] * k:.1f} {to[1] - anchor[1] * k:.1f}) scale({k:.4f})", k


def knockout(d_list, k):
    """Mask contents that cut a KNOCKOUT-wide gap around the given shapes (drawn at scale k)."""
    return "".join(f'<path d="{d}" fill="#000" stroke="#000" stroke-width="{2 * KNOCKOUT / k:.1f}" '
                   f'stroke-linejoin="round"/>' for d in d_list)


def mark(prefix, style=None, stem=False):
    """Circle with the double leaves (and optionally a stem) sitting mostly inside it, in lockup
    coordinates. Returns (svg body, right edge)."""
    style = style or LEAF_STYLE
    r = CIRCLE_D / 2
    cx, cy = r, WORD_BASELINE + CIRCLE_OVERSHOOT - r
    fb = DOUBLE_FRONT["bbox"]
    base_src = (fb[0] + 8, fb[1] + fb[3] - 4)   # where the two leaves meet
    lb, lh = (RING_LEAVES_BASE, RING_LEAVES_HEIGHT) if style == "ring" else (LEAVES_BASE, LEAVES_HEIGHT)
    base_to = (cx + lb[0] * CIRCLE_D, cy + lb[1] * CIRCLE_D)
    tf, k = placed([DOUBLE_FRONT, DOUBLE_BACK], base_src, base_to, lh * CIRCLE_D)
    front, back = DOUBLE_FRONT["d"], DOUBLE_BACK["d"]
    big = 'x="-5000" y="-5000" width="20000" height="20000"'
    circle = f'cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"'
    gap = f'stroke-width="{2 * KNOCKOUT / k:.1f}" stroke-linejoin="round"'
    stem_hole = stem_solid = ""
    if style == "ring":
        # Solid leaves; the outline (and the back leaf) are cut away around the leaves in front.
        ring_gap = f'stroke-width="{2 * RING_GAP / k:.1f}" stroke-linejoin="round"'
        cut = "".join(f'<path d="{d}" fill="#000" stroke="#000" {ring_gap}/>' for d in (front, back))
        rr = r - RING_WIDTH / 2  # outer edge of the outline stays on the circle
        return (f'<mask id="{prefix}-ring" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                f'<g transform="{tf}">{cut}</g></mask>'
                f'<mask id="{prefix}-back" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                f'<g transform="{tf}">{knockout([front], k)}</g></mask>'
                f'<circle id="fruit" cx="{cx:.1f}" cy="{cy:.1f}" r="{rr:.1f}" fill="none" '
                f'stroke="currentColor" stroke-width="{RING_WIDTH}" mask="url(#{prefix}-ring)"/>'
                f'<g mask="url(#{prefix}-back)"><path id="leaf-back" transform="{tf}" d="{back}"/></g>'
                f'<path id="leaf-front" transform="{tf}" d="{front}"/>'), CIRCLE_D
    if stem:
        if style == "outlined":
            raise SystemExit("the stem variant is only drawn in the cutout style")
        sb = STEM["bbox"]
        stem_to = (base_to[0] + STEM_BASE[0] * CIRCLE_D, base_to[1] + STEM_BASE[1] * CIRCLE_D)
        # anchor: the stem's lower end, where it met the leaf in the old logo
        stf, _ = placed([STEM], (sb[0] + sb[2] - 6, sb[1] + sb[3] - 6), stem_to, STEM_HEIGHT * CIRCLE_D)
        stem_hole = f'<path transform="{stf}" d="{STEM["d"]}" fill="#000"/>'
        stem_solid = f'<path id="stem" transform="{stf}" d="{STEM["d"]}"/>'
    if style == "outlined":
        # Solid leaves; the fruit and the back leaf are cut away around the leaves in front of them.
        masks = (f'<mask id="{prefix}-fruit" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                 f'<g transform="{tf}">{knockout([front, back], k)}</g></mask>'
                 f'<mask id="{prefix}-back" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                 f'<g transform="{tf}">{knockout([front], k)}</g></mask>'
                 f'<mask id="{prefix}-front" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/></mask>')
    else:
        # Leaves are holes in the fruit (with a thin line of fruit between them) and solid outside it.
        masks = (f'<mask id="{prefix}-fruit" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                 f'{stem_hole}<g transform="{tf}"><path d="{back}" fill="#000"/>'
                 f'<path d="{front}" fill="#fff" stroke="#fff" {gap}/><path d="{front}" fill="#000"/></g></mask>'
                 f'<mask id="{prefix}-back" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                 f'<circle {circle} fill="#000"/><g transform="{tf}">{knockout([front], k)}</g></mask>'
                 f'<mask id="{prefix}-front" maskUnits="userSpaceOnUse" {big}><rect {big} fill="#fff"/>'
                 f'<circle {circle} fill="#000"/></mask>')
    body = (masks +
            f'<circle id="fruit" {circle} mask="url(#{prefix}-fruit)"/>'
            # Masks go on untransformed groups: on the transformed path they'd be scaled with it.
            f'<g mask="url(#{prefix}-back)">{stem_solid}<path id="leaf-back" transform="{tf}" d="{back}"/></g>'
            f'<g mask="url(#{prefix}-front)"><path id="leaf-front" transform="{tf}" d="{front}"/></g>')
    return body, CIRCLE_D


def outline_word():
    """Outline WORD with Inkscape; returns glyph paths and their bboxes (at x origin 0)."""
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
    return paths, boxes


def wordmark(x):
    paths, boxes = outline_word()
    # Optical spacing on top of the font's kerning: each glyph moves by the pair adjustments before it.
    offsets, total = [], 0.0
    for i in range(len(WORD)):
        if i:
            total += TRACKING + KERN.get(WORD[i - 1:i + 1], 0)
        offsets.append(total)
    shift = x - boxes[0][0]
    glyphs = "".join(f'<path transform="translate({o:.1f} 0)" d="{d}"/>' if o else f'<path d="{d}"/>'
                     for d, o in zip(paths, offsets))
    tx, ty, tw, th = boxes[2]  # S a t s u m a
    tx += offsets[2] + shift
    b = SINGLE_LEAF["bbox"]
    tf, _ = placed([SINGLE_LEAF], (b[0], b[1] + b[3]), (tx + tw * T_LEAF_AT[0], ty + th * T_LEAF_AT[1]),
                   T_LEAF_HEIGHT)
    return (f'<g id="wordmark"><g transform="translate({shift:.1f} 0)">{glyphs}</g>'
            f'<path id="t-leaf" transform="{tf}" d="{SINGLE_LEAF["d"]}"/></g>')


def write_fitted(path, body, square=False):
    """Write the SVG with its viewBox fitted to the drawing (plus PAD)."""
    head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="{}" fill="currentColor" '
            'role="img" aria-label="Satsuma">')
    path.write_text(head.format("0 0 10 10") + body + "</svg>\n")
    q = subprocess.run(["inkscape", str(path), "--query-all"], check=True, capture_output=True, text=True)
    x, y, w, h = map(float, q.stdout.splitlines()[0].split(",")[1:])
    if square:  # icons get a square box
        side = max(w, h)
        x, y, w, h = x - (side - w) / 2, y - (side - h) / 2, side, side
    path.write_text(head.format(f"{x - PAD:.0f} {y - PAD:.0f} {w + 2 * PAD:.0f} {h + 2 * PAD:.0f}")
                    + body + "</svg>\n")


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]  # optional: outlined | cutout | ring, and "stem" for the stem variant
    style = next((a for a in args if a in ("outlined", "cutout", "ring")), LEAF_STYLE)
    stem = "stem" in args
    suffix = ("-stem" if stem else "") + ("-ring" if style == "ring" else "")
    body, _ = mark("sx-mark", style, stem)
    write_fitted(LOGO / f"satsuma-mark{suffix}.svg", body, square=True)
    body, width = mark("sx-logo", style, stem)
    write_fitted(LOGO / f"satsuma-logo{suffix}.svg", body + wordmark(width + MARK_GAP))
    print(f"wrote satsuma-mark{suffix}.svg, satsuma-logo{suffix}.svg")
