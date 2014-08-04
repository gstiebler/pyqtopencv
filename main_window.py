import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, uic

from video_screen import VideoScreen 
from param_provider import ParamProvider

import img_process
import viewer_window

class CaptureWindow(QtGui.QMainWindow):

    DEFAULT_FPS = 30

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
 
        self.ui = uic.loadUi('main_window.ui')
        
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
        self.ui.zoomViewButton.clicked.connect(self.openViewerWindow)
        
        self.imgProcess = img_process.ImgProcess()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.queryFrame)
        
        fps = self.stream.get(cv2.cv.CV_CAP_PROP_FPS)
        if not fps > 0: fps = self.DEFAULT_FPS
        
        self.timer.setInterval(1000/fps)
        self.timer.start()
        self.ui.show()
        
    def process(self):
        self.videoScreen.onNewFrame(self.frame)
        color = self.imgProcess.imgProcess(self.frame, self.paramProvider)
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
        
    @QtCore.pyqtSlot()
    def keepCapturingClicked(self):
        if(self.ui.keepCapturingCheckBox.isChecked()):
            self.timer.start()
        else:
            self.timer.stop()
    
    @QtCore.pyqtSlot()
    def openViewerWindow(self):
        self.win = viewer_window.ViewerWindow(self.frame)
