import cv2
import glob
from PIL import Image
import numpy as np


def get_file(fon_path, watermark_path, res_path):
    fon = cv2.imread(fon_path)
    height, width, channels = fon.shape
    print(height, width, channels)

    im = Image.open(watermark_path)
    h, w = im.size
    scale = width / max(h, w)
    im.resize((int(h * scale), int(w * scale)), Image.ANTIALIAS).save(watermark_path)
    im = Image.open(watermark_path)
    h, w = im.size
    print(h, w)

    fon1 = Image.open(fon_path)
    im = Image.open(watermark_path)
    fon1.paste(im, (0, int(width / 2.5)))
    fon1.save(res_path)


list_x = ['img/1.jpg', 'img/2.jpg', 'img/3.jpg', 'img/4.jpg']
x = 1
for i in list_x:
    get_file('fon.jpg', i, 'res/{0}.jpg'.format(x))
    x = x + 1

img = cv2.imread('res/1.jpg')
height, width, channels = img.shape
print(height, width, channels)

# # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# # out = cv2.VideoWriter('video.mp4v', fourcc, 120.0, (width, height))
#
#
out = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 1.0, (width, height))  # создаем видео
out.write(cv2.imread('res/1.jpg'))  # добавляем картинки
out.write(cv2.imread('res/1.jpg'))
out.write(cv2.imread('res/1.jpg'))
out.write(cv2.imread('res/1.jpg'))
out.release()  # генерируем
cv2.destroyAllWindows()  # завершаем
