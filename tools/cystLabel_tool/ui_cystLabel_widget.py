# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cystLabel_widget.ui'
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
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_cystLabel_widget(object):
    def setupUi(self, cystLabel_widget):
        if not cystLabel_widget.objectName():
            cystLabel_widget.setObjectName(u"cystLabel_widget")
        cystLabel_widget.resize(182, 454)
        self.verticalLayout = QVBoxLayout(cystLabel_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.curser_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer)

        self.widget_title = QLabel(cystLabel_widget)
        self.widget_title.setObjectName(u"widget_title")
        self.widget_title.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.widget_title)

        self.curser_verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_4)

        self.curserPos_label = QLabel(cystLabel_widget)
        self.curserPos_label.setObjectName(u"curserPos_label")
        self.curserPos_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.curserPos_label)

        self.cursorPos_frame = QFrame(cystLabel_widget)
        self.cursorPos_frame.setObjectName(u"cursorPos_frame")
        self.cursorPos_frame.setMaximumSize(QSize(16777215, 35))
        self.cursorPos_frame.setFrameShape(QFrame.StyledPanel)
        self.cursorPos_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.cursorPos_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.curserX_label = QLabel(self.cursorPos_frame)
        self.curserX_label.setObjectName(u"curserX_label")

        self.horizontalLayout_3.addWidget(self.curserX_label)

        self.curserY_label = QLabel(self.cursorPos_frame)
        self.curserY_label.setObjectName(u"curserY_label")

        self.horizontalLayout_3.addWidget(self.curserY_label)

        self.curserZ_label = QLabel(self.cursorPos_frame)
        self.curserZ_label.setObjectName(u"curserZ_label")

        self.horizontalLayout_3.addWidget(self.curserZ_label)


        self.verticalLayout.addWidget(self.cursorPos_frame)

        self.curserIntensity_label = QLabel(cystLabel_widget)
        self.curserIntensity_label.setObjectName(u"curserIntensity_label")
        self.curserIntensity_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.curserIntensity_label)

        self.curserIntensity_frame = QFrame(cystLabel_widget)
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

        self.curser_verticalSpacer_5 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_5)

        self.lowerThresh_title = QLabel(cystLabel_widget)
        self.lowerThresh_title.setObjectName(u"lowerThresh_title")

        self.verticalLayout.addWidget(self.lowerThresh_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lowerThresh_spinBox = QSpinBox(cystLabel_widget)
        self.lowerThresh_spinBox.setObjectName(u"lowerThresh_spinBox")
        self.lowerThresh_spinBox.setMaximum(5000)

        self.horizontalLayout.addWidget(self.lowerThresh_spinBox)

        self.lowerThresh_slider = QSlider(cystLabel_widget)
        self.lowerThresh_slider.setObjectName(u"lowerThresh_slider")
        self.lowerThresh_slider.setMinimum(0)
        self.lowerThresh_slider.setMaximum(5000)
        self.lowerThresh_slider.setSingleStep(1)
        self.lowerThresh_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.lowerThresh_slider)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.upperThresh_title = QLabel(cystLabel_widget)
        self.upperThresh_title.setObjectName(u"upperThresh_title")

        self.verticalLayout.addWidget(self.upperThresh_title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.upperThresh_spinBox = QSpinBox(cystLabel_widget)
        self.upperThresh_spinBox.setObjectName(u"upperThresh_spinBox")
        self.upperThresh_spinBox.setMaximum(5000)
        self.upperThresh_spinBox.setValue(5000)

        self.horizontalLayout_2.addWidget(self.upperThresh_spinBox)

        self.upperThresh_slider = QSlider(cystLabel_widget)
        self.upperThresh_slider.setObjectName(u"upperThresh_slider")
        self.upperThresh_slider.setMinimum(0)
        self.upperThresh_slider.setMaximum(5000)
        self.upperThresh_slider.setValue(5000)
        self.upperThresh_slider.setSliderPosition(5000)
        self.upperThresh_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.upperThresh_slider)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.curser_verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.leftKidney_Label = QLabel(cystLabel_widget)
        self.leftKidney_Label.setObjectName(u"leftKidney_Label")
        self.leftKidney_Label.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_5.addWidget(self.leftKidney_Label)

        self.leftKidney_spinBox = QSpinBox(cystLabel_widget)
        self.leftKidney_spinBox.setObjectName(u"leftKidney_spinBox")
        self.leftKidney_spinBox.setMaximum(5000)
        self.leftKidney_spinBox.setValue(2)

        self.horizontalLayout_5.addWidget(self.leftKidney_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rightKidney_label = QLabel(cystLabel_widget)
        self.rightKidney_label.setObjectName(u"rightKidney_label")
        self.rightKidney_label.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_4.addWidget(self.rightKidney_label)

        self.rightKidney_spinBox = QSpinBox(cystLabel_widget)
        self.rightKidney_spinBox.setObjectName(u"rightKidney_spinBox")
        self.rightKidney_spinBox.setMaximum(5000)
        self.rightKidney_spinBox.setValue(1)

        self.horizontalLayout_4.addWidget(self.rightKidney_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.curser_verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.toggle = QPushButton(cystLabel_widget)
        self.toggle.setObjectName(u"toggle")

        self.horizontalLayout_6.addWidget(self.toggle)

        self.segment = QPushButton(cystLabel_widget)
        self.segment.setObjectName(u"segment")

        self.horizontalLayout_6.addWidget(self.segment)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(cystLabel_widget)

        QMetaObject.connectSlotsByName(cystLabel_widget)
    # setupUi

    def retranslateUi(self, cystLabel_widget):
        cystLabel_widget.setWindowTitle(QCoreApplication.translate("cystLabel_widget", u"Form", None))
        self.widget_title.setText(QCoreApplication.translate("cystLabel_widget", u"Hemmorhagic Cysts", None))
        self.curserPos_label.setText(QCoreApplication.translate("cystLabel_widget", u"Curser Position (x,y,z)", None))
        self.curserX_label.setText(QCoreApplication.translate("cystLabel_widget", u"#", None))
        self.curserY_label.setText(QCoreApplication.translate("cystLabel_widget", u"#", None))
        self.curserZ_label.setText(QCoreApplication.translate("cystLabel_widget", u"#", None))
        self.curserIntensity_label.setText(QCoreApplication.translate("cystLabel_widget", u"Intensity (min,max,cur):", None))
        self.minIntensity_label.setText(QCoreApplication.translate("cystLabel_widget", u"#", None))
        self.maxIntensity_label.setText(QCoreApplication.translate("cystLabel_widget", u"#", None))
        self.curIntensity_label.setText(QCoreApplication.translate("cystLabel_widget", u"#", None))
        self.lowerThresh_title.setText(QCoreApplication.translate("cystLabel_widget", u"Cyst Lower Threshold", None))
        self.upperThresh_title.setText(QCoreApplication.translate("cystLabel_widget", u"Cyst Upper Threshold", None))
        self.leftKidney_Label.setText(QCoreApplication.translate("cystLabel_widget", u"Left Kidney", None))
        self.rightKidney_label.setText(QCoreApplication.translate("cystLabel_widget", u"Right Kidney", None))
        self.toggle.setText(QCoreApplication.translate("cystLabel_widget", u"Toggle", None))
        self.segment.setText(QCoreApplication.translate("cystLabel_widget", u"Segment", None))
    # retranslateUi

