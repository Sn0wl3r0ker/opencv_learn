#ppt 7
import cv2 as cv
import numpy as np
height = 150
weight = 300
img = np.zeros((height, weight, 3), dtype=np.uint8)
img[0:50,:,0] = 255
img[50:100,:,1] = 255
img[100:150,:,2] = 255
cv.imshow("img", img)
cv.waitKey(0)