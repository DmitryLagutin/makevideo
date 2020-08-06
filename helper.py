import cv2
from PIL import Image

import cv2
import glob
from PIL import Image
import numpy as np
import moviepy.editor as mpe
from moviepy.video.VideoClip import TextClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import threading
from helper import *
import os

basic_directory = 'img'
result_directory = 'res'


def get_file(fon_path, watermark_path, res_path):
    fon = cv2.imread(fon_path)
    height, width, channels = fon.shape
    print(height, width, channels)

    im = Image.open(watermark_path)
    h, w = im.size
    scale = width / h  # width / max(w, h)
    im.resize((int(h * scale), int(w * scale)), Image.ANTIALIAS).save(watermark_path)
    im = Image.open(watermark_path)
    h, w = im.size

    fon1 = Image.open(fon_path)
    im = Image.open(watermark_path)
    fon1.paste(im, (0, int(height / 2 - h / 2)))  # fon1.paste(im, (0, int(width / 2.5))) int(width / 2.7)
    fon1.save(res_path)
    fon1.close()
    im.close()


def make_res_images():
    basic_files = os.listdir(basic_directory)
    for i in basic_files:
        get_file('fon/fon.jpg', '{0}/{1}'.format(basic_directory, i), '{0}/{1}'.format(result_directory, i))


def make_video():
    result_files = os.listdir(result_directory)
    print(len(result_files), '---------')

    height, width, channels = cv2.imread('{0}/{1}'.format(result_directory, result_files[0])).shape

    out = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                          float(1 / (15 / int(len(result_files)))),
                          (width, height))  # создаем видео

    for i in result_files:
        out.write(cv2.imread('{0}/{1}'.format(result_directory, i)))

    out.release()  # генерируем
    cv2.destroyAllWindows()  # завершаем
    # склеиваем музыку и видео
    my_clip = mpe.VideoFileClip('video.avi')
    my_clip.write_videofile('res_video/result_video.mp4', audio='music/sunny.mp3')
    my_clip.close()
    clip = VideoFileClip("res_video/result_video.mp4").subclip(0, 15)
    clip.write_videofile("res_video/result_video.mp4")
    clip.close()
