import cv2 as cv
import numpy as np
img = cv.imread(r'images/traffic_light.png')
cv.imshow('img',img)
cv.waitKey(0)
x = img.shape[0]
y = img.shape[1]
yellow = [28,217,248]
for i in range(1, x):
    for j in range(1, y):
        if ((img[i,j] == yellow).all()):
            img[i,j]=[100,102,147]#BGR
cv.imshow('img',img)
cv.imwrite(r'images/traffic_changed.png',img)
cv.waitKey(0)