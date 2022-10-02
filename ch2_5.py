import cv2 as cv
import numpy as np
lower = np.array([200,150,31])#轉換成Numpy陣列範圍稍微變小
upper = np.array([225,190,51])#轉換成Numpy陣列範圍稍微加大
img = cv.imread(r"images/1.png")
mask = cv.inRange(img,lower,upper)
output = cv.bitwise_and(img,img, mask=mask) #套用影像遮照
cv.imshow("output", output)
cv.waitKey(0)