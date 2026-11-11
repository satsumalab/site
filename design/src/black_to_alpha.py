"""Turn a render on pure black into a transparent PNG that fades into any dark background.

Opacity comes from brightness (the brightest channel, reaching full opacity at OPAQUE_AT), and the
colour is divided back out, so the result composited over black matches the original exactly.

    python3 -I design/src/black_to_alpha.py ch_0.png ch_1.png ch_2.png out.png
    (16-bit greyscale PNGs of the R, G and B channels, e.g. from `convert in.tif -separate ch_%d.png`)
"""
import sys

import numpy as np
from PIL import Image

OPAQUE_AT = 0.3   # channel value (0-1, sRGB-encoded) at and above which a pixel is fully opaque
FLOOR = 0.012     # values below this (film grain on the black) become fully transparent


def load(path):
    return np.asarray(Image.open(path), dtype=np.float64) / 65535.0


def main(r, g, b, out):
    rgb = np.stack([load(r), load(g), load(b)], axis=-1)
    m = rgb.max(axis=-1)
    alpha = np.clip((m - FLOOR) / (OPAQUE_AT - FLOOR), 0, 1)
    colour = np.where(alpha[..., None] > 0, rgb / np.maximum(alpha, 1e-6)[..., None], 0)
    rgba = np.dstack([np.clip(colour, 0, 1), alpha])
    Image.fromarray(np.round(rgba * 255).astype(np.uint8), "RGBA").save(out, optimize=True)
    print(f"wrote {out}: {(alpha == 0).mean():.0%} fully transparent, {(alpha == 1).mean():.0%} opaque")


if __name__ == "__main__":
    main(*sys.argv[1:5])
