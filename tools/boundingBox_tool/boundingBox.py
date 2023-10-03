#TODO: this abstract class does not give any functionality... rippp please fix it so that all tools must include these methods

import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QRubberBand, QGraphicsView
from PySide6.QtCore import QPoint, QRect, QSize, Qt, Signal
import numpy as np
from tools.boundingBox_tool.ui_boundingBox_widget import Ui_boundingBox_widget
from tools.default_tool import Meta, default_tool
from utils.globalConstants import IMG_OBJ, MSK_OBJ, TOOL_OBJ
from utils.utils import theBrushPen, clamp, theCrossPen
from matplotlib import pyplot as plt
import cv2 as cv2
from PIL import Image
from numpy import unravel_index
import torch
import matplotlib.pyplot as plt
import sys
from segment_anything import sam_model_registry, SamPredictor


class boundingBox(QtWidgets.QWidget, default_tool, metaclass=Meta):    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_boundingBox_widget()
        self.ui.setupUi(self)
        self.setupGlobalConstants()

        sam_checkpoint = "sam_vit_h_4b8939.pth"
        model_type = "vit_h"

        device = "mps"

        sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
        sam.to(device=device)
        self.predictor = SamPredictor(sam)
        self.Axis = 'axi'
        self.prevSlice = -1

    def show_mask(self, mask, z, random_color=False):
        if random_color:
            color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
        else:
            color = np.array([30/255, 144/255, 255/255, 0.6])
        h, w = mask.shape[-2:]
        mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)

        # rotate mask_image to match the orientation of the image
        mask_image = np.rot90(mask_image, k=1, axes=(0, 1))

        # reflect mask_image over y axis to match the orientation of the image
        mask_image = np.flip(mask_image, axis=0)

        # find all non-zero pixels in img
        non_zero_pixels = np.nonzero(mask_image)
        
        # for each non-zero pixel, label it as a cyst in self.MSK_OBJ.MSK using numpy fancy indexing, TODO: replace brush function with this since it is faster
        self.MSK_OBJ.MSK[non_zero_pixels[0], non_zero_pixels[1], z] = self.MSK_OBJ.CURRENT_LBL

    
    def show_points(self, coords, labels, ax, marker_size=375):
        pos_points = coords[labels==1]
        neg_points = coords[labels==0]
        ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='o', s=marker_size, edgecolor='white', linewidth=1.25)
        ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='o', s=marker_size, edgecolor='white', linewidth=1.25)   
        
    def show_box(self, box, ax):
        x0, y0 = box[0], box[1]
        w, h = box[2] - box[0], box[3] - box[1]
        ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))   

    def predictMask(self): 
        print("STARTTTINGGGG")  
        x, y, z = self.IMG_OBJ.FOC_POS
         
        # create a copy of the image
        img = self.IMG_OBJ.ORIG_NP_IMG[:, :, z].copy()

        # change img from 3D to 2D array
        img = np.stack([img.T, img.T, img.T], axis=-1)

        # set variables to min and max intensities
        min_intensity = self.IMG_OBJ.MIN_MAX_INTENSITIES[0]
        max_intensity = max(self.IMG_OBJ.MIN_MAX_INTENSITIES[1], 1)

        # normalize image to 0-255
        image = ((255.0/max_intensity) * img).astype('uint8')
        print(type(image))
        print(image.shape)
        print(image.shape[0])

        self.predictor.set_image(image)

        input_point = np.array([[220, 140]])
        input_label = np.array([1])

        # plt.figure(figsize=(10,10))
        # plt.imshow(image)
        # self.show_points(input_point, input_label, plt.gca())
        # plt.axis('on')
        # plt.show()  

        masks, scores, logits = self.predictor.predict(
        point_coords=input_point,
        point_labels=input_label,
        multimask_output=False,
        )

        print(masks.shape)

        for i, (mask, score) in enumerate(zip(masks, scores)):
            # plt.figure(figsize=(10,10))
            # plt.imshow(image)
            # print(type(mask), mask.shape)
            # self.show_mask(mask, z)
            # self.show_points(input_point, input_label, z)
            # plt.title(f"Mask {i+1}, Score: {score:.3f}", fontsize=18)
            # plt.axis('off')
            # plt.show()  
            self.show_mask(mask, z)

        self.prevSlice = z

    def widgetMouseReleaseEvent(self, event):
        axis = self.Axis
        x, y, z = self.IMG_OBJ.FOC_POS
        positive_label = 1008
        negative_label = 1009
        if event.button() == Qt.MouseButton.LeftButton:
            if axis == 'axi': self.MSK_OBJ.MSK[x-1:x+1, y-1:y+1, z] = positive_label #positive label for SAM model
            elif axis == 'sag': self.MSK_OBJ.MSK[x, y-1:y+1, z-1:z+1] = positive_label #positive label for SAM model
            elif axis == 'cor': self.MSK_OBJ.MSK[x-1:x+1, y, z-1:z+1] = positive_label #positive label for SAM model
            
            
        elif event.button() == Qt.MouseButton.RightButton:
            if axis == 'axi': self.MSK_OBJ.MSK[x-1:x+1, y-1:y+1, z] = negative_label #positive label for SAM model
            elif axis == 'sag': self.MSK_OBJ.MSK[x, y-1:y+1, z-1:z+1] = negative_label #positive label for SAM model
            elif axis == 'cor': self.MSK_OBJ.MSK[x-1:x+1, y, z-1:z+1] = negative_label #positive label for SAM model
            
  

    
    def widgetMouseMoveEvent(self, event, axis):
        x, y, z, xx, yy, margin, shape = self.computePosition(event, axis)
        self.Axis = axis
        if event.buttons() & QtCore.Qt.LeftButton:
            self.IMG_OBJ.FOC_POS = [x, y, z]

        elif event.buttons() & QtCore.Qt.RightButton:
            self.IMG_OBJ.FOC_POS = [x, y, z]

        elif event.buttons() & QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.position().x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            if axis == 'axi': self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]
            elif axis == 'sag': self.IMG_OBJ.SHIFT = [0, self.IMG_OBJ.SHIFT[1] - diffX, self.IMG_OBJ.SHIFT[2] - diffY]
            elif axis == 'cor': self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, 0, self.IMG_OBJ.SHIFT[2] - diffY]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.position().x(), event.position().y()]

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)

        return painter
    


    # constantly updates the functions in the widget
    def widgetUpdate(self): 
        # update curser coordinates

        if self.ui.rightKidney_spinBox.value() == 2 and self.prevSlice != self.IMG_OBJ.FOC_POS[2]:
            self.predictMask()
