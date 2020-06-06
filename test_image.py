from PIL import Image, ImageDraw, ImageFont

name = 'Juan Cruz'
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 32)
temp = Image.new('RGB', (600,600), color='white')
d = ImageDraw.Draw(temp)
textsize = d.textsize(name, fnt)

if textsize[0] < 600:
    img = Image.new('RGB', (600, 600), color='white')
    d = ImageDraw.Draw(img)
else:
    img = Image.new('RGB', (textsize[0] + 60, 600), color='white')
    d = ImageDraw.Draw(img)

width = (img.width / 2) - (textsize[0]/2)
height = (img.height / 2) - (textsize[1]/2)
d.text((width, height), name, fill=(0,0,0), font=fnt)

file_name = name + '.png'

img.save(file_name)