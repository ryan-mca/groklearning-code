from PIL import Image

fname = input("File name: ")
img = Image.open(fname)

print(f"{img.width * img.height} pixels!")