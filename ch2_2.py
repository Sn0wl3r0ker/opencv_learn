import cv2 as cv
import numpy as np
x = np.array([1,2,3])
print(f"type{type(x)}")
print(f"size:{x.size}")
print(f"shape:{x.shape}")#元素個數得位元組，用resize可以變更陣列大小
print(f"dim:{x.ndim}")  #維度