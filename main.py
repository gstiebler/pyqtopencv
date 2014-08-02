import sys
from PyQt4 import QtGui
 
import main_window
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = main_window.CaptureWindow()
    sys.exit(app.exec_())