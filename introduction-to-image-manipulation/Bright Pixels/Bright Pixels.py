from PIL import Image

img = Image.open(input("File name: "))

bright = 0

for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        if int(pixel) >= 200:
            bright+=1

print(f"{bright} pixels are bright.")