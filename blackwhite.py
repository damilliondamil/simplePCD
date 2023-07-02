import numpy as np
import cv2

img2 = np.array([[255, 255, 255], [255, 255, 255], [0, 0, 0]])

print(img2)
cv2.imwrite('whiteblack3x3.png', img2)
