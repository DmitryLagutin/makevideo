from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (270, 70), 'red')
idraw = ImageDraw.Draw(img)
headline = ImageFont.truetype('9041.ttf', size=25)
text = 'https://ali.ski/Zyqnb'



idraw.text((10, 20), text, 'black', font=headline)
w, h = idraw.textsize(text, font=headline)
print(w, h)

img.save('canvas.png')

# im = Image.new("RGBA", (400, 200), 'gray')
# transparent_area = (0,0,400, 200)
# mask=Image.new('L', im.size, color=255)
# draw=ImageDraw.Draw(mask)
# draw.rectangle(transparent_area, fill=0)
# im.putalpha(mask)
# headline = ImageFont.truetype('19485.otf', size=30)
# text = 'Hello World'
# #
# draw.text((40, 20), text, font=headline)
#
# im.save('output.png')
#
# img = Image.open("output.png")
#
# idraw = ImageDraw.Draw(img)
# headline = ImageFont.truetype('19485.otf', size=30)
# text = 'Hello World'
#
# idraw.text((40, 20), text, font=headline)
#
# img.save('canvas.png')
