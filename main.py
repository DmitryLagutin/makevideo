import cv2
import glob
from PIL import Image
import numpy as np
import moviepy.editor as mpe
from moviepy.video.VideoClip import TextClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from helper import *
import os

make_res_images()
make_video()
os.remove('video.avi')
result_files = os.listdir(result_directory)
for i in result_files:
    os.remove('{0}/{1}'.format(result_directory, i))
