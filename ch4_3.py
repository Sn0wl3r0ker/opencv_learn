# ppt 5
import cv2 as cv
import numpy as np
hight = 160
weight = 280
img = np.zeros((hight, weight, 3), np.uint8)
img[:,:,0]=255 #B通道 =255 顯示藍色!
cv.imshow("img",img)
cv.waitKey(0)
