import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

# создадим белое изображение
# или можно считать изобрежние с помощью cv2.imread("path_to_file")
img = np.zeros((256, 512, 3), np.uint8)
img[:, :, :] = 255


# для простоты и совместимости возьмем пустое изображение из первого примера
# Чтобы не использовать opencv, а только PIL используйте функцию Image.open()
def put_text_pil(img: np.array, txt: str):
    im = Image.fromarray(img)

    font_size = 24
    font = ImageFont.truetype('9041.ttf', size=font_size)

    draw = ImageDraw.Draw(im)
    # здесь узнаем размеры сгенерированного блока текста
    w, h = draw.textsize(txt, font=font)


    y_pos = 50
    im = Image.fromarray(img)
    draw = ImageDraw.Draw(im)

    # теперь можно центрировать текст
    draw.text((int((img.shape[1] - w) / 2), y_pos), txt, fill='rgb(0, 0, 0)', font=font)

    img = np.asarray(im)

    return img


img = put_text_pil(img, 'Some Styled Black Text Here')

cv2.imshow('Result', img)
cv2.waitKey()