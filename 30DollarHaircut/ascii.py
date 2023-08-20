import cv2
import numpy as np
import os
import time


WIDTH = 16
HEIGHT = 9
ASCII_CHARS = "#* "
FRAMERATE = 15 ## Actually Framerate /2

# Convert an RGB image to grayscale
def rgb_to_gray(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])


# Resize image to target dimensions
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


# Convert grayscale pixel value to ASCII character
def pixel_to_ascii(pixel_value):
    char_idx = int(pixel_value / 256 * len(ASCII_CHARS))
    return ASCII_CHARS[char_idx]


# Convert an image to ASCII art
def image_to_ascii(image):
    ascii_image = ""
    for row in image:
        ascii_row = "".join([pixel_to_ascii(pixel) for pixel in row])
        ascii_image += ascii_row
    return ascii_image


# Load video
cap = cv2.VideoCapture("bad_apple.mp4")

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    

    if count % FRAMERATE == 0:
        gray_frame = rgb_to_gray(frame)
        resized_frame = resize_image(gray_frame, WIDTH, HEIGHT)
        ascii_frame = image_to_ascii(resized_frame)

        Frame_to_ThirtyDollar = ''

        with open(f'files/Frame{(int(count/FRAMERATE))}.🗿', 'a') as f:

            for i in ascii_frame:
                if i == '#':
                   f.write('_pause|')
                elif i == '*':
                    f.write('noteblock_flute|')
                else:
                    f.write('noteblock_guitar|')
                    

        os.system("cls")
    count += 1
    
    print(count)
    time.sleep(0.05)
cap.release()