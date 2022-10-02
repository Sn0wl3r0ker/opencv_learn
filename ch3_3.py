import cv2 as cv
import numpy as np
lt = cv.imread(r'images/lt.png')
rt = cv.imread(r'images/rt.png')
lb = cv.imread(r'images/lb.png')
rb = cv.imread(r'images/rb.png')
stackV = np.vstack((lt,lb))
stackH = np.hstack((lt,rt))

cv.imshow('stackV', stackV)
cv.imshow('stackH', stackH)
cv.waitKey(0)