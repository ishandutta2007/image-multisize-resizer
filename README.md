<p align="center">
  <img src="./assets/banner.svg" alt="Image Multisize Resizer Banner">
</p>

# 🖼️ Image Multisize Resizer: Batch Image Resizing CLI Tool for Python

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://badge.fury.io/py/image-multisize-resizer"><img src="https://badge.fury.io/py/image-multisize-resizer.svg" alt="PyPI version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://pypi.org/project/image-multisize-resizer/"><img src="https://img.shields.io/pypi/pyversions/image-multisize-resizer.svg" alt="Python Versions"></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

A robust, production-ready **Python Command Line Interface (CLI) tool** 🛠️ for fast and efficient **batch image resizing**. It allows you to automatically resize a single image into multiple widths in one go, saving time and effort 🚀. Built with Python's `argparse` and the powerful `Pillow` library for high-quality **image processing**.

The tool automatically calculates proportional heights based on your target widths, ensuring the original **aspect ratio** is perfectly maintained using high-quality **LANCZOS resampling** ✨. Ideal for web developers 👨‍💻, designers 🎨, and anyone needing quick, multi-resolution image generation for responsive web design or app thumbnails 📱.

## 👥 For Users

### ✨ Features
- ⚡ **Batch Resizing / Multiple Sizes at Once**: Provide a comma-separated list of widths to generate multiple images simultaneously.
- 📐 **Aspect Ratio Preservation**: Automatically scales the height proportionally to the provided width to prevent distortion.
- 💎 **High-Quality Resampling**: Uses `Image.Resampling.LANCZOS` for the best possible resized image quality and sharpness.
- 📂 **Custom Output Directory**: Save the generated images in the same directory as the original, or specify a custom output path for better organization.
- 🏷️ **Descriptive Auto-Naming**: Automatically appends the generated width to the filename (e.g., `photo_800px.jpg`).

### ⚙️ Installation
You can install the package directly via pip:

```bash
pip install image-multisize-resizer
```

*(Note: If installing from source, clone the repository and run `pip install .`)*

### 🚀 Usage
Once installed, the `multi-resizer` command is available globally on your system.

**Arguments:**
- `-i`, `--image` (Required): Path to the input image file you want to resize.
- `-s`, `--sizes` (Required): Comma-separated list of target widths in pixels (e.g., `300,600,1200`).
- `-o`, `--output` (Optional): Directory to save the resized output images. Defaults to the input image directory.

**Examples:**

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

### 🛡️ Error Handling
- 🛑 Gracefully handles missing input files.
- 📁 Creates the target output directory if it does not already exist.
- ✅ Validates the target sizes argument to ensure it contains a valid list of integers.

---

## 💻 For Developers

### 🛠️ Local Setup
To set up the project locally for development:

1. Clone the repository:
   ```bash
   git clone https://github.com/ishandutta2007/image-multisize-resizer.git
   cd image-multisize-resizer
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows use: venv\Scripts\activate
   # On Linux/macOS use: source venv/bin/activate
   ```
3. Install the package in editable mode along with dependencies:
   ```bash
   pip install -e .
   ```

### 📋 Requirements
- Python 3.7+ 🐍
- Pillow >= 9.5.0 🖼️

### 🤝 Contributing
Please refer to the `CONTRIBUTING.md` file for more details on how to contribute to this project. We welcome bug reports 🐛, feature requests 💡, and pull requests 🔄.

---

## 📦 For Package Publishers

The publishing process for this package to PyPI is fully automated using GitHub Actions and PyPI Trusted Publishing (OIDC) 🔒.

### 🤖 How Automated Publishing Works
Whenever a new git tag starting with `v` (e.g., `v0.1.1`) is pushed to the repository, the GitHub Actions workflow (`.github/workflows/publish.yml`) is triggered.

The workflow will:
1. Checkout the repository.
2. Set up Python.
3. Build the source distribution (`sdist`) and wheel (`bdist_wheel`) using the `build` module.
4. Publish the package securely to PyPI using the `pypa/gh-action-pypi-publish` action via an OIDC token. The `skip-existing: true` flag ensures that if the version already exists, the step will simply skip publishing without failing.

### 🚀 How to Release a New Version
To publish a new version of the package to PyPI, follow these steps:
1. Open `pyproject.toml`.
2. Update the `version = "X.Y.Z"` field to the new desired version.
3. Commit your changes.
4. Create a new git tag matching the version (with a `v` prefix) and push it to origin:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```
5. The GitHub Action will trigger on the pushed tag and automatically build and publish the new version to PyPI.

### 🔑 Initial Setup (For Project Owner)
If this is your first time setting up the repository for PyPI publishing via OIDC:
1. Go to your project on PyPI (or create the project if it doesn't exist).
2. Navigate to **Manage > Publishing**.
3. Add a new **GitHub publisher**.
4. Provide the GitHub repository owner (`ishandutta2007`), repository name (`image-multisize-resizer`), and workflow filename (`publish.yml`).
5. This grants the GitHub Action permission to publish to PyPI securely without needing to store API tokens as secrets.

---

## 🌟 Star History
[![Star History Chart](https://star-history.dera.page/svg?repos=ishandutta2007/image-multisize-resizer&type=date&legend=top-left)](https://star-history.dera.page/#ishandutta2007/image-multisize-resizer&type=date&legend=top-left)
