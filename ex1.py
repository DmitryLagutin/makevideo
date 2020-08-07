from moviepy.editor import *

basic_directory = 'res'
basic_files = os.listdir(basic_directory)

img = ['{0}/{1}'.format(basic_directory, basic_files[0]),
       '{0}/{1}'.format(basic_directory, basic_files[1]),
       '{0}/{1}'.format(basic_directory, basic_files[2]),
       '{0}/{1}'.format(basic_directory, basic_files[3])]

clips = [ImageClip(m).set_duration(2)
         for m in img]

print(clips)

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=24)