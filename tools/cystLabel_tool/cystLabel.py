'''
Cyst Label Tool
TODO: Change name to cyst segmentation tool & create a cyst label tool for bounding box of these cysts

Created to label hemmorhagic cysts in the kidney. 
First takes in a mask of the organs and user selects which # the kidneys are.
Then the user sets a lower and upper threshold for the cysts. (low should be set to intesity of muscle)
Once the thresholds are set, the user can press a process button to segment all cysts within the mask.
This segmentation will be semantic and not instance based.
'''

#TODO: this abstract class does not give any functionality... rippp please fix it so that all tools must include these methods

import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
import numpy as np
from tools.cystLabel_tool.ui_cystLabel_widget import Ui_cystLabel_widget
from tools.default_tool import Meta, default_tool
from utils.utils import theBrushPen, clamp, theCrossPen

class cystLabel(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_cystLabel_widget()
        self.ui.setupUi(self)
        self.setupGlobalConstants()

        self.ui.lowerThresh_slider.valueChanged.connect(self.ui.lowerThresh_spinBox.setValue)
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.ui.lowerThresh_slider.setValue)

        self.ui.upperThresh_slider.valueChanged.connect(self.ui.upperThresh_spinBox.setValue)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.ui.upperThresh_slider.setValue)


        #self.ui.lowerThresh_slider.valueChanged.connect(self.ui.lowerThresh_spinBox)


    def setLowerThreshold(self, value):
        self.IMG_OBJ.LOWER_VALUE = value
        self.ui.winVal_slider.setValue(value)
        self.ui.winVal_label.setText(str(value))

    def setUpperThreshold(self, value):
        self.IMG_OBJ_UPPER_VALUE = value
        self.ui.levVal_slider.setValue(value)
        self.ui.levVal_label.setText(str(value))


    def widgetMouseMoveEvent(self, event, axis):
        pass

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theCrossPen())
        
        return painter

    def widgetUpdate(self):
        pass