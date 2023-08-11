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

        # set duplicate to a non-image value so we know we haven't touched it yet
        self.DUP_ORIG_NP_IMG = 0

        # connect sliders to spinboxes
        self.ui.lowerThresh_slider.valueChanged.connect(self.ui.lowerThresh_spinBox.setValue)
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.ui.lowerThresh_slider.setValue)

        self.ui.upperThresh_slider.valueChanged.connect(self.ui.upperThresh_spinBox.setValue)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.ui.upperThresh_slider.setValue)

        # connect threshold spinboxes to setContourMask
        self.ui.lowerThresh_spinBox.valueChanged.connect(self.setContourMask)
        self.ui.upperThresh_spinBox.valueChanged.connect(self.setContourMask)

        # connect segment button to segmentButton
        self.ui.segment.clicked.connect(self.segmentButton)

        # connect toggle button to toggleButton
        self.ui.toggle.clicked.connect(self.toggleButton)  



        # set ORIG values to default values (for updating purposes in widgetUpdate)
        self.ORIG_lowerValue = -1
        self.ORIG_upperValue = -1
        self.ORIG_slice = -1
        self.thresh = -1
        self.leftKidney = -1
        self.rightKidney = -1
        self.liver = -1
        
        self.toggle = False
        self.PAST_lowerValue = -1
        self.PAST_upperValue = -1

    def setContourMask(self):

        print("running setContourMask")
        ''' Setting up ORIG image saving system '''

        # know the current coordinates
        x, y, z = self.IMG_OBJ.FOC_POS

        print(type(self.MSK_OBJ.CURRENT_LBL))
        print(type(self.MSK_OBJ.MSK[0, 0, 0]))
        print(self.MSK_OBJ.MSK[x, y, z])

        # set past values to what they are before updating
        self.PAST_lowerValue = self.ORIG_lowerValue
        self.PAST_upperValue = self.ORIG_upperValue

        # set ORIG values to what they are currently
        self.ORIG_lowerValue = self.ui.lowerThresh_spinBox.value()
        self.ORIG_upperValue = self.ui.upperThresh_spinBox.value()
        self.ORIG_slice = z
        
        # connect kidneys to the Kidney_comboBox
        self.leftKidney = 2 #self.ui.leftKidney_spinBox.value() # should be 2
        self.rightKidney = 1 #self.ui.rightKidney_spinBox.value() # should be1
        self.liver = 4

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
        upperValue = min(int((255.0/max_intensity) * self.ORIG_upperValue), 255)

        print(upperValue, "FDSLJKFKDFD", max_intensity)

        ''' Thresholding image '''

        # create a mask of the image within lower and upper threshold
        mask = cv2.inRange(img, (lowerValue, lowerValue, lowerValue), (upperValue, upperValue, upperValue))

        #ret, mask = cv2.threshold(img, lowerValue, upperValue, cv2.THRESH_BINARY)
        # mask = mask[:, :, 1]
        # mask = mask.clip(min=0, max=1)
        # mask = mask.astype('uint8')

        # add the kidneys to the mask
        currMask = self.MSK_OBJ.MSK[:, :, z].copy().astype('uint16')
        currMask = np.stack([currMask.T, currMask.T, currMask.T], axis=-1)
        currMask = currMask[:, :, 1]

        leftKidneyMask = np.zeros(currMask.shape, dtype='uint8')
        rightKidneyMask = np.zeros(currMask.shape, dtype='uint8')
        liverMask = np.zeros(currMask.shape, dtype='uint8')
        cystMask = np.zeros(currMask.shape, dtype='uint8')
        completeMask = np.zeros(currMask.shape, dtype='uint8')

        # get the kidney mask
        if(self.ui.leftKidney_toggle.isChecked()):
            leftKidneyMask = np.where(currMask == self.leftKidney, 1, 0)

        # get the kidney mask
        if(self.ui.rightKidney_toggle.isChecked()):
            rightKidneyMask = np.where(currMask == self.rightKidney, 1, 0)

        # get the kidney mask
        if(self.ui.liver_toggle.isChecked()):
            liverMask = np.where(currMask == self.liver, 1, 0)

        # get the cyst mask
        cystmask = np.where(currMask == 20, 1, 0)
        
        # add the masks together
        completeMask = leftKidneyMask | rightKidneyMask | cystmask | liverMask
        completeMask = completeMask.astype('uint8')

        # if the lower threshold is zero, we want to let the user see everything in the image
        if(self.ORIG_lowerValue > 0 or self.ORIG_upperValue < 5000):
            # add the kidney mask to the mask but only where both kidney mask and mask are 1 using np.bitwise_and
            mask = mask & completeMask
        
        mask = mask.astype('uint8')

        # fill all contours in mask
        contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]
        cv2.drawContours(mask, contours, -1, 1, thickness=-1)
        
        # semi see through mask
        # mask = mask.astype('float')
        # mask[mask == 0] = 0.0
        # mask = mask[:, :, np.newaxis]
        # thresh = img * mask
        #thresh = thresh.astype('uint8')
        
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

        # set self.img to thresh
        self.thresh = thresh

        # display threshed image by replacing NP_IMG with threshed image
        self.IMG_OBJ.ORIG_NP_IMG[:, :, z] = thresh
        # alternate solution: originally used when contrast was still in use
        # self.IMG_OBJ.ORIG_NP_IMG[:, :, z] = np.minimum(thresh, self.IMG_OBJ.ORIG_NP_IMG[:, :, z])

    def segmentButton(self):

        if(self.ui.lowerThresh_spinBox.value() == 0):
            return
        # label all pixels within the mask as a cyst
        print("segmenting cysts")

        # know the current coordinates
        x, y, z = self.IMG_OBJ.FOC_POS

        # find all non-zero pixels in img
        non_zero_pixels = np.nonzero(self.thresh)
        
        # for each non-zero pixel, label it as a cyst in self.MSK_OBJ.MSK using numpy fancy indexing, TODO: replace brush function with this since it is faster
        self.MSK_OBJ.MSK[non_zero_pixels[0], non_zero_pixels[1], z] = self.MSK_OBJ.CURRENT_LBL


        print("finished segmenting cysts")


    def toggleButton(self):

        if(self.ORIG_lowerValue > 0 or self.ORIG_upperValue < 5000):
            # reset the image to the original image
            self.ui.lowerThresh_spinBox.setValue(0)
            self.ui.upperThresh_spinBox.setValue(5000)
            self.toggle = True
        else:
            # reset the image to the original image
            self.ui.lowerThresh_spinBox.setValue(self.PAST_lowerValue)
            self.ui.upperThresh_spinBox.setValue(self.PAST_upperValue)
            self.toggle = False

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
        
        # update threshold values (auto thresholds each slice) if we're on a new slice and threshold is on
        if(self.IMG_OBJ.FOC_POS[2] != self.ORIG_slice and self.ORIG_lowerValue > 0):
            self.setContourMask()
