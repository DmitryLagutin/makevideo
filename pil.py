from PIL import Image

im = Image.open("img/1.jpg")
h, w = im.size
scale = 1080 / max(h, w)
im.resize((int(h * scale), int(w * scale)), Image.ANTIALIAS).save("img/1.jpg")