# GoodCompanions2 — Type 1 chess font for LaTeX's `chessboard` package

**GoodCompanions2** is a Type 1 conversion of the freeware [GoodCompanions](http://www.enpassant.dk/chess/fonteng.htm) chess font (by Armando H. Marroquin, 2004), adapted for use with Ulrike Fischer's [`chessboard`](https://ctan.org/pkg/chessboard) and [`chessfss`](https://ctan.org/pkg/chessfss) LaTeX packages using the `LSB1` encoding.

**The generated font files (PFB, AFM, TFM, FD) are ready to install — no need to run the conversion script yourself.**

---

## Preview

The font renders clean, elegant chess pieces with good contrast between light and dark squares:

| Style | Description |
|---|---|
| Pieces | Outline pieces with filled kings and queens |
| Squares | Plain light squares, hatched dark squares |
| Board size | Scales cleanly from 12pt to 36pt+ |

---

## Files

| File | Purpose |
|---|---|
| `chess-goodcompanions2-board-fig-raw.pfb` | Type 1 font binary — **install this** |
| `chess-goodcompanions2-board-fig-raw.afm` | Adobe Font Metrics — **install this** |
| `chess-goodcompanions2-lsb.tfm` | TeX Font Metrics for pdflatex — **install this** |
| `lsb1goodcompanions2.fd` | LaTeX font definition file — **install this** |
| `chess-goodcompanions2.map` | dvips/pdftex map entries — **append to your map** |
| `goodcompanions.ttf` | Original TTF source (needed only to regenerate via `make_gc_pfb.py`) |
| `make_gc_pfb.py` | Conversion script (requires FontForge) |

---

## Installation

### macOS with TeX Live

```bash
# 1. Copy font files into your local texmf tree
TEXMF=~/Library/texmf
cp chess-goodcompanions2-board-fig-raw.pfb  $TEXMF/fonts/type1/chess/enpassant/
cp chess-goodcompanions2-board-fig-raw.afm  $TEXMF/fonts/type1/chess/enpassant/
cp chess-goodcompanions2-board-fig-raw.afm  $TEXMF/fonts/afm/chess/enpassant/
cp chess-goodcompanions2-lsb.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp lsb1goodcompanions2.fd                   $TEXMF/tex/latex/chessfss/enpassant/

# 2. Append map entries to the enpassant map file
cat chess-goodcompanions2.map >> $(kpsewhich chess-enpassant.map)

# 3. Refresh the TeX database and font maps
mktexlsr
updmap --user
```

### Linux with TeX Live

Same as macOS, but `TEXMF` is typically `~/texmf`.

---

## Usage in LaTeX

```latex
\usepackage[LSB1,T1]{fontenc}
\usepackage{chessboard}
\usepackage{chessfss}

\setfigfontfamily{goodcompanions2}

\setchessboard{
  boardfontfamily=goodcompanions2,
  boardfontencoding=LSB1,
  boardfontsize=24pt
}

% Render the starting position
\chessboard[setfen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1]
```

---

## Regenerating the font from source

Requires [FontForge](https://fontforge.org) with its Python extension:

```bash
# Output to current directory (repo root):
python3 make_gc_pfb.py

# Output directly into your texmf tree:
python3 make_gc_pfb.py --output-dir ~/Library/texmf/fonts/type1/chess/enpassant
```

### How the conversion works

The original `goodcompanions.ttf` stores chess glyphs at Latin Unicode codepoints
(e.g. the white king is at U+0030 `zero`, the white queen at U+0047 `G`).
The `chess-board.enc` encoding used by `chessboard` expects glyphs with specific
names at different codepoints (`k`, `K`, `q`, `Q`, etc.).

`make_gc_pfb.py` bridges this gap:
1. Opens the TTF in FontForge
2. Renames each wanted glyph to a temporary name (avoiding collisions)
3. Deletes all other glyphs
4. Renames the survivors to their `chess-board.enc` target names
5. Exports as Type 1 PFB + AFM

The key challenge was that many target glyph names collide with existing Latin
glyph names in the font — the two-step rename-then-delete approach avoids this.

---

## Glyph mapping reference

| Unicode | TTF name | Chess piece |
|---|---|---|
| U+0030 | zero | WKingOnWhite |
| U+0031 | one | WKingOnBlack |
| U+0032 | two | BKingOnWhite |
| U+0033 | three | BKingOnBlack |
| U+0047 | G | WQueenOnWhite |
| U+0048 | H | WQueenOnBlack |
| U+0049 | I | BQueenOnWhite |
| U+004A | J | BQueenOnBlack |
| U+0057 | W | WRookOnWhite |
| U+0058 | X | WRookOnBlack |
| U+0059 | Y | BRookOnWhite |
| U+005A | Z | BRookOnBlack |
| U+006D | m | WBishopOnWhite |
| U+006E | n | WBishopOnBlack |
| U+006F | o | BBishopOnWhite |
| U+0070 | p | BBishopOnBlack |
| U+00A3 | sterling | LightSquare |
| U+00A4 | currency | DarkSquare |
| U+00A9 | copyright | WKnightOnWhite |
| U+00AA | ordfeminine | WKnightOnBlack |
| U+00AB | guillemotleft | BKnightOnWhite |
| U+00AC | logicalnot | BKnightOnBlack |
| U+00B9 | onesuperior | WPawnOnWhite |
| U+00BA | ordmasculine | WPawnOnBlack |
| U+00BB | guillemotright | BPawnOnWhite |
| U+00BC | onequarter | BPawnOnBlack |

---

## License

The original **GoodCompanions** font is freeware, created by Armando H. Marroquin (2004).
It is freely redistributable for non-commercial use.

The conversion files (`make_gc_pfb.py`, `.tfm`, `.fd`, `.map`) are released under the
[MIT License](LICENSE.md) by Joel Cato (2026).
