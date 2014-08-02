import sys
import cv2
from PyQt4 import QtGui, QtCore
 
import numpy as np

class VideoScreen(QtGui.QWidget):

    def __init__(self, mainWindow, parent=None):
        super(VideoScreen, self).__init__(parent)
        self.mainWindow = mainWindow

        self.frame = None

        self.setGeometry( 0, 0, parent.size().width(), parent.size().height() )

    def frame2QImage(self, frame):
        height, width=frame.shape[:2]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return QtGui.QImage(frame, width, height, QtGui.QImage.Format_RGB888)

    def onNewFrame(self, frame):
        self.frame = frame
        self.update()

    def paintEvent(self, e):
        if self.frame is None: return

        painter = QtGui.QPainter(self)
        painter.drawImage(QtCore.QPoint(0, 0), self.frame2QImage(self.frame))
