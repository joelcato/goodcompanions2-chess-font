# GoodCompanions2 — Chess font for LaTeX's `chessboard` package

Joel Cato's [`chessboard`](https://ctan.org/pkg/chessboard) / [`chessfss`](https://ctan.org/pkg/chessfss) adaptation of the [GoodCompanions](http://www.enpassant.dk/chess/fonteng.htm) chess font by David L. Brown (2004).

See **[sample.pdf](sample.pdf)** for a preview showing all encodings and color options.

---

## What's in this repo

| File | Purpose |
|---|---|
| `chess-goodcompanions2.ttf` | The font, with glyphs pre-renamed for `chess-board.enc` — start here |
| `sample.tex` | Gallery page demonstrating LSB1/LSB2/LSB3/LSF encodings |
| `sample.pdf` | Pre-built gallery PDF |

---

## macOS

### Prerequisites

**TeX Live packages:**

```bash
sudo tlmgr install chessboard chessfss
```

**enpassant** (not in tlmgr — install manually):

1. Download the zip from https://ctan.org/pkg/enpassant and extract it
2. Copy the `enpassant/` folder into your texmf tree:

```bash
TEXMF=~/Library/texmf

mkdir -p $TEXMF/fonts/chess
cp -r enpassant $TEXMF/fonts/chess/
mktexlsr
```

**FontForge:**

```bash
brew install fontforge
```

### Installation

#### 1. Convert TTF → PFB + AFM

```bash
fontforge -lang=ff -c '
  Open("chess-goodcompanions2.ttf");
  Reencode("custom");
  Generate("chess-goodcompanions2-board-fig-raw.pfb");
'
```

This produces `chess-goodcompanions2-board-fig-raw.pfb` and `chess-goodcompanions2-board-fig-raw.afm`.

#### 2. Generate TFM files

Requires enpassant to be installed in your texmf tree (see Prerequisites above).

```bash
TEXMF=~/Library/texmf

afm2tfm chess-goodcompanions2-board-fig-raw.afm -T $TEXMF/fonts/chess/enpassant/chess-board.enc chess-goodcompanions2-lsb.tfm
afm2tfm chess-goodcompanions2-board-fig-raw.afm -T $TEXMF/fonts/chess/enpassant/chess-fig.enc chess-goodcompanions2-lsf.tfm
```

#### 3. Create font definition files

```bash
cat > lsb1goodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSB1}{goodcompanions2}{}
\DeclareFontShape{LSB1}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
EOF

cat > lsb2goodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSB2}{goodcompanions2}{}
\DeclareFontShape{LSB2}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
EOF

cat > lsb3goodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSB3}{goodcompanions2}{}
\DeclareFontShape{LSB3}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
EOF

cat > lsfgoodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSF}{goodcompanions2}{}
\DeclareFontShape{LSF}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsf}{}
EOF
```

#### 4. Install to your local texmf tree

```bash
TEXMF=~/Library/texmf

mkdir -p $TEXMF/fonts/type1/chess/enpassant
mkdir -p $TEXMF/fonts/afm/chess/enpassant
mkdir -p $TEXMF/fonts/tfm/chess/enpassant
mkdir -p $TEXMF/fonts/truetype/chess/enpassant
mkdir -p $TEXMF/fonts/enc/dvips/chess
mkdir -p $TEXMF/tex/latex/chessfss/enpassant

cp chess-goodcompanions2-board-fig-raw.pfb  $TEXMF/fonts/type1/chess/enpassant/
cp chess-goodcompanions2-board-fig-raw.afm  $TEXMF/fonts/afm/chess/enpassant/
cp chess-goodcompanions2-lsb.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp chess-goodcompanions2-lsf.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp chess-goodcompanions2.ttf                $TEXMF/fonts/truetype/chess/enpassant/
cp $TEXMF/fonts/chess/enpassant/chess-board.enc  $TEXMF/fonts/enc/dvips/chess/
cp $TEXMF/fonts/chess/enpassant/chess-fig.enc    $TEXMF/fonts/enc/dvips/chess/
cp lsb1goodcompanions2.fd lsb2goodcompanions2.fd lsb3goodcompanions2.fd lsfgoodcompanions2.fd \
   $TEXMF/tex/latex/chessfss/enpassant/
```

#### 5. Register the map entries

```bash
cat > chess-goodcompanions2.map << 'EOF'
chess-goodcompanions2-board-fig-raw GC2004D2 <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsb GC2004D2 " ChessBoardEncoding ReEncodeFont " <chess-board.enc <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsf GC2004D2 " ChessFigEncoding ReEncodeFont " <chess-fig.enc <chess-goodcompanions2-board-fig-raw.pfb
EOF

mkdir -p $TEXMF/fonts/map/dvips/chess
cp chess-goodcompanions2.map $TEXMF/fonts/map/dvips/chess/
updmap-user --enable Map chess-goodcompanions2.map
```

#### 6. Refresh the TeX database

```bash
mktexlsr
```

---

## Linux

### Prerequisites

**TeX Live packages:**

```bash
sudo tlmgr install chessboard chessfss
```

**enpassant** (not in tlmgr — install manually):

1. Download the zip from https://ctan.org/pkg/enpassant and extract it
2. Copy the `enpassant/` folder into your texmf tree:

```bash
TEXMF=~/texmf

mkdir -p $TEXMF/fonts/chess
cp -r enpassant $TEXMF/fonts/chess/
mktexlsr
```

**FontForge:**

| Distro(s) | Command |
|---|---|
| Ubuntu, Debian, Mint, Pop!\_OS, Elementary | `sudo apt install fontforge` |
| Fedora, RHEL, CentOS | `sudo dnf install fontforge` |
| Arch, Manjaro | `sudo pacman -S fontforge` |
| openSUSE | `sudo zypper install fontforge` |

### Installation

#### 1. Convert TTF → PFB + AFM

```bash
fontforge -lang=ff -c '
  Open("chess-goodcompanions2.ttf");
  Reencode("custom");
  Generate("chess-goodcompanions2-board-fig-raw.pfb");
'
```

This produces `chess-goodcompanions2-board-fig-raw.pfb` and `chess-goodcompanions2-board-fig-raw.afm`.

#### 2. Generate TFM files

Requires enpassant to be installed in your texmf tree (see Prerequisites above).

```bash
TEXMF=~/texmf

afm2tfm chess-goodcompanions2-board-fig-raw.afm -T $TEXMF/fonts/chess/enpassant/chess-board.enc chess-goodcompanions2-lsb.tfm
afm2tfm chess-goodcompanions2-board-fig-raw.afm -T $TEXMF/fonts/chess/enpassant/chess-fig.enc chess-goodcompanions2-lsf.tfm
```

#### 3. Create font definition files

```bash
cat > lsb1goodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSB1}{goodcompanions2}{}
\DeclareFontShape{LSB1}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
EOF

cat > lsb2goodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSB2}{goodcompanions2}{}
\DeclareFontShape{LSB2}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
EOF

cat > lsb3goodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSB3}{goodcompanions2}{}
\DeclareFontShape{LSB3}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
EOF

cat > lsfgoodcompanions2.fd << 'EOF'
\DeclareFontFamily{LSF}{goodcompanions2}{}
\DeclareFontShape{LSF}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsf}{}
EOF
```

#### 4. Install to your local texmf tree

```bash
TEXMF=~/texmf

mkdir -p $TEXMF/fonts/type1/chess/enpassant
mkdir -p $TEXMF/fonts/afm/chess/enpassant
mkdir -p $TEXMF/fonts/tfm/chess/enpassant
mkdir -p $TEXMF/fonts/truetype/chess/enpassant
mkdir -p $TEXMF/fonts/enc/dvips/chess
mkdir -p $TEXMF/tex/latex/chessfss/enpassant

cp chess-goodcompanions2-board-fig-raw.pfb  $TEXMF/fonts/type1/chess/enpassant/
cp chess-goodcompanions2-board-fig-raw.afm  $TEXMF/fonts/afm/chess/enpassant/
cp chess-goodcompanions2-lsb.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp chess-goodcompanions2-lsf.tfm            $TEXMF/fonts/tfm/chess/enpassant/
cp chess-goodcompanions2.ttf                $TEXMF/fonts/truetype/chess/enpassant/
cp $TEXMF/fonts/chess/enpassant/chess-board.enc  $TEXMF/fonts/enc/dvips/chess/
cp $TEXMF/fonts/chess/enpassant/chess-fig.enc    $TEXMF/fonts/enc/dvips/chess/
cp lsb1goodcompanions2.fd lsb2goodcompanions2.fd lsb3goodcompanions2.fd lsfgoodcompanions2.fd \
   $TEXMF/tex/latex/chessfss/enpassant/
```

#### 5. Register the map entries

```bash
cat > chess-goodcompanions2.map << 'EOF'
chess-goodcompanions2-board-fig-raw GC2004D2 <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsb GC2004D2 " ChessBoardEncoding ReEncodeFont " <chess-board.enc <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsf GC2004D2 " ChessFigEncoding ReEncodeFont " <chess-fig.enc <chess-goodcompanions2-board-fig-raw.pfb
EOF

mkdir -p $TEXMF/fonts/map/dvips/chess
cp chess-goodcompanions2.map $TEXMF/fonts/map/dvips/chess/
updmap-user --enable Map chess-goodcompanions2.map
```

#### 6. Refresh the TeX database

```bash
mktexlsr
```

---

## Windows

Uses PowerShell and TeX Live. Run all commands from the directory containing the cloned repo.

### Prerequisites

**TeX Live packages** (run PowerShell as Administrator):

```powershell
tlmgr install chessboard chessfss
```

**enpassant** (not in tlmgr — install manually):

1. Download the zip from https://ctan.org/pkg/enpassant and extract it
2. Copy the `enpassant/` folder into your texmf tree:

```powershell
$TEXMF = "$env:USERPROFILE\texmf"

New-Item -ItemType Directory -Force $TEXMF\fonts\chess
Copy-Item -Recurse enpassant $TEXMF\fonts\chess\
mktexlsr
```

**FontForge:** Download and install from https://fontforge.org/en-US/downloads/windows/ — ensure `fontforge` is on your PATH.

### Installation

#### 1. Convert TTF → PFB + AFM

```powershell
@'
Open("chess-goodcompanions2.ttf")
Reencode("custom")
Generate("chess-goodcompanions2-board-fig-raw.pfb")
'@ | Set-Content convert.pe
fontforge -script convert.pe
Remove-Item convert.pe
```

This produces `chess-goodcompanions2-board-fig-raw.pfb` and `chess-goodcompanions2-board-fig-raw.afm`.

#### 2. Generate TFM files

Requires enpassant to be installed in your texmf tree (see Prerequisites above).

```powershell
$TEXMF = "$env:USERPROFILE\texmf"

afm2tfm chess-goodcompanions2-board-fig-raw.afm -T $TEXMF\fonts\chess\enpassant\chess-board.enc chess-goodcompanions2-lsb.tfm
afm2tfm chess-goodcompanions2-board-fig-raw.afm -T $TEXMF\fonts\chess\enpassant\chess-fig.enc chess-goodcompanions2-lsf.tfm
```

#### 3. Create font definition files

```powershell
@'
\DeclareFontFamily{LSB1}{goodcompanions2}{}
\DeclareFontShape{LSB1}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
'@ | Set-Content lsb1goodcompanions2.fd

@'
\DeclareFontFamily{LSB2}{goodcompanions2}{}
\DeclareFontShape{LSB2}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
'@ | Set-Content lsb2goodcompanions2.fd

@'
\DeclareFontFamily{LSB3}{goodcompanions2}{}
\DeclareFontShape{LSB3}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsb}{}
'@ | Set-Content lsb3goodcompanions2.fd

@'
\DeclareFontFamily{LSF}{goodcompanions2}{}
\DeclareFontShape{LSF}{goodcompanions2}{m}{n}{<-> chess-goodcompanions2-lsf}{}
'@ | Set-Content lsfgoodcompanions2.fd
```

#### 4. Install to your local texmf tree

```powershell
$TEXMF = "$env:USERPROFILE\texmf"

New-Item -ItemType Directory -Force $TEXMF\fonts\type1\chess\enpassant
New-Item -ItemType Directory -Force $TEXMF\fonts\afm\chess\enpassant
New-Item -ItemType Directory -Force $TEXMF\fonts\tfm\chess\enpassant
New-Item -ItemType Directory -Force $TEXMF\fonts\truetype\chess\enpassant
New-Item -ItemType Directory -Force $TEXMF\fonts\enc\dvips\chess
New-Item -ItemType Directory -Force $TEXMF\tex\latex\chessfss\enpassant

Copy-Item chess-goodcompanions2-board-fig-raw.pfb  $TEXMF\fonts\type1\chess\enpassant\
Copy-Item chess-goodcompanions2-board-fig-raw.afm  $TEXMF\fonts\afm\chess\enpassant\
Copy-Item chess-goodcompanions2-lsb.tfm            $TEXMF\fonts\tfm\chess\enpassant\
Copy-Item chess-goodcompanions2-lsf.tfm            $TEXMF\fonts\tfm\chess\enpassant\
Copy-Item chess-goodcompanions2.ttf                $TEXMF\fonts\truetype\chess\enpassant\
Copy-Item $TEXMF\fonts\chess\enpassant\chess-board.enc  $TEXMF\fonts\enc\dvips\chess\
Copy-Item $TEXMF\fonts\chess\enpassant\chess-fig.enc    $TEXMF\fonts\enc\dvips\chess\
Copy-Item lsb1goodcompanions2.fd, lsb2goodcompanions2.fd, lsb3goodcompanions2.fd, lsfgoodcompanions2.fd `
          $TEXMF\tex\latex\chessfss\enpassant\
```

#### 5. Register the map entries

```powershell
@'
chess-goodcompanions2-board-fig-raw GC2004D2 <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsb GC2004D2 " ChessBoardEncoding ReEncodeFont " <chess-board.enc <chess-goodcompanions2-board-fig-raw.pfb
chess-goodcompanions2-lsf GC2004D2 " ChessFigEncoding ReEncodeFont " <chess-fig.enc <chess-goodcompanions2-board-fig-raw.pfb
'@ | Set-Content chess-goodcompanions2.map

New-Item -ItemType Directory -Force $TEXMF\fonts\map\dvips\chess
Copy-Item chess-goodcompanions2.map $TEXMF\fonts\map\dvips\chess\
updmap-user --enable Map chess-goodcompanions2.map
```

#### 6. Refresh the TeX database

```powershell
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

The original **GoodCompanions** font is freeware by David L. Brown (2004), freely redistributable for non-commercial use.

This adaptation is released under the [MIT License](LICENSE.md) by Joel Cato (2026).


