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
        
        self.ui.sliderHueMin.valueChanged.connect(self.sliderValueChanged)
        self.ui.sliderHueMax.valueChanged.connect(self.sliderValueChanged)
        self.ui.sliderSaturationMin.valueChanged.connect(self.sliderValueChanged)
        
        self.ui.keepCapturingCheckBox.stateChanged.connect(self.keepCapturingClicked)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.queryFrame)
        
        fps = self.stream.get(cv2.cv.CV_CAP_PROP_FPS)
        if not fps > 0: fps = self.DEFAULT_FPS
        
        self.timer.setInterval(1000/fps)
        self.timer.start()
        self.ui.show()
        
    def process(self):
        self.videoScreen.onNewFrame(self.frame)
        color = img_process.imgProcess(self.frame, self.paramProvider)
        self.outputScreen.onNewFrame(color)

    @QtCore.pyqtSlot()
    def queryFrame(self):
        ret, self.frame = self.stream.read()
        if not ret: return
        self.process()
        
    @QtCore.pyqtSlot()
    def sliderValueChanged(self):
        if(not self.ui.keepCapturingCheckBox.isChecked()):
            self.process()
        
    def keepCapturingClicked(self, state):
        if(state):
            self.timer.start()
        else:
            self.timer.stop()
        
