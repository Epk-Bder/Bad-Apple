import json
import os
import time
from toFrames import v2f

# // Uncomment this to rerender frames,
v2f.toFrames("badapple.mp4", 6, 16, 10, 5)

f = open("frames.json")
vidInfo = json.load(f)
print(vidInfo)

for frame in vidInfo:
    os.system("cls")
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
    print(content)
    time.sleep(1/6)