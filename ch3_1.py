import cv2 as cv
import numpy as np
img = cv.imread(r'images/1.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('img', img)
cv.waitKey(0)
cv.imshow('gray', img_gray)
cv.waitKey(0)
cv.imshow('hsv', img_hsv)
cv.waitKey(0)