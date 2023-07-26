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
from matplotlib import pyplot as plt
import cv2 as cv2
from PIL import Image

class cystLabel(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_cystLabel_widget()
        self.ui.setupUi(self)
        self.setupGlobalConstants()

        # connect sliders to spinboxes
        self.ui.lowerThresh_slider.valueChanged.connect(self.ui.lowerThresh_spinBox.setValue)
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.ui.lowerThresh_slider.setValue)

        self.ui.upperThresh_slider.valueChanged.connect(self.ui.upperThresh_spinBox.setValue)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.ui.upperThresh_slider.setValue)


        # connect spinboxes to setContourMask
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.setContourMask)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.setContourMask)

    def setContourMask(self):
        # set lower and upper threshold values called from spinbox
        lowerValue = self.ui.lowerThresh_spinBox.value()
        upperValue = self.ui.upperThresh_spinBox.value()

        # create a copy of the image
        x, y, z = self.IMG_OBJ.FOC_POS
        img = self.IMG_OBJ.ORIG_NP_IMG[:, :, z].copy()

        # set contrast of image
        val_win = self.IMG_OBJ.WINDOW_VALUE
        val_lev = self.IMG_OBJ.LEVEL_VALUE

        val_max = val_lev + val_win / 2
        val_min = val_lev - val_win / 2

        img[img > val_max] = val_max
        img[img < val_min] = val_min
        img = (img - val_min)/(val_max-val_min+1e-5)

        img = np.stack([img.T, img.T, img.T], axis=-1)

        # normalize image to 0-255
        img = ((255.0/img.max()) * img).astype('uint8')

        # create a mask of the image within lower and upper threshold
        mask = cv2.inRange(img, (lowerValue, lowerValue, lowerValue), (upperValue, upperValue, upperValue))

        # create bitwise image of mask and original image and convert from numpy array to grayscale
        thresh = cv2.bitwise_and(img, img, mask=mask)

        # display threshed image
        plt.imshow(thresh, interpolation='nearest')
        plt.show()


    def setContrast(self, img):
        

        return img

    def widgetMouseMoveEvent(self, event, axis):
        pass

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theCrossPen())
        
        return painter

    def widgetUpdate(self):
        pass