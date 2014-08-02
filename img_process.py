import cv2
import numpy as np

def imgProcess(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    sobel_filter_x = np.array([[1, -2, 1], [2, -4, 2], [1, -2, 1]])
    img_filter_x = cv2.filter2D(gray, -1, sobel_filter_x)
    color = cv2.cvtColor(img_filter_x, cv2.COLOR_GRAY2RGB)
    return color