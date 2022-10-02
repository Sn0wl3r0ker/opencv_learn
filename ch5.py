import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read() #ret為True or False看有沒有讀到
    # height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    # weight = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    lower = np.array([200,200,200])
    upper = np.array([255,255,255])
    mask = cv.inRange(frame, lower, upper)
    output = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('capture vid', output)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()