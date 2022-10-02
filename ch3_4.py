import cv2 as cv
import numpy as np

img = cv.imread(r'images/origin.png')
b,g,r = cv.split(img)
rg = np.hstack((r,g))
rg = cv.cvtColor(rg, cv.COLOR_GRAY2BGR)
b = cv.cvtColor(b, cv.COLOR_GRAY2BGR)
bo = np.hstack((b,img))
merge = np.vstack((rg,bo))

cv.imwrite(r'images/merge.png', merge)
cv.imshow('final', merge)
cv.waitKey(0)