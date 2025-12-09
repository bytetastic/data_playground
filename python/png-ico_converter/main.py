from PIL import Image

png_image = Image.open("assets/office.png")

png_image.save("office.ico", format="ICO", size=(256, 256))