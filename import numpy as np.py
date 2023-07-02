import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1 = cv.imread('messi5.jpg')
ball = img1 [280: 340, 330: 390]
img1 [273: 333, 100: 160] = ball
cv.imshow('citra rubah', img1)
cv.waitKey(0)

