import cv2
import glob
from PIL import Image
import numpy as np
import moviepy.editor as mpe
from moviepy.video.VideoClip import TextClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from helper import *
import os

# создаем картинки из которых будем делать видео
make_res_images()
make_ticker()
# делаем видео
make_video()
# удаляем промежуточные видео
os.remove('video.avi')
# удаляем картинки, из которых делали видео
result_files = os.listdir(result_directory)
for i in result_files:
    os.remove('{0}/{1}'.format(result_directory, i))
