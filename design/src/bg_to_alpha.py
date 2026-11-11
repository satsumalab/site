"""Cut a render off its plain or gradient background into a transparent PNG.

The background is modelled as a smooth surface (a quadratic in x and y per channel) fitted to the frame's border, so
flat colours and soft studio gradients both work. Each pixel's opacity is how far it sits from that background
(`difference matte`), and the colour is un-mixed from the background, so the cut-out composited back over the original
background reproduces the input. Pixels darker than the background (floor shadows) become translucent black.

    python3 -I design/src/bg_to_alpha.py in.png out.png [--opaque-at 0.22] [--floor 0.03] [--max-side 2000]
"""
import argparse

import numpy as np
from PIL import Image

BORDER = 0.04   # fraction of each side sampled for the background fit


def fit_background(rgb):
    h, w, _ = rgb.shape
    yy, xx = np.mgrid[0:h, 0:w]
    bw, bh = max(2, int(w * BORDER)), max(2, int(h * BORDER))
    border = np.zeros((h, w), bool)
    border[:bh] = border[-bh:] = True
    border[:, :bw] = border[:, -bw:] = True
    x, y = xx / w - 0.5, yy / h - 0.5
    basis = np.stack([np.ones_like(x), x, y, x * x, x * y, y * y], axis=-1)
    keep = border.copy()
    bg = np.zeros_like(rgb)
    for _ in range(3):  # refit, dropping border pixels that belong to the subject
        A = basis[keep]
        for c in range(3):
            coef, *_ = np.linalg.lstsq(A, rgb[..., c][keep], rcond=None)
            bg[..., c] = basis @ coef
        resid = np.abs(rgb - bg).max(axis=-1)
        keep = border & (resid < np.percentile(resid[border], 80) + 0.01)
    return bg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--opaque-at", type=float, default=0.22, help="difference from the background that is fully opaque")
    ap.add_argument("--floor", type=float, default=0.03, help="differences below this are fully transparent")
    ap.add_argument("--max-side", type=int, default=2000)
    a = ap.parse_args()

    im = Image.open(a.inp).convert("RGB")
    if max(im.size) > a.max_side:
        im.thumbnail((a.max_side, a.max_side), Image.LANCZOS)
    rgb = np.asarray(im, dtype=np.float64) / 255.0
    bg = fit_background(rgb)
    diff = rgb - bg
    d = np.abs(diff).max(axis=-1)
    alpha = np.clip((d - a.floor) / (a.opaque_at - a.floor), 0, 1)
    # Un-mix: C = a*F + (1-a)*B  ->  F = B + (C - B) / a
    fg = bg + diff / np.maximum(alpha, 1e-6)[..., None]
    fg = np.where(alpha[..., None] > 0, np.clip(fg, 0, 1), 0)
    out = np.dstack([fg, alpha])
    Image.fromarray(np.round(out * 255).astype(np.uint8), "RGBA").save(a.out, optimize=True)
    print(f"{a.out}: {im.size[0]}x{im.size[1]}, background ~{np.round(np.median(bg.reshape(-1, 3), 0) * 255)}, "
          f"{(alpha == 0).mean():.0%} transparent")


if __name__ == "__main__":
    main()
