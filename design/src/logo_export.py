"""Write the ring logo and mark in fixed colourways (design/logo/export/).

The master SVGs draw in `currentColor`; these copies bake colours in, so they work as plain
image files (<img>, slides, print) where currentColor isn't available.

    python3 -I design/src/logo_export.py   # after logo.py ring
"""
from pathlib import Path

LOGO = Path(__file__).resolve().parents[2] / "design/logo"
OUT = LOGO / "export"

INK, PAPER = "#0b0d10", "#ffffff"
ORANGE, LEAF, DEEP_LEAF = "#f28c00", "#86c343", "#5c8a26"

# name: (wordmark/default colour, ring, front leaf, back leaf)
COLOURWAYS = {
    "colour-on-light": (INK, ORANGE, LEAF, DEEP_LEAF),
    "colour-on-dark": ("#e9e7e2", ORANGE, LEAF, DEEP_LEAF),
    "ink": (INK, INK, INK, INK),
    "paper": (PAPER, PAPER, PAPER, PAPER),
}


def recolour(svg, word, ring, front, back):
    style = (f"<style>#fruit{{stroke:{ring}}}#leaf-front,#t-leaf{{fill:{front}}}"
             f"#leaf-back{{fill:{back}}}</style>")
    svg = svg.replace('fill="currentColor"', f'fill="{word}" color="{word}"', 1)
    return svg.replace(">", ">" + style, 1)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for kind in ("logo", "mark"):
        master = (LOGO / f"satsuma-{kind}-ring.svg").read_text()
        for name, colours in COLOURWAYS.items():
            (OUT / f"satsuma-{kind}-{name}.svg").write_text(recolour(master, *colours))
    print("wrote", len(list(OUT.glob("*.svg"))), "files to", OUT)
