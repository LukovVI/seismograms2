import random
import numpy
import math
import copy
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw
import datetime
import schedule
import time

def png_jpg(str):
    image = Image.open(str + ".png")
    image = image.convert("RGB")
    img = cv2.imread(os.getcwd() + "\\" + str + ".png", 0)
    r, g, b = image.split()
    # draw = ImageDraw.Draw(image)
    # for i in range(80, 3991, 782):
    #     for j in range(0, 2000):
    #         draw.point((i, j), (0, 0, 100))
    # print(os.getcwd(), str)
    # image.save(str + "_final.png")

    # result = np.count_nonzero(np.all(img[100:200, 100:200] == 255, axis = 2))
    # print(result)
    print((img == 0).sum())

def main():
    print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    # for i in list(map(lambda x: x[0:-4], list(filter(lambda x: x.endswith(".png"), os.listdir())))):
    #     png_jpg(i)



if __name__ == '__main__':
    schedule.every(1).minute.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)