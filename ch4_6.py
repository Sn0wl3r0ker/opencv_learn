# ppt practice
import cv2 as cv
import numpy as np
height = 210
weight = 210
img = np.ones((height, weight, 3), dtype=np.uint8)*255
img[0:100,0:100,0:2] = 0
img[0:100,110:,0:3:2] = 0
img[110:,0:100,1:3] = 0
img[110:,110:,0] = 0
cv.imshow("img", img)
cv.waitKey(0)