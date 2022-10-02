#ppt 6
import cv2 as cv
import numpy as np
height = 280
weight = 280
img = np.random.randint(256, size=[height, weight, 3], dtype=np.uint8)
cv.imshow("img", img)
cv.waitKey(0)