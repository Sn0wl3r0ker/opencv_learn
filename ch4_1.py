import cv2 as cv
import numpy as np
hight = 160
width = 280
img = np.ones((hight, width), np.uint8)*255
cv.imshow("img", img)
cv.waitKey(0)