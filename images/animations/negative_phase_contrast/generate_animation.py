import os
from subprocess import check_call


print("Converting to mp4...", end='')
convert_command = [
    'ffmpeg', '-y',
    '-r', '10',
    '-f', 'image2',
    '-i', 'img%d.png',
    '-movflags', 'faststart',
    # See here: https://trac.ffmpeg.org/wiki/Encode/H.264#Encodingfordumbplayers
    '-pix_fmt', 'yuv420p',
    '-vcodec', 'libx264',
    '-vf', 'crop=2*trunc(iw/2):2*trunc(0.54*ih/2):0:ih*(1-0.54)/2',
    '-preset', 'veryslow',
    '-crf', '25',
    'animation.mp4']
try:
    with open('conversion_messages.txt', 'wt') as f:
        f.write("So far, everthing's fine...\n")
        f.flush()
        check_call(convert_command, stderr=f, stdout=f)
        f.flush()
    os.remove('conversion_messages.txt')
except: # This is unlikely to be platform independent :D
    print("MP4 conversion failed. Is ffmpeg installed?")
    raise
print('done.')

