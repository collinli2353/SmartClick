# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'curserWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_curserWidget(object):
    def setupUi(self, curserWidget):
        if not curserWidget.objectName():
            curserWidget.setObjectName(u"curserWidget")
        curserWidget.resize(178, 256)
        self.verticalLayout = QVBoxLayout(curserWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.curser_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer)

        self.curserPos_label = QLabel(curserWidget)
        self.curserPos_label.setObjectName(u"curserPos_label")
        self.curserPos_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.curserPos_label)

        self.cursorPos_frame = QFrame(curserWidget)
        self.cursorPos_frame.setObjectName(u"cursorPos_frame")
        self.cursorPos_frame.setMaximumSize(QSize(16777215, 35))
        self.cursorPos_frame.setFrameShape(QFrame.StyledPanel)
        self.cursorPos_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.cursorPos_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.curserX_label = QLabel(self.cursorPos_frame)
        self.curserX_label.setObjectName(u"curserX_label")

        self.horizontalLayout_2.addWidget(self.curserX_label)

        self.curserY_label = QLabel(self.cursorPos_frame)
        self.curserY_label.setObjectName(u"curserY_label")

        self.horizontalLayout_2.addWidget(self.curserY_label)

        self.curserZ_label = QLabel(self.cursorPos_frame)
        self.curserZ_label.setObjectName(u"curserZ_label")

        self.horizontalLayout_2.addWidget(self.curserZ_label)


        self.verticalLayout.addWidget(self.cursorPos_frame)

        self.curserIntensity_label = QLabel(curserWidget)
        self.curserIntensity_label.setObjectName(u"curserIntensity_label")
        self.curserIntensity_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.curserIntensity_label)

        self.curserIntensity_frame = QFrame(curserWidget)
        self.curserIntensity_frame.setObjectName(u"curserIntensity_frame")
        self.curserIntensity_frame.setMaximumSize(QSize(16777215, 35))
        self.curserIntensity_frame.setFrameShape(QFrame.StyledPanel)
        self.curserIntensity_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.curserIntensity_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.minIntensity_label = QLabel(self.curserIntensity_frame)
        self.minIntensity_label.setObjectName(u"minIntensity_label")

        self.horizontalLayout_9.addWidget(self.minIntensity_label)

        self.maxIntensity_label = QLabel(self.curserIntensity_frame)
        self.maxIntensity_label.setObjectName(u"maxIntensity_label")

        self.horizontalLayout_9.addWidget(self.maxIntensity_label)

        self.curIntensity_label = QLabel(self.curserIntensity_frame)
        self.curIntensity_label.setObjectName(u"curIntensity_label")

        self.horizontalLayout_9.addWidget(self.curIntensity_label)


        self.verticalLayout.addWidget(self.curserIntensity_frame)

        self.label = QLabel(curserWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.winVal_spinBox = QSpinBox(curserWidget)
        self.winVal_spinBox.setObjectName(u"winVal_spinBox")
        self.winVal_spinBox.setMaximum(2000)

        self.horizontalLayout.addWidget(self.winVal_spinBox)

        self.winVal_slider = QSlider(curserWidget)
        self.winVal_slider.setObjectName(u"winVal_slider")
        self.winVal_slider.setMinimum(0)
        self.winVal_slider.setMaximum(2000)
        self.winVal_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.winVal_slider)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(curserWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.levVal_spinBox = QSpinBox(curserWidget)
        self.levVal_spinBox.setObjectName(u"levVal_spinBox")
        self.levVal_spinBox.setMaximum(2000)

        self.horizontalLayout_3.addWidget(self.levVal_spinBox)

        self.levVal_slider = QSlider(curserWidget)
        self.levVal_slider.setObjectName(u"levVal_slider")
        self.levVal_slider.setMinimum(0)
        self.levVal_slider.setMaximum(2000)
        self.levVal_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.levVal_slider)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(curserWidget)

        QMetaObject.connectSlotsByName(curserWidget)
    # setupUi

    def retranslateUi(self, curserWidget):
        curserWidget.setWindowTitle(QCoreApplication.translate("curserWidget", u"Form", None))
        self.curserPos_label.setText(QCoreApplication.translate("curserWidget", u"Curser Position (x,y,z)", None))
        self.curserX_label.setText(QCoreApplication.translate("curserWidget", u"#", None))
        self.curserY_label.setText(QCoreApplication.translate("curserWidget", u"#", None))
        self.curserZ_label.setText(QCoreApplication.translate("curserWidget", u"#", None))
        self.curserIntensity_label.setText(QCoreApplication.translate("curserWidget", u"Intensity (min,max,cur):", None))
        self.minIntensity_label.setText(QCoreApplication.translate("curserWidget", u"#", None))
        self.maxIntensity_label.setText(QCoreApplication.translate("curserWidget", u"#", None))
        self.curIntensity_label.setText(QCoreApplication.translate("curserWidget", u"#", None))
        self.label.setText(QCoreApplication.translate("curserWidget", u"Window Value", None))
        self.label_2.setText(QCoreApplication.translate("curserWidget", u"Level Value", None))
    # retranslateUi

