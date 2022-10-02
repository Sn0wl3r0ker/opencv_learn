import cv2 as cv
import numpy as np
img = cv.imread(r'images/rgb.png')
b,g,r = cv.split(img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)
cv.waitKey(0)
img_merge = cv.merge([b,g,r])
print(f'{img_merge.ndim}')
cv.imshow('merge', img_merge)
cv.waitKey(0)