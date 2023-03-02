import json
import os
import time
from toFrames import v2f

fps = 6
width = 16
height = 10
length = -1
# // Uncomment this to rerender frames,
v2f.toFrames("badapple.mp4", fps, width, height, length)

f = open("frames.json")
vidInfo = json.load(f)
print(vidInfo)

finish = []
for frame in vidInfo:
    content = ""
    for v in frame:
        for h in v:
            if h == 2:
                color = "#"
            elif h == 1:
                color = "*"
            else:
                color = " "
            content = (f"{content}{color}")
        content = (f"{content}\n")
    finish.append(content)

for i in finish:
    print(i)
    time.sleep(1/6)
    os.system("cls")

print("Done!")