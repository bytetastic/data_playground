# OCR and Text-to-Speech Project

This project demonstrates how to use **EasyOCR** for optical character recognition (OCR) and **pyttsx3** for offline text-to-speech (TTS) in Python. The goal is to extract text from images (e.g., PNG files) and have the recognized text read aloud.

## Features
- Extract text from images using EasyOCR (supports multiple languages).
- Convert recognized text into speech using pyttsx3.
- Works completely offline (no cloud services required).
- Simple and minimal code setup.

## Requirements
- Python 3.8+
- Conda or pip environment
- Packages: `easyocr`, `pyttsx3`

## Environment & Notebook Usage

This project was developed and tested inside a **Conda environment** using **Jupyter Notebook**.  
Running the code in a notebook makes it easy to experiment with OCR and text-to-speech step by step. 

## Installation
```bash
# Using conda-forge
conda install -c conda-forge easyocr pyttsx3

# Or using pip inside your conda environment
pip install easyocr pyttsx3
```

## Usage Example
```python
import easyocr
import pyttsx3

# Initialize OCR reader for english
reader = easyocr.Reader(['en'])

# Read text from image
results = reader.readtext('example.png')

# Extract text parts
text = " ".join([res[1] for res in results])
print("Recognized Text:", text)

# TTS
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
```

## Notes
- The OCR results depend on image quality, font style, and layout.
- Complex layouts (e.g., textbooks with images, formulas, or multiple columns) may reduce accuracy.
- During testing with a short English sample text, **not all words were correctly recognized**. This shows that OCR can sometimes misinterpret characters or miss parts of the text.