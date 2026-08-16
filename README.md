# Image Multisize Resizer

A robust, production-ready Python Command Line Interface (CLI) tool that allows you to resize a single image into multiple widths in one go. It uses Python's built-in `argparse` library for the CLI and the `Pillow` library for high-quality image processing.

The tool automatically calculates proportional heights based on your target widths, ensuring the original aspect ratio is perfectly maintained using high-quality LANCZOS resampling.

## Features

- **Multiple Sizes at Once**: Provide a comma-separated list of widths to generate multiple images simultaneously.
- **Aspect Ratio Preservation**: Automatically scales the height proportionally to the provided width.
- **High-Quality Resampling**: Uses `Image.Resampling.LANCZOS` for the best possible resized image quality.
- **Custom Output Directory**: Save the generated images in the same directory as the original, or specify a custom output path.
- **Descriptive Naming**: Automatically appends the generated width to the filename (e.g., `photo_800px.jpg`).

## Installation

Install the package using pip:

```bash
pip install .
```

This will install the required dependencies (like `Pillow`) and make the `multi-resizer` command available globally in your environment.

## Usage

Once installed, you can use the `multi-resizer` command. It accepts the following arguments:

- `-i`, `--image` (Required): Path to the input image file.
- `-s`, `--sizes` (Required): Comma-separated list of target widths (e.g., `300,600,1200`).
- `-o`, `--output` (Optional): Directory to save resized images. Defaults to the input image directory.

### CLI Usage Examples

**1. Basic Usage**
Saves copies directly next to your original file.

```bash
multi-resizer -i photo.jpg -s 400,800,1200
```
*Output files generated:* `photo_400px.jpg`, `photo_800px.jpg`, and `photo_1200px.jpg`.

**2. Custom Output Directory**
Saves copies into a dedicated folder (the tool will create the directory if it doesn't exist).

```bash
multi-resizer --image elements.png --sizes 150,300 --output ./thumbnails
```
*Output files generated:* `./thumbnails/elements_150px.png` and `./thumbnails/elements_300px.png`.

## Error Handling

- Gracefully handles missing input files.
- Creates the target output directory if it does not already exist.
- Validates the target sizes argument to ensure it contains a valid list of integers.

## Requirements

- Python 3.x
- Pillow
