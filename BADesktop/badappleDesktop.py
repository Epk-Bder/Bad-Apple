import os
import time
import shutil

src0 = r"black.bmp"
black = r"white.bmp"

imgs = [r"black.bmp", "white.bmp"]

WIDTH = 16
HEIGHT = 10


pixels = []



desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')

for i in range(0, (WIDTH * HEIGHT)):
    file_path = os.path.join(desktop_dir, f"{str(i)}.png")
    shutil.copyfile(imgs[1], file_path)
    pixels.append(file_path)

time.sleep(15)

for i in pixels:
    os.remove(i)