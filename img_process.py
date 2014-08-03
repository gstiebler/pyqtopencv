import cv2
import numpy as np

def imgProcess(frame, paramProvider):
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #verticalEdgesImg = verticalEdges(gray)
    #color = cv2.cvtColor(verticalEdgesImg, cv2.COLOR_GRAY2RGB)
    color = hsvProcess(frame, paramProvider)
    return color
    
def verticalEdges(grayImg):
    sobel_filter_x = np.array([[1, -2, 1], [2, -4, 2], [1, -2, 1]])
    return cv2.filter2D(grayImg, -1, sobel_filter_x)
    
def hsvProcess(inputColorImg, paramProvider):
    color = cv2.cvtColor(inputColorImg, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(color)
    s.fill(255)
    h = cv2.blur(h,(5,5))
    min = paramProvider.getParam("min")
    max = paramProvider.getParam("max")
    hMask = cv2.inRange(h, min, max)
    img = cv2.merge((h, hMask, v))
    return cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    