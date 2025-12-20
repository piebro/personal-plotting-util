# Personal Plotting Documentation

These are a collection of commands I use to plot in my [AxiDraw V3](https://shop.evilmadscientist.com/846).

## Setup

Install [uv](https://docs.astral.sh/uv/) to install [vpype](https://github.com/abey79/vpype) for preparing SVG for plotting and [AxiCLI](https://axidraw.com/doc/cli_api/) for plotting:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh # for Linux and Mac
uv venv
uv pip install vpype
uv pip install https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_API.zip
```

## Preparing SVGs for plotting

```bash
uv run vpype read input.svg \
  linemerge --tolerance 1mm \
  linesort \
  scaleto 10cm 10cm \
  write \
  --page-size 10x10cm \
  --center \
  plot.svg

# other arg: linesimplify --tolerance 0.5mm

# DIN A3
# --page-size 42.0x29.7cm \
# DIN A4
# --page-size 29.7x21.0cm \
# DIN A5
# --page-size 21.0x14.8cm \
# my Postcard format
# --page-size 15.3x10.8cm \
```

## Plotting these SVGs

```bash
# create preview
uv run axicli plot.svg --model 2 -vg3 --speed_pendown 15 --report_time -o preview.svg

# show preview
eog preview.svg

# turn pen up/down
uv run axicli -m toggle

# plot
uv run axicli plot.svg --model 2 --speed_pendown 15 && uv run axicli -m align
# speed_pendown default 25

# turn motors off
uv run axicli -m align
```

## General Links

- [awesome-plotters](https://github.com/beardicus/awesome-plotters) - List of Plotter resources
- [Pens](https://www.pilotpen.de/themenwelten/alles-fuers-buero/3917/mine-g2-7-0.7-m?c=28) - Pens I use for plotting.

## Generating SVGs

- [Image to Lineart](image_to_lineart.md) - Convert AI-generated lineart images to SVGs for plotting.
- [Creating Maps](https://github.com/piebro/plotting-maps) - A tool to easily create OpenStreetMap SVG maps to plot them with a pen plotter. 
- [TurtleToy](https://turtletoy.net/) - Create generative art using a minimalistic JavaScript Turtle graphics API.
- [Architecture](https://github.com/piebro/plotting-architecture) - Generative art resembling Architecture blueprints.
- [Protein Ribbons](https://github.com/piebro/plotting-ribbons) - A tool to render protein ribbon diagrams as SVGs.
- [Algorithmic Tree](https://zv.github.io/static/algorithmic-tree.html) - Generate trees for plotting.
- [Shan, Shui](https://github.com/LingDong-/shan-shui-inf) - Procedurally-generated infinitely-scrolling Chinese landscape.
- [Linedraw](https://github.com/LingDong-/linedraw) - Convert images to vectorized line drawings for plotters. 
- [plotter.vision](https://plotter.vision/) - Convert 3D STL file to SVG.

### Fishdraw

Project link: https://github.com/LingDong-/fishdraw

```bash
# crop the rect around the fish away

uv run vpype read input.svg \
  linemerge --tolerance 0.2mm \
  linesort \
  crop 11 11 498 298 \
  write \
  --page-size 15.3x10.8cm \
  --center \
  plot.svg
```

### Turtletoy

#### Packed Custom Text

Link: https://turtletoy.net/turtle/cd5d29d769

#### Hexagon Truchet

Link: https://turtletoy.net/turtle/e5df5b10e0
This works great with a thicker pen and maybe change the scale.

#### Forest of trees

Link: https://turtletoy.net/turtle/ce083b5113#style=2,seed=69.8,leaf_detail=6,tree_count=1,line_thickness=2
```bash
uv run vpype read llemarie-forest-of-trees-ce083b5113.svg scaleto 101mm 140mm linemerge -t 0.05mm linesort write --page-size 111mmx150mm --center plot.svg
```

#### Strange attractors III

Link: https://turtletoy.net/turtle/a521066015#trajectory=16,plottable=1
```bash
vpype read llemarie-strange-attractors-iii-a521066015.svg scaleto 101mm 140mm linemerge -t 2mm linesimplify -t 0.2mm linesort write --page-size 111mmx150mm --center plot.svg
```

