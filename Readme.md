# Python Developer Test 2: FFmpeg and Pillow

## Overview

This script makes a short video from an image using **FFmpeg** and **Pillow**. It adds text to the image, applies a simple change (**grayscale, rotate, or resize**), and turns it into a video with background music.

---

## Features

- Open an image with **Pillow**
- Add text to the image
- Change the image (**grayscale, rotate, or resize**)
- Make a short video using **FFmpeg**
- Set the video to be **at least 5 seconds long**
- Add background music (**MP3/FLAC**)
- Let the user choose **text, font size, image change, and music file**

---

## Installation

### 1. Install Python and Needed Libraries

Make sure **Python 3.x** is installed. Then, install **Pillow**:

```sh
pip install pillow
```

### 2. Install FFmpeg

You need FFmpeg installed and set up in your system's PATH.

Windows: Download it from https://ffmpeg.org/download.html and install.
Linux/macOS: Use this command:

```sh
sudo apt install ffmpeg  # Ubuntu/Debian
brew install ffmpeg      # macOS (Homebrew)

```

To check if FFmpeg is installed, run:

```sh
ffmpeg -version
```

---

## Usage

Run this command:

```sh
python test.py
```

- Then enter:
  - Image file name (e.g., input.jpg)
  - Music file name (e.g., sound.mp3)
  - Text to add (e.g., I am a cat)
  - Font size (e.g., 100)
  - Image change type (choose: grayscale, rotate, or resize)

---

## Included Files

This project comes with the following files:

- input.jpg (sample image for testing)
- sound.flac (sample background music)

These files are expected to be in the same folder as the script. If they are missing, place them in the same directory as test.py before running the script.

Example Interaction with the Script:

```sh
PS C:\New folder> python test.py
Enter image filename: input.jpg
Enter background music filename: sound.flac
Enter text to overlay: i am a cat
Enter font size: 400
Choose transformation (grayscale/rotate/resize): rotate
```
