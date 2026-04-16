#!/usr/bin/env python3
"""
fix_figurine_baseline.py  —  shift GoodCompanions2 figurine glyphs onto the baseline.

The figurine glyphs (U+00A2–U+00A7) are copies of the board piece artwork and
currently extend below y=0.  This script translates each one upward by exactly
its descent so the glyph bottom sits on the text baseline (y=0), matching the
behaviour of Merida and SKAKnew.

After the font is fixed the script also:
  • regenerates chess-goodcompanions2-board-fig-raw.pfb / .afm
  • regenerates chess-goodcompanions2-lsb.tfm and chess-goodcompanions2-lsf.tfm
  • installs everything to ~/Library/texmf  (macOS user texmf tree)
  • runs mktexlsr

Usage:
    python3 fix_figurine_baseline.py        # needs fontforge on sys.path
  or
    fontforge -script fix_figurine_baseline.py
"""

import fontforge  # type: ignore
import os
import shutil
import subprocess

# ---------------------------------------------------------------------------
REPO    = os.path.dirname(os.path.abspath(__file__))
TTF     = os.path.join(REPO, "chess-goodcompanions2.ttf")
PFB_BASE = os.path.join(REPO, "chess-goodcompanions2-board-fig-raw")

TEXMF    = os.path.expanduser("~/Library/texmf")
TEXMF_AFM = f"{TEXMF}/fonts/afm/chess/enpassant"
TEXMF_PFB = f"{TEXMF}/fonts/type1/chess/enpassant"
TEXMF_TFM = f"{TEXMF}/fonts/tfm/chess/enpassant"
TEXMF_TTF = f"{TEXMF}/fonts/truetype/chess/enpassant"
TEXMF_ENC = f"{TEXMF}/fonts/enc/dvips/chess"

# Figurine glyphs: (Unicode codepoint, descriptive name)
FIGURINES = [
    (0xA2, "cent     / King"),
    (0xA3, "sterling / Queen"),
    (0xA4, "currency / Knight"),
    (0xA5, "yen      / Bishop"),
    (0xA6, "brokenbar/ Rook"),
    (0xA7, "section  / Pawn"),
]
# ---------------------------------------------------------------------------


def shift_figurines(font):
    """Translate each figurine glyph up so its bounding-box bottom = 0."""
    print("Shifting figurine glyphs:")
    for cp, name in FIGURINES:
        glyph = font[cp]
        xmin, ymin, xmax, ymax = glyph.boundingBox()
        if ymin < 0:
            shift = -int(ymin)          # positive: move up
            glyph.transform((1, 0, 0, 1, 0, shift))
            print(f"  U+{cp:04X}  {name:20s}  "
                  f"was y=[{ymin:.0f}..{ymax:.0f}]  "
                  f"shifted +{shift}  "
                  f"now y=[0..{ymax+shift:.0f}]")
        else:
            print(f"  U+{cp:04X}  {name:20s}  already ≥0, skipped")


def generate_fonts(font):
    """Save modified TTF, PFB, and AFM."""
    font.generate(TTF)
    print(f"\nSaved TTF : {TTF}")

    font.generate(PFB_BASE + ".pfb")
    font.generate(PFB_BASE + ".afm")
    print(f"Generated : {PFB_BASE}.pfb")
    print(f"Generated : {PFB_BASE}.afm")


def generate_tfms():
    """Regenerate both TFM files via afm2tfm."""
    afm = PFB_BASE + ".afm"
    jobs = [
        ("chess-board.enc", "chess-goodcompanions2-lsb"),
        ("chess-fig.enc",   "chess-goodcompanions2-lsf"),
    ]
    print()
    for enc_name, tfm_name in jobs:
        enc  = f"{TEXMF_ENC}/{enc_name}"
        tfm  = os.path.join(REPO, tfm_name + ".tfm")
        cmd  = ["afm2tfm", afm, "-T", enc, tfm]
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ERROR: {result.stderr.strip()}")
        else:
            print(f"  Generated: {tfm}")
            if result.stdout.strip():
                print(f"  {result.stdout.strip()}")


def install_to_texmf():
    """Copy all generated files to ~/Library/texmf."""
    copies = [
        (PFB_BASE + ".afm",                           TEXMF_AFM),
        (PFB_BASE + ".pfb",                           TEXMF_PFB),
        (os.path.join(REPO, "chess-goodcompanions2-lsb.tfm"), TEXMF_TFM),
        (os.path.join(REPO, "chess-goodcompanions2-lsf.tfm"), TEXMF_TFM),
        (TTF,                                         TEXMF_TTF),
    ]
    print("\nInstalling to texmf:")
    for src, dst_dir in copies:
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, os.path.basename(src))
        shutil.copy2(src, dst)
        print(f"  {os.path.basename(src):45s} -> {dst_dir}/")

    print("\nRunning mktexlsr …")
    result = subprocess.run(["mktexlsr", TEXMF], capture_output=True, text=True)
    if result.returncode == 0:
        print("  Done.")
    else:
        print(f"  mktexlsr error: {result.stderr.strip()}")


def main():
    print(f"Opening: {TTF}\n")
    font = fontforge.open(TTF)

    shift_figurines(font)
    generate_fonts(font)
    font.close()

    generate_tfms()
    install_to_texmf()

    print("\nAll done — recompile your .tex file to test.")


if __name__ == "__main__":
    main()
