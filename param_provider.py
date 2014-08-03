
from PyQt4 import QtGui

class ParamProvider():
    
    def __init__(self):
        self.paramMap = {}
    
    def addSlider(self, slider, paramName):
        self.paramMap[paramName] = slider
        
    def getParam(self, paramName):
        return self.paramMap[paramName].value()