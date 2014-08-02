import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, uic

from video_screen import VideoScreen 

class CaptureWindow(QtGui.QMainWindow):

    DEFAULT_FPS = 30

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
 
        self.ui = uic.loadUi('window.ui')
        self.ui.lineEdit.setText("qt python")
        
        self.stream = cv2.VideoCapture(1)
        
        
        self.stream.set(3, self.ui.inputCamStream.size().width())
        self.stream.set(4, self.ui.inputCamStream.size().height())
        
        self.videoScreen = VideoScreen(self, self.ui.inputCamStream)
        self.outputScreen = VideoScreen(self, self.ui.outputCanvas)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.queryFrame)
        
        fps = self.stream.get(cv2.cv.CV_CAP_PROP_FPS)
        if not fps > 0: fps = self.DEFAULT_FPS
        
        self.timer.setInterval(1000/fps)
        self.timer.start()
        self.ui.show()

    @QtCore.pyqtSlot()
    def queryFrame(self):
        ret, frame = self.stream.read()
        if not ret: return

        self.videoScreen.onNewFrame(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        sobel_filter_x = np.array([[1, -2, 1], [2, -4, 2], [1, -2, 1]])
        img_filter_x = cv2.filter2D(gray, -1, sobel_filter_x)
        color = cv2.cvtColor(img_filter_x, cv2.COLOR_GRAY2RGB)
        self.outputScreen.onNewFrame(color)