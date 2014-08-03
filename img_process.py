import cv2
import numpy as np

def imgProcess(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    verticalEdgesImg = verticalEdges(gray)
    color = cv2.cvtColor(verticalEdgesImg, cv2.COLOR_GRAY2RGB)
    color = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    return color
    
def verticalEdges(grayImg):
    sobel_filter_x = np.array([[1, -2, 1], [2, -4, 2], [1, -2, 1]])
    return cv2.filter2D(grayImg, -1, sobel_filter_x)
    