import os
import cv2
import pandas as pd
import openpyxl
import numpy as np
import requests

link = "http://emsd.ru/~ddv/smkshe.png"
name = link.split("/")[-1][:-4]
print(name)
# r = requests.get(link, allow_redirects=True).raw
# image = np.asarray(bytearray(r.read()), dtype="uint8")
# image = cv2.imdecode(image, 0)
url = r'http://emsd.ru/~ddv/smkshe.png'
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, 0)

# for testing
cv2.imwrite(name + "_final.png", image)
cv2.imshow('image', image)

cv2.waitKey(0)

