import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, uic

from video_screen import VideoScreen 
from param_provider import ParamProvider

import img_process

class CaptureWindow(QtGui.QMainWindow):

    DEFAULT_FPS = 30

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
 
        self.ui = uic.loadUi('window.ui')
        self.ui.lineEdit.setText("qt python")
        
        self.stream = cv2.VideoCapture(0)
        
        self.stream.set(3, self.ui.inputCamStream.size().width())
        self.stream.set(4, self.ui.inputCamStream.size().height())
        
        self.videoScreen = VideoScreen(self, self.ui.inputCamStream)
        self.outputScreen = VideoScreen(self, self.ui.outputCanvas)
        
        self.paramProvider = ParamProvider()
        self.paramProvider.addSlider(self.ui.sliderHueMin, "hueMin")
        self.paramProvider.addSlider(self.ui.sliderHueMax, "hueMax")
        self.paramProvider.addSlider(self.ui.sliderSaturationMin, "satMin")

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
        color = img_process.imgProcess(frame, self.paramProvider)
        self.outputScreen.onNewFrame(color)
