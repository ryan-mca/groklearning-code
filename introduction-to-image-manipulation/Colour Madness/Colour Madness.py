from PIL import Image

img = Image.open(input("File name: "))

r, g, b = img.split()

new_img = Image.merge("RGB", (g, r, b))
new_img.save("output.png")