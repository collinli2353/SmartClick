import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
import numpy as np
from tools.default_tool import Meta, default_tool
from tools.cystLabel_tool.ui_cystLabel import ui_cystLabel
from utils.utils import theBrushPen

'''
Cyst Label Tool
TODO: Change name to cyst segmentation tool & create a cyst label tool for bounding box of these cysts

Created to label hemmorhagic cysts in the kidney. 
First takes in a mask of the organs and user selects which # the kidneys are.
Then the user sets a lower and upper threshold for the cysts. (low should be set to intesity of muscle)
Once the thresholds are set, the user can press a process button to segment all cysts within the mask.
This segmentation will be semantic and not instance based.
'''

class cystLabel(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ui_cystLabel()
        self.ui.setupUi(self)
        self.setupGlobalConstants()

        # Setup Local Constants
        self.brush_size = 15
        self.brush_type = 'local'
        self.brush_dim = '2D'
        self.ui.levelsetSize_label.setText(str(self.brush_size))
        self.ui.levelsetSize_slider.setValue(int(self.brush_size))

        def setBrushType(type, dim):
            self.brush_type = type
            self.brush_dim = dim
            self.IMG_OBJ.UPDATE_VIEWERS()
        
        def setBrushSize(size):
            self.brush_size = size
            self.ui.levelsetSize_label.setText(str(size))
            self.IMG_OBJ.UPDATE_VIEWERS()

        self.ui.levelset2D_button.clicked.connect(lambda: setBrushType(self.brush_type, '2D'))
        self.ui.levelset3D_button.clicked.connect(lambda: setBrushType(self.brush_type, '3D'))
        self.ui.levelsetAuto_button.clicked.connect(lambda: setBrushType('auto', self.brush_dim))
        self.ui.levelsetLocal_button.clicked.connect(lambda: setBrushType('local', self.brush_dim))

        self.ui.levelsetSize_slider.valueChanged.connect(setBrushSize)

    def normMinMax(self, img, msk=None, p_val=None, ll=0, rr=255):
        new_img = np.zeros(img.shape)
        if msk is not None:
            min_val = np.min(img[msk > 0])
            max_val = np.max(img[msk > 0])
            new_img = (img - min_val) / (max_val - min_val) * (rr-ll) + ll
        else:
            min_val = np.min(img)
            max_val = np.max(img)
            new_img = ((img - min_val) / (max_val - min_val)) * (rr-ll) + ll

        if p_val is not None:
            p_val = (p_val - min_val) / (max_val - min_val) * (rr-ll) + ll

            return new_img, p_val

        return new_img

    def widgetMouseMoveEvent(self, event, axis):
        x, y, z, xx, yy, margin, shape = self.computePosition(event, axis)
        xx, yy, w, h = self.computeCoords(xx, yy, self.brush_size, self.brush_size, shape)
        self.IMG_OBJ.POINT_POS = [x, y, z]
        
        if event.buttons() & PySide6.QtCore.Qt.LeftButton:
            if self.brush_dim == '2D':
                if axis == 'axi':
                    ls_msk = self.runLevelSet2D(self.IMG_OBJ.NP_IMG[:, :, z], xx-w//2, yy-h//2, w, h, xx, yy, 1, 1)
                    print(ls_msk.sum())
                    if self.brush_type == 'local': ls_msk = self.recursive(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2)
                    pos = (ls_msk > 0)
                    t_msk = self.MSK_OBJ.MSK[:, :, z]
                    xx, yy = xx-w//2, yy-h//2
                    t_msk[xx:xx+w, yy:yy+h][pos] = self.MSK_OBJ.CURRENT_LBL
                    self.MSK_OBJ.MSK[:, :, z] = t_msk
                # elif axis == 'cor':
                #     ls_msk = self.runLevelSet2D(self.IMG_OBJ.NP_IMG[x, :, :], xx-w//2, yy-h//2, w, h, xx, yy, 1, 1)
                #     if self.brush_type == 'local': ls_msk = self.recursive(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2)
                #     pos = (ls_msk > 0)
                #     t_msk = self.MSK_OBJ.MSK[x, :, :]
                #     xx, yy = xx-w//2, yy-h//2
                #     t_msk[xx:xx+w, yy:yy+h][pos] = self.MSK_OBJ.CURRENT_LBL
                #     self.MSK_OBJ.MSK[x, :, :] = t_msk
                # elif axis == 'sag':
                #     ls_msk = self.runLevelSet2D(self.IMG_OBJ.NP_IMG[:, y, :], xx-w//2, yy-h//2, w, h, xx, yy, 1, 1)
                #     if self.brush_type == 'local': ls_msk = self.recursive(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2)
                #     pos = (ls_msk > 0)
                #     t_msk = self.MSK_OBJ.MSK[:, y, :]
                #     xx, yy = xx-w//2, yy-h//2
                #     t_msk[xx:xx+w, yy:yy+h][pos] = self.MSK_OBJ.CURRENT_LBL
                #     self.MSK_OBJ.MSK[:, y, :] = t_msk
            
            elif self.brush_dim == '3D':
                w = min(w, h)
                ls_msk = self.runLevelSet3D(self.IMG_OBJ.NP_IMG, x-w//2, y-w//2, z-4//2, w, w, 4, x, y, z, 1, 1, 1)
                # if self.brush_type == 'local': ls_msk = self.recursive3D(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2, ls_msk.shape[2]//2)
                pos = (ls_msk > 0)
                x, y, z = x-w//2, y-w//2, z-4//2
                self.MSK_OBJ.MSK[x:x+w, y:y+w, z:z+4][pos] = self.MSK_OBJ.CURRENT_LBL

        elif event.buttons() & PySide6.QtCore.Qt.RightButton:
            if axis == 'axi':
                self.MSK_OBJ.MSK[xx-w//2:xx+w//2, yy-h//2:yy+h//2, z] = 0
            elif axis == 'cor':
                self.MSK_OBJ.MSK[x, xx-w//2:xx+w//2, yy-h//2:yy+h//2] = 0
            elif axis == 'sag':
                self.MSK_OBJ.MSK[xx-w//2:xx+w//2, y, yy-h//2:yy+h//2] = 0

        elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.position().x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.position().y()
            self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.position().x(), event.position().y()]

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theBrushPen(lbl=self.MSK_OBJ.CURRENT_LBL))
        cx, cy = new_point[0], new_point[1]          
        cx, cy = np.round((cx-margin[0])/zoom), np.round((cy-margin[1])/zoom)
        s_x, s_y = cx - self.brush_size // 2, cy - self.brush_size // 2 
        s_x = s_x * zoom + margin[0]
        s_y = s_y * zoom + margin[1]
        w = self.brush_size * zoom
        
        if self.brush_type == 'local':
            painter.drawLine(int(new_point[0]+spacing/2-5), int(new_point[1]+spacing/2),
                            int(new_point[0]+spacing/2+5), int(new_point[1]+spacing/2))
            painter.drawLine(int(new_point[0]+spacing/2), int(new_point[1]+spacing/2-5),
                            int(new_point[0]+spacing/2), int(new_point[1]+spacing/2+5))

        painter.drawLine(s_x,s_y,s_x,s_y+w)
        painter.drawLine(s_x,s_y,s_x+w,s_y)
        painter.drawLine(s_x+w,s_y+w,s_x,s_y+w)
        painter.drawLine(s_x+w,s_y+w,s_x+w,s_y)

        return painter
