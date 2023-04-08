from PIL import Image

img = Image.open(input("File name: "))

for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        img.putpixel((x, y), 255 - pixel)

img.save("output.png")