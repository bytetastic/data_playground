# PNG to ICO Converter with Python 🖼️➡️📂

This project demonstrates how to use Pillow (Python Imaging Library) to convert a PNG file into an ICO file.  
It’s especially useful if you want to create your own **folder icons** or **app icons**.

---

## 📦 Requirements

- Python 3.x
- Pillow library

Install Pillow:
```bash
pip install pillow
```

---

## 🚀 Usage

Example script:

```python
from PIL import Image

# Load PNG file
png_image = Image.open("assets/office.png")

# Save as ICO (256x256)
png_image.save("office.ico", format="ICO", size=(256, 256))
```

---

## 📂 Output

- Input: `assets/office.png`  
- Output: `office.ico` in the current working directory  

The ICO file can then be used in Windows as a **folder icon** or **application icon**.

---

## ✨ Tips

- Make sure your PNG is **square** (e.g., 256×256 pixels), otherwise the icon may look stretched.  
- You can include multiple sizes in one ICO file:
  ```python
  png_image.save("office.ico", format="ICO", sizes=[(16,16), (32,32), (48,48), (256,256)])
  ```
- Transparent backgrounds in PNGs are preserved in ICO format.  

---

## 📌 License

This example code is free to use and intended as a learning project.
```