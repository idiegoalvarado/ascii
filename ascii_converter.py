import numpy as np
from PIL import Image

# Contrast on a scale - int(contrast) -> int(contrast)
contrast = 10
density  = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|''()1{}[]?-_+~<>i!lI;:,"^`\'.            ')
density  = density[:-11+contrast]
n        = len(density)

img_path = "enter your path"
width    = 100

# Open the image and convert to greyscale
img = Image.open(img_path)
img = img.convert('L')

original_width, original_height = img.size
r = original_height / original_width

height = int(width * r * 0.5)
img = img.resize((width, height), Image.ANTIALIAS)

# Map the pixel brightness to the ASCII density glyphs.
image_array = np.array(img)

for i in range(height):
    for j in range(width):
        p = image_array[i,j]
        k = int(np.floor(p/256 * n))
        print(density[n-1-k], end='')
    print()