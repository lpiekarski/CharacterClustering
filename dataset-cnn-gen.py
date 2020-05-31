import os
import random
from PIL import Image, ImageDraw, ImageFont

dataset_dir = 'dataset-cnn'
N = 400000
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.']
fonts = ["cambria"]
if not os.path.exists(dataset_dir):
    os.mkdir(dataset_dir)

for i in range(N):
    if i % 100 == 99:
        print(str(i) + '/' + str(N))
    text = random.choice(letters)
    img = Image.new('RGB', (10, 10))
    font_name = random.choice(fonts)
    font = ImageFont.truetype(font_name, int(12 + random.random() * 6 - 3))
    text_w, text_h = ImageDraw.Draw(img).textsize(text, font=font)
    img = Image.new('RGB', (text_w, text_h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((0, 0), text, fill=(0, 0, 0), font=font)
    img.save(dataset_dir + '/' + str(i) + ".png", "PNG")
    with open(dataset_dir + '/' + str(i) + '.txt', 'w') as output_file:
        output_file.write(text)
