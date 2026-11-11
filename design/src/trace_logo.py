"""Trace the original raster logo (assets/media/logo.png) into smooth vector shapes.

Each colour region is split into connected shapes. Small square ones are recorded as voxels
(position and size); everything else is outlined and fitted with cubic Béziers
(Schneider's curve-fitting algorithm), keeping sharp corners such as leaf tips.

    python3 design/src/trace_logo.py   # writes design/logo/traced.json
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage
from skimage import measure

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "assets/media/logo.png"
OUT = ROOT / "design/logo/traced.json"

PALETTE = {
    "orange": (240, 140, 0),
    "yellow": (252, 211, 77),
    "grey": (211, 211, 211),
    "green": (134, 195, 67),
    "darkgreen": (108, 148, 38),
}
FIT_ERROR = 2.0       # px, in the source image
CORNER_DEG = 75       # turning angle that counts as a corner
CORNER_SPAN = 14     # contour points either side used to measure turning


# ----------------------------------------------------------------- Bézier fitting (Schneider) --

def _norm(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-12 else v


def _bez(ctrl, t):
    t = np.asarray(t)[:, None]
    mt = 1 - t
    return mt ** 3 * ctrl[0] + 3 * mt ** 2 * t * ctrl[1] + 3 * mt * t ** 2 * ctrl[2] + t ** 3 * ctrl[3]


def _bez_d1(ctrl, t):
    t = np.asarray(t)[:, None]
    mt = 1 - t
    return 3 * mt ** 2 * (ctrl[1] - ctrl[0]) + 6 * mt * t * (ctrl[2] - ctrl[1]) + 3 * t ** 2 * (ctrl[3] - ctrl[2])


def _bez_d2(ctrl, t):
    t = np.asarray(t)[:, None]
    return 6 * (1 - t) * (ctrl[2] - 2 * ctrl[1] + ctrl[0]) + 6 * t * (ctrl[3] - 2 * ctrl[2] + ctrl[1])


def _chord_params(pts):
    d = np.r_[0, np.cumsum(np.linalg.norm(np.diff(pts, axis=0), axis=1))]
    return d / d[-1]


def _generate(pts, u, t1, t2):
    p0, p3 = pts[0], pts[-1]
    a1 = t1[None, :] * (3 * (1 - u) ** 2 * u)[:, None]
    a2 = t2[None, :] * (3 * (1 - u) * u ** 2)[:, None]
    c = np.array([[np.sum(a1 * a1), np.sum(a1 * a2)], [np.sum(a1 * a2), np.sum(a2 * a2)]])
    base = _bez(np.array([p0, p0, p3, p3]), u)
    tmp = pts - base
    x = np.array([np.sum(a1 * tmp), np.sum(a2 * tmp)])
    det = c[0, 0] * c[1, 1] - c[0, 1] * c[1, 0]
    seg = np.linalg.norm(p3 - p0)
    if abs(det) > 1e-12:
        al1 = (x[0] * c[1, 1] - c[0, 1] * x[1]) / det
        al2 = (c[0, 0] * x[1] - x[0] * c[1, 0]) / det
    else:
        al1 = al2 = seg / 3
    if al1 < 1e-6 * seg or al2 < 1e-6 * seg:
        al1 = al2 = seg / 3
    return np.array([p0, p0 + t1 * al1, p3 + t2 * al2, p3])


def _reparam(ctrl, pts, u):
    q, q1, q2 = _bez(ctrl, u), _bez_d1(ctrl, u), _bez_d2(ctrl, u)
    num = np.sum((q - pts) * q1, axis=1)
    den = np.sum(q1 * q1 + (q - pts) * q2, axis=1)
    out = u - np.where(np.abs(den) > 1e-12, num / den, 0)
    return np.clip(out, 0, 1)


def _max_err(ctrl, pts, u):
    d = np.linalg.norm(_bez(ctrl, u) - pts, axis=1)
    i = int(np.argmax(d))
    return d[i], i


def _fit(pts, t1, t2, err):
    if len(pts) == 2:
        dist = np.linalg.norm(pts[1] - pts[0]) / 3
        return [np.array([pts[0], pts[0] + t1 * dist, pts[1] + t2 * dist, pts[1]])]
    u = _chord_params(pts)
    ctrl = _generate(pts, u, t1, t2)
    e, split = _max_err(ctrl, pts, u)
    if e < err:
        return [ctrl]
    if e < err * 4:
        for _ in range(20):
            u = _reparam(ctrl, pts, u)
            ctrl = _generate(pts, u, t1, t2)
            e, split = _max_err(ctrl, pts, u)
            if e < err:
                return [ctrl]
    split = min(max(split, 1), len(pts) - 2)
    tc = _norm(pts[split - 1] - pts[split + 1])
    return _fit(pts[:split + 1], t1, tc, err) + _fit(pts[split:], -tc, t2, err)


def fit_open(pts, err):
    pts = np.asarray(pts, float)
    k = min(3, len(pts) - 1)
    t1 = _norm(pts[k] - pts[0])
    t2 = _norm(pts[-1 - k] - pts[-1])
    return _fit(pts, t1, t2, err)


# ---------------------------------------------------------------------------- contour tracing --

def corners(pts):
    n = len(pts)
    k = CORNER_SPAN
    ang = np.zeros(n)
    for i in range(n):
        a = _norm(pts[i] - pts[(i - k) % n])
        b = _norm(pts[(i + k) % n] - pts[i])
        ang[i] = np.degrees(np.arccos(np.clip(np.dot(a, b), -1, 1)))
    out = []
    for i in range(n):
        if ang[i] > CORNER_DEG and ang[i] == max(ang[(i + j) % n] for j in range(-k, k + 1)):
            out.append(i)
    return out


def trace(mask):
    """Closed outlines of a binary mask (outer contours and holes) as SVG path data."""
    m = ndimage.gaussian_filter(np.pad(mask, 4).astype(float), 2.5)
    parts = []
    for c in measure.find_contours(m, 0.5):
        if len(c) < 12:
            continue
        pts = c[:, ::-1] - 4  # (row, col) -> (x, y), undo padding
        if np.allclose(pts[0], pts[-1]):
            pts = pts[:-1]
        cs = corners(pts)
        if not cs:
            cs = [0]
        segs = []
        for j, s in enumerate(cs):
            e = cs[(j + 1) % len(cs)]
            idx = list(range(s, e + 1)) if e > s else list(range(s, len(pts))) + list(range(0, e + 1))
            segs += fit_open(pts[idx], FIT_ERROR)
        d = f"M{segs[0][0][0]:.1f} {segs[0][0][1]:.1f}"
        for b in segs:
            d += "C" + " ".join(f"{p[0]:.1f} {p[1]:.1f}" for p in b[1:])
        parts.append(d + "Z")
    return "".join(parts)


def main():
    rgba = np.array(Image.open(SRC).convert("RGBA")).astype(int)
    opaque = rgba[..., 3] > 128
    cols = np.array(list(PALETTE.values()))
    dist = ((rgba[..., None, :3] - cols[None, None]) ** 2).sum(-1)
    label_of = np.argmin(dist, axis=-1)

    shapes, voxels = [], []
    for ci, name in enumerate(PALETTE):
        mask = opaque & (label_of == ci)
        mask = ndimage.binary_opening(mask, iterations=1)
        lab, n = ndimage.label(mask)
        for i, sl in enumerate(ndimage.find_objects(lab), start=1):
            region = lab[sl] == i
            h, w = region.shape
            area = region.sum()
            if area < 150:
                continue
            x0, y0 = sl[1].start, sl[0].start
            squareish = 0.8 < w / h < 1.25 and area / (w * h) > 0.9 and max(w, h) < 90
            if squareish:
                voxels.append(dict(colour=name, x=x0, y=y0, w=w, h=h))
                continue
            full = np.zeros_like(mask)
            full[sl] = region
            shapes.append(dict(colour=name, bbox=[x0, y0, w, h], d=trace(full)))
            print(f"{name:9s} shape bbox=({x0},{y0},{w},{h})")
    print(len(voxels), "voxels")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(dict(size=list(rgba.shape[1::-1]), shapes=shapes, voxels=voxels)))


if __name__ == "__main__":
    main()
