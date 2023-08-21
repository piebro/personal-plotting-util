# personal-plotting-util

## SVG Util

[vpype](<https://github.com/abey79/vpype>) is a helpful tool.

Example bash command:

```bash
vpype --help
vpype write --help

vpype read input.svg \
  linemerge --tolerance 1mm \
  linesort \
  scaleto 25cm 25cm \
  write \
  --page-size 14.7x10.2cm \
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

vpype read input.svg splitdist 50cm write output.svg

```

## Plot Cmds

```bash
# if the plotter cant connect: sudo chmod 666 /dev/ttyACM1

# create preview
axicli plot.svg --model 2 -vg3 --speed_pendown 15 --report_time -o preview.svg

# show preview
eog preview.svg

# turn pen up/down
axicli -m toggle

# plot
axicli plot.svg --model 2 --speed_pendown 15 && axicli -m align
# speed_pendown default 25

# turn motors off
axicli -m align
```

## Projects

### Links

[Pens](https://www.pilotpen.de/themenwelten/alles-fuers-buero/3917/mine-g2-7-0.7-m?c=28)

[Pens](https://shop.molotow.com/de/marker-refills.html)

[Architecture](https://github.com/piebro/plotting-architecture)

[Map](https://github.com/piebro/plotting-map)

[Protein Ribbons](https://github.com/piebro/plotting-ribbons)

[Packed Custom Text](https://turtletoy.net/turtle/cd5d29d769)

[TurtleToy](https://turtletoy.net/)

[algorithmic tree](https://zv.github.io/static/algorithmic-tree.html)

[Shan, Shui](https://github.com/LingDong-/shan-shui-inf)

### fishdraw

Go [here](https://fishdraw.glitch.me/) and copy the svg from the side with the developer console and save it in a file.

```bash
# crop the rect around the fish away

vpype read input.svg \
  linemerge --tolerance 0.2mm \
  linesort \
  crop 11 11 498 298 \
  write \
  --page-size 15.3x10.8cm \
  --center \
  plot.svg
```

### Turtletoy Hexagon Truchet

Go [here](https://turtletoy.net/turtle/e5df5b10e0). This is great with a thicker pen and maybe change the scale.