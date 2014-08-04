import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, uic

from video_screen import VideoScreen 

class ViewerWindow(QtGui.QMainWindow):

    def __init__(self, image):
        QtGui.QMainWindow.__init__(self)
 
        self.ui = uic.loadUi('viewer_window.ui')
        self.videoScreen = VideoScreen(self, self.ui.imageCanvas)
        self.videoScreen.onNewFrame(image)
        self.ui.imageCanvas.setMinimumSize ( 640, 480 )
        self.ui.show()