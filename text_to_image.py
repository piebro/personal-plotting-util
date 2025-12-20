#!/usr/bin/env python3
# /// script
# dependencies = ["fal-client"]
# ///
"""Generate images using fal-ai models."""

import argparse
import urllib.request
from pathlib import Path

import fal_client

VALID_MODELS = ["nano-banana-pro", "flux-2-pro", "flux-2-max"]

VALID_ASPECT_RATIOS = [
    "21:9", "16:9", "3:2", "4:3", "5:4", "1:1",
    "9:21", "9:16", "2:3", "3:4", "4:5",
]

VALID_RESOLUTIONS = ["1K", "2K", "4K"]

# Map aspect ratios to Flux image_size format
ASPECT_TO_FLUX_SIZE = {
    "21:9": "landscape_21_9",
    "16:9": "landscape_16_9",
    "3:2": "landscape_3_2",
    "4:3": "landscape_4_3",
    "5:4": "landscape_5_4",
    "1:1": "square",
    "9:21": "portrait_9_21",
    "9:16": "portrait_9_16",
    "2:3": "portrait_2_3",
    "3:4": "portrait_3_4",
    "4:5": "portrait_4_5",
}


def get_output_path(base_name):
    """Get the next available output path with counter."""
    base = Path(base_name)
    if base.suffix.lower() == ".png":
        base = base.with_suffix("")

    counter = 0
    while True:
        path = Path(f"{base}_{counter:02d}.png")
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            return path
        counter += 1


def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(log["message"])


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using fal-ai models"
    )
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument(
        "--model", "-m",
        default="nano-banana-pro",
        choices=VALID_MODELS,
        help="Model to use (default: nano-banana-pro)"
    )
    parser.add_argument(
        "--aspect-ratio", "-a",
        default="1:1",
        choices=VALID_ASPECT_RATIOS,
        help="Aspect ratio (default: 1:1)"
    )
    parser.add_argument(
        "--resolution", "-r",
        default="1K",
        choices=VALID_RESOLUTIONS,
        type=str.upper,
        help="Resolution: 1K, 2K, or 4K (default: 1K, nano-banana-pro only)"
    )
    parser.add_argument(
        "--output", "-o",
        default="output",
        help="Output file base name (default: output)"
    )
    parser.add_argument(
        "--image", "-i",
        help="Input image path for image-to-image editing"
    )

    args = parser.parse_args()

    model_id = f"fal-ai/{args.model}"

    if args.image:
        uploaded_url = fal_client.upload_file(args.image)
        if args.model == "nano-banana-pro":
            result = fal_client.subscribe(
                f"{model_id}/edit",
                arguments={
                    "prompt": args.prompt,
                    "num_images": 1,
                    "aspect_ratio": "auto",
                    "output_format": "png",
                    "image_urls": [uploaded_url],
                    "resolution": args.resolution,
                },
                with_logs=True,
                on_queue_update=on_queue_update,
            )
        else:  # flux-2-pro, flux-2-max
            result = fal_client.subscribe(
                f"{model_id}/edit",
                arguments={
                    "prompt": args.prompt,
                    "image_urls": [uploaded_url],
                    "output_format": "png",
                },
                with_logs=True,
                on_queue_update=on_queue_update,
            )
    else:
        if args.model == "nano-banana-pro":
            result = fal_client.subscribe(
                model_id,
                arguments={
                    "prompt": args.prompt,
                    "num_images": 1,
                    "aspect_ratio": args.aspect_ratio,
                    "output_format": "png",
                    "resolution": args.resolution,
                },
                with_logs=True,
                on_queue_update=on_queue_update,
            )
        else:  # flux-2-pro, flux-2-max
            result = fal_client.subscribe(
                model_id,
                arguments={
                    "prompt": args.prompt,
                    "image_size": ASPECT_TO_FLUX_SIZE[args.aspect_ratio],
                    "output_format": "png",
                },
                with_logs=True,
                on_queue_update=on_queue_update,
            )

    image_url = result["images"][0]["url"]
    output_path = get_output_path(args.output)
    urllib.request.urlretrieve(image_url, output_path)
    print(f"Image saved to {output_path}")


if __name__ == "__main__":
    main()
