from moviepy import *
from moviepy.editor import *
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import os

from moviepy.video.io.VideoFileClip import VideoFileClip

basic_directory = 'img'
basic_files = os.listdir(basic_directory)
clip = ImageSequenceClip(['{0}/{1}'.format(basic_directory, basic_files[0]),
                          '{0}/{1}'.format(basic_directory, basic_files[1]),
                          '{0}/{1}'.format(basic_directory, basic_files[2]),
                          '{0}/{1}'.format(basic_directory, basic_files[3]),
                          ], fps=0.5)
clip.write_videofile("myHolidays_edited.mp4",  audio='music/sunny.mp3')
clip = VideoFileClip("myHolidays_edited.mp4").subclip(0, 15)
clip.write_videofile("myHolidays_edited.mp4", codec = 'mpeg4')
