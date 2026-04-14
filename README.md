# GoodCompanions2 — Chess font for LaTeX's `chessboard` package

Joel Cato's [`chessboard`](https://ctan.org/pkg/chessboard) / [`chessfss`](https://ctan.org/pkg/chessfss) adaptation of the [GoodCompanions](http://www.enpassant.dk/chess/fonteng.htm) chess font by Armando H. Marroquin (2004).

See **[sample.pdf](sample.pdf)** for a preview showing all encodings and color options.

---

## What's in this repo

| File | Purpose |
|---|---|
| `chess-goodcompanions2.ttf` | The font, with glyphs pre-renamed for `chess-board.enc` — start here |
| `sample.tex` | Gallery page demonstrating LSB1/LSB2/LSB3/LSF encodings |
| `sample.pdf` | Pre-built gallery PDF |

---

## Prerequisites

You'll need a working TeX Live (or MiKTeX) installation with the following CTAN packages:

- [`chessboard`](https://ctan.org/pkg/chessboard)
- [`chessfss`](https://ctan.org/pkg/chessfss)
- [`enpassant`](https://ctan.org/pkg/enpassant) — provides `chess-board.enc` and the font infrastructure

Install via TeX Live:

```bash
tlmgr install chessboard chessfss enpassant
```

---

## Installation

The TTF must be converted to Type 1 (PFB) and the TeX support files installed. Requires [FontForge](https://fontforge.org).

### 1. Convert TTF → PFB + AFM

```bash
fontforge -lang=ff -c '
  Open("chess-goodcompanions2.ttf");
  Generate("chess-goodcompanions2-board-fig-raw.pfb");
'
```

This produces `chess-goodcompanions2-board-fig-raw.pfb` and `chess-goodcompanions2-board-fig-raw.afm`.

### 2. Generate TFM files

```bash
# LSB encoding (board squares + pieces)
afm2tfm chess-goodcompanions2-board-fig-raw.afm \
  -T $(kpsewhich chess-board.enc) \
  chess-goodcompanions2-lsb

# LSF encoding (figurines)
afm2tfm chess-goodcompanions2-board-fig-raw.afm \
  -T chess-goodcompanions2-fig.enc \
  chess-goodcompanions2-lsf
```

### 3. Create font definition files

Create `lsb1goodcompanions2.fd`, `lsb2goodcompanions2.fd`, `lsb3goodcompanions2.fd`:

```latex
\DeclareFontFamily{LSB1}{goodcompanions2}{}
\DeclareFontShape{LSB1}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
```

(Change `LSB1` to `LSB2` / `LSB3` for the other two files.)

Create `lsfgoodcompanions2.fd`:

```latex
\DeclareFontFamily{LSF}{goodcompanions2}{}
\DeclareFontShape{LSF}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsf}{}
```

### 4. Install to your local texmf tree

```bash
TEXMF=~/Library/texmf   # macOS; Linux: ~/texmf

cp chess-goodcompanions2-board-fig-raw.pfb  $TEXMF/fonts/type1/chess/enpassant/
cp chess-goodcompanions2-board-fig-raw.afm  $TEXMF/fonts/afm/chess/enpassant/
cp chess-goodcompanions2-lsb.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp chess-goodcompanions2-lsf.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp chess-goodcompanions2.ttf                $TEXMF/fonts/truetype/chess/enpassant/
cp lsb1goodcompanions2.fd  lsb2goodcompanions2.fd  lsb3goodcompanions2.fd  lsfgoodcompanions2.fd \
                            $TEXMF/tex/latex/chessfss/enpassant/
```

### 5. Register the map entries

Create `chess-goodcompanions2.map`:

```
chess-goodcompanions2-board-fig-raw GC2004D2 <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsb GC2004D2 " ChessBoardEncoding ReEncodeFont " <chess-board.enc <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsf GC2004D2 " ChessGC2FigEncoding ReEncodeFont " <chess-goodcompanions2-fig.enc <chess-goodcompanions2-board-fig-raw.pfb
```

Then register it:

```bash
cp chess-goodcompanions2.map $(kpsewhich --var-value TEXMFLOCAL)/fonts/map/dvips/chess/
updmap-user --enable Map chess-goodcompanions2.map
```

### 6. Refresh the TeX database

```bash
mktexlsr
```

---

## Usage in LaTeX

```latex
\usepackage[LSB1,LSB2,LSB3,LSF,T1]{fontenc}
\usepackage{xcolor}
\usepackage{chessboard}
\usepackage{chessfss}

\setfigfontfamily{goodcompanions2}
\setchessboard{
  boardfontfamily=goodcompanions2,
  boardfontencoding=LSB1,
  boardfontsize=20pt,
  showmover=false
}

% Hatched dark squares (LSB1)
\chessboard[setfen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR]

% Solid gray dark squares with colored pieces (LSB2)
\setchessboard{boardfontencoding=LSB2}
\chessboard[setfen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR,
  color=black!60,colorblackbackfields,
  clearfontcolors,colorwhite=blue,colorblack=red,setfontcolors]
```

See `sample.tex` for a complete working example.

---

## License

The original **GoodCompanions** font is freeware by Armando H. Marroquin (2004), freely redistributable for non-commercial use.

This adaptation is released under the [MIT License](LICENSE.md) by Joel Cato (2026).


