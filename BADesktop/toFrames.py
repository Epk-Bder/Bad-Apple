import os
import cv2
import json
from PIL import Image

class v2f:
    
    def toFrames(video, desfps, width, height, vlength:None):
        
        # Open the video file
        video = cv2.VideoCapture(video)

        fps = video.get(cv2.CAP_PROP_FPS)
        # Initialize a counter for the frames
        frame_count = 0

        if vlength != None:
            videolength = vlength * desfps * desfps
        else: videolength = -1

        print(video, desfps, width, height, videolength)

        frameskip = round(video.get(cv2.CAP_PROP_FPS) / desfps)
        # Loop through the frames
        directory = "bin"
        while True:

            ret, frame = video.read()

            if not ret:
                break
            
            
            if frame_count % frameskip == 0:
                filename = f"/frame{int(frame_count / frameskip)}.jpg"
                cv2.imwrite((directory+filename), frame)

            if frame_count == videolength:
                break


            frame_count += 1

        video.release()

        framelist = []
        for i in os.listdir(directory):
            image = Image.open(f"{directory}/{i}")
            image = image.resize((width, height), resample=Image.Resampling.NEAREST)
            image = image.convert("HSV")
            
            grid = []
            for y in range(image.height):
                grid.append([])
                for x in range(image.width):
                    hsv_pixel = image.getpixel((x, y))
                    colourgroup = 100 / 3 #100 is max brightness value, 3 is amount of colours
                    if hsv_pixel[2] > colourgroup * 2:
                        colour3 = 0
                    elif hsv_pixel[2] > colourgroup * 1:
                        colour3 = 1
                    else:
                        colour3 = 2
                    
                    grid[y].append([])
                    grid[y][x] = colour3

            framelist.append(grid)
        
        with open("frames.json", "w") as f:
            json.dump(framelist, f)

        for i in os.listdir(directory):
            file_path = os.path.join(directory, i)
            if os.path.isfile(file_path):
                os.remove(file_path)