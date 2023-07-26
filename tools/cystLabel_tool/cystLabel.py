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
from numpy import unravel_index

class cystLabel(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_cystLabel_widget()
        self.ui.setupUi(self)
        self.setupGlobalConstants()

        self.DUP_ORIG_NP_IMG = 0
        print("HEYOO")
        # connect sliders to spinboxes
        self.ui.lowerThresh_slider.valueChanged.connect(self.ui.lowerThresh_spinBox.setValue)
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.ui.lowerThresh_slider.setValue)

        self.ui.upperThresh_slider.valueChanged.connect(self.ui.upperThresh_spinBox.setValue)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.ui.upperThresh_slider.setValue)

        # connect spinboxes to setContourMask
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.setContourMask)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.setContourMask)

        # set variables to lower and upper threshold values
        self.lowerThresh = self.ui.lowerThresh_spinBox.value()
        self.upperThresh = self.ui.upperThresh_spinBox.value()

        # set ORIG values to default values
        self.ORIG_lowerValue = -1
        self.ORIG_upperValue = -1
        self.ORIG_slice = -1

    def setContourMask(self):
        ''' Setting up ORIG image saving system '''

        # know the current coordinates
        x, y, z = self.IMG_OBJ.FOC_POS

        # set ORIG values to what they are currently
        self.ORIG_lowerValue = self.ui.lowerThresh_spinBox.value()
        self.ORIG_upperValue = self.ui.upperThresh_spinBox.value()
        self.ORIG_slice = z

        # if the type of self.DUP_ORIG_NP_IMG is not int, then it has been created
        if(isinstance(self.DUP_ORIG_NP_IMG, int)):
            self.DUP_ORIG_NP_IMG = self.IMG_OBJ.ORIG_NP_IMG.copy()
        
        # update the image to the original image
        self.IMG_OBJ.ORIG_NP_IMG = self.DUP_ORIG_NP_IMG.copy()
        
        # create duplicate of ORIG_NP_IMG to update in the future
        self.DUP_ORIG_NP_IMG = self.IMG_OBJ.ORIG_NP_IMG.copy()



        ''' Setting up image for thresholding '''

        # create a copy of the image
        img = self.IMG_OBJ.ORIG_NP_IMG[:, :, z].copy()

        # change img from 3D to 2D array
        img = np.stack([img.T, img.T, img.T], axis=-1)

        # set variables to min and max intensities
        min_intensity = self.IMG_OBJ.MIN_MAX_INTENSITIES[0]
        max_intensity = max(self.IMG_OBJ.MIN_MAX_INTENSITIES[1], 1)

        # normalize image to 0-255
        img = ((255.0/max_intensity) * img).astype('uint16')

        # for images use img[y, x] instead of img[x, y]

        # normalize lowerValue and upperValue to 0-255
        lowerValue = int((255.0/max_intensity) * self.ORIG_lowerValue)
        upperValue = int((255.0/max_intensity) * self.ORIG_upperValue)



        ''' Thresholding image '''

        # create a mask of the image within lower and upper threshold
        mask = cv2.inRange(img, (lowerValue, lowerValue, lowerValue), (upperValue, upperValue, upperValue))

        # create bitwise image of mask and original image and convert from numpy array to grayscale
        thresh = cv2.bitwise_and(img, img, mask=mask)
        
        # set current slice min and max intensities
        slice_min_intensity = self.IMG_OBJ.ORIG_NP_IMG[:, :, z].min()
        slice_max_intensity = self.IMG_OBJ.ORIG_NP_IMG[:, :, z].max()

        ''' Converting threshed image to display image '''

        # denormalize thresh from 0-255 to min and max intensities of the slice
        thresh = ((max_intensity/255.0) * thresh).astype('int')

        # rotate thresh 90 degrees
        thresh = np.rot90(thresh, 1)

        # flip thresh vertically
        thresh = np.flipud(thresh)
        
        # change thresh into a 3d numpy array
        thresh = thresh[:, :, 1]

        # display threshed image by replacing NP_IMG with threshed image
        self.IMG_OBJ.ORIG_NP_IMG[:, :, z] = thresh
        # alternate solution: originally used when contrast was still in use
        # self.IMG_OBJ.ORIG_NP_IMG[:, :, z] = np.minimum(thresh, self.IMG_OBJ.ORIG_NP_IMG[:, :, z])

    def segmentButton(self):
        # label all pixels within the mask as a cyst

        # reset the image to the original image
        self.IMG_OBJ.NP_IMG = self.IMG_OBJ.resetNPImg()

    def widgetMouseMoveEvent(self, event, axis):
        x, y, z, xx, yy, margin, shape = self.computePosition(event, axis)
        
        if event.buttons() & QtCore.Qt.LeftButton:
            self.IMG_OBJ.FOC_POS = [x, y, z]

        elif event.buttons() & QtCore.Qt.RightButton:
            diff = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            self.IMG_OBJ.ZOOM_FACTOR *= 1.01**(diff)
            self.IMG_OBJ.ZOOM_FACTOR = clamp(0.3, self.IMG_OBJ.ZOOM_FACTOR, 15)

        elif event.buttons() & QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.position().x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            if axis == 'axi': self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]
            elif axis == 'sag': self.IMG_OBJ.SHIFT = [0, self.IMG_OBJ.SHIFT[1] - diffX, self.IMG_OBJ.SHIFT[2] - diffY]
            elif axis == 'cor': self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, 0, self.IMG_OBJ.SHIFT[2] - diffY]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.position().x(), event.position().y()]

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theCrossPen())
        painter.drawLine(int(margin[0]), int(new_foc[1]+spacing/2),
                         int(margin[0]+newshape[0]), int(new_foc[1]+spacing/2))
        painter.drawLine(int(new_foc[0]+spacing/2), int(margin[1]),
                         int(new_foc[0]+spacing/2), int(margin[1]+newshape[1]))

        return painter

    # constantly updates the functions in the widget
    def widgetUpdate(self): 
        # update curser coordinates
        self.ui.curserX_label.setNum(self.IMG_OBJ.FOC_POS[0])
        self.ui.curserY_label.setNum(self.IMG_OBJ.FOC_POS[1])
        self.ui.curserZ_label.setNum(self.IMG_OBJ.FOC_POS[2]+1)

        # update intensity value at current curser position
        self.ui.minIntensity_label.setNum(round(self.IMG_OBJ.MIN_MAX_INTENSITIES[0], 3))
        self.ui.maxIntensity_label.setNum(round(self.IMG_OBJ.MIN_MAX_INTENSITIES[1], 3))
        self.ui.curIntensity_label.setNum(round(self.IMG_OBJ.ORIG_NP_IMG[self.IMG_OBJ.FOC_POS[0], self.IMG_OBJ.FOC_POS[1], self.IMG_OBJ.FOC_POS[2]], 3))

        # set variables to lower and upper threshold values
        self.lowerThresh = self.ui.lowerThresh_spinBox.value()
        self.upperThresh = self.ui.upperThresh_spinBox.value()

        # update threshold values (auto thresholds each slice) if current spinBox values are different from the original values or we are on a new slice
        if(self.ORIG_lowerValue != self.lowerThresh or self.ORIG_upperValue != self.upperThresh or self.IMG_OBJ.FOC_POS[2] != self.ORIG_slice):
            self.setContourMask()
