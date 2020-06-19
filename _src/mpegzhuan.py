import os

m4a_path = os.path.join(os.path.dirname(os.getcwd()), 'files', 'm4a')
m4a_files = os.listdir(m4a_path)
ffmpeg_path = 'D:\ffmpeg-20200617-0b3bd00-win64-static\bin'

for i, m4a in enumerate(m4a_files):
    os.system(r"D:\ffmpeg-20200617-0b3bd00-win64-static\bin\ffmpeg -i " + m4a_path + '\\' + m4a + " " + m4a_path + str(i) + ".mp3")
print('success.')
