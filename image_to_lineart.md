# Image to Lineart

There are many easy ways todays to use text to image models to generate PNGs with lineart with just a prompt or an image and a prompt.
Here is a collection a scripts and cmds to generate these images and then turn them to SVGs.

## Generating Images

The easiest way is to just go to Gemini, ChatGPT, bfl.ai or fal.ai and ask a model to generate a line art image and download it.

To create images locally I use fal.ai with a small script that can be run like this

```bash
export FAL_KEY=""
uv run https://raw.githubusercontent.com/piebro/personal-plotting-util/refs/heads/main/text_to_image.py "your prompt here" --aspect-ratio 16:9 --resolution 1k -o images/test
uv run https://raw.githubusercontent.com/piebro/personal-plotting-util/refs/heads/main/text_to_image.py "your prompt here" --aspect-ratio 16:9 --resolution 1k --image path/to/image.png -o images/test
```

Some example prompt elements are:

- black and white lineart
- thin consistent linework
- thin stroke
- uniform line weight
- pen plotter style
- 100% white background
- Single continuous line drawing of handwritten ...
- Botanical illustration ...

## Converting Images to SVGs

There are online tools that can help with this, e.g. [vtracer](https://www.visioncortex.org/vtracer/), but I used ImageMagick and Potrace and run it locally.

```bash
# Install ImageMagick and Potrace
sudo apt install imagemagick potrace

# Convert to PBM and trace to SVG with a variable threshold
INPUT="input.png" && convert "$INPUT" -threshold 50% "${INPUT}.pbm" && potrace "${INPUT}.pbm" -s -o "${INPUT}.svg"
```