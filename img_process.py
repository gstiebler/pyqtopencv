import cv2
import numpy as np

class ImgProcess():

    def __init__(self):
        self.hsvImg = np.zeros((480,640,3), np.uint8)
        self.h = np.zeros((480,640), np.uint8)
        self.s = np.zeros((480,640), np.uint8)
        self.v = np.zeros((480,640), np.uint8)
        self.hMask = np.zeros((480,640), np.uint8)
        self.sMask = np.zeros((480,640), np.uint8)
        self.lMask = np.zeros((480,640), np.uint8)
        self.finalMask = np.zeros((480,640), np.uint8)
        self.processedHsv = np.zeros((480,640,3), np.uint8)
        self.resultImg = np.zeros((480,640,3), np.uint8)

    def imgProcess(self, frame, paramProvider):
        #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        #verticalEdgesImg = verticalEdges(gray)
        #color = cv2.cvtColor(verticalEdgesImg, cv2.COLOR_GRAY2RGB)
        color = self.hsvProcess(frame, paramProvider)
        return color
        
    def verticalEdges(self, grayImg):
        sobel_filter_x = np.array([[1, -2, 1], [2, -4, 2], [1, -2, 1]])
        return cv2.filter2D(grayImg, -1, sobel_filter_x)
        
    def hsvProcess(self, inputColorImg, paramProvider):
        cv2.cvtColor(inputColorImg, cv2.COLOR_RGB2HSV, self.hsvImg)
        cv2.split(self.hsvImg, [self.h, self.s, self.v])
        #h = cv2.blur(h,(5,5))
        hueMin = paramProvider.getParam("hueMin")
        hueMax = paramProvider.getParam("hueMax")
        satMin = paramProvider.getParam("satMin")
        lumMin = paramProvider.getParam("lumMin")
        cv2.inRange(self.h, hueMin, hueMax, self.hMask)
        cv2.inRange(self.s, satMin, 255, self.sMask)
        cv2.inRange(self.v, lumMin, 255, self.lMask)
        cv2.bitwise_and(self.hMask, self.sMask, self.finalMask)
        cv2.bitwise_and(self.lMask, self.finalMask, self.finalMask)
        cv2.merge((self.h, self.finalMask, self.v), self.processedHsv)
        cv2.cvtColor(self.processedHsv, cv2.COLOR_HSV2RGB, self.resultImg)
        return self.resultImg
        