import cv2 as cv
img=cv.imread(r'images/traffic_light.png')
cv.rectangle(img, (93,50), (122,85), (0,0,255), 3)
cv.rectangle(img, (93,95), (122,130), (0,255,255), 3)
cv.rectangle(img, (93,135), (122,170), (0,255,0), 3)
cv.imshow('img', img)
cv.waitKey(0)
cv.imwrite(r'images/traffic_marked.png', img)