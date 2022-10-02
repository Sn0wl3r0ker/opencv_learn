import cv2 as cv
import numpy as np
# img = cv.imread(r"images/1.png")
img = cv.imread(r"images/1.png", cv.IMREAD_GRAYSCALE)
print(f"type{type(img)}")
print(f"size:{img.size}")
print(f"shape:{img.shape}")#元素個數得位元組，用resize可以變更陣列大小
print(f"dim:{img.ndim}")  #維度