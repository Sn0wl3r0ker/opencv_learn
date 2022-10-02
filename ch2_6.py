import cv2 as cv
import numpy as np
img = cv.imread(r'images/1.png')
cv.imshow('img',img)
cv.waitKey(0)
x = img.shape[0]
y = img.shape[1]
for i in range(1, x):
    for j in range(1, y):
        if ((img[i,j] == [65,56,48]).all()):
            img[i,j]=[111,102,147]#BGR
cv.imshow('img',img)
cv.waitKey(0)