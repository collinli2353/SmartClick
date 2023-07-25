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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_cystLabel_widget(object):
    def setupUi(self, cystLabel_widget):
        if not cystLabel_widget.objectName():
            cystLabel_widget.setObjectName(u"cystLabel_widget")
        cystLabel_widget.resize(170, 363)
        self.verticalLayout_4 = QVBoxLayout(cystLabel_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.curser_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.curser_verticalSpacer)

        self.widget_title = QLabel(cystLabel_widget)
        self.widget_title.setObjectName(u"widget_title")
        self.widget_title.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_4.addWidget(self.widget_title)

        self.curser_verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.curser_verticalSpacer_4)

        self.lowerThresh_title = QLabel(cystLabel_widget)
        self.lowerThresh_title.setObjectName(u"lowerThresh_title")

        self.verticalLayout_4.addWidget(self.lowerThresh_title)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lowerThresh_spinBox = QSpinBox(cystLabel_widget)
        self.lowerThresh_spinBox.setObjectName(u"lowerThresh_spinBox")
        self.lowerThresh_spinBox.setMaximum(255)

        self.verticalLayout_2.addWidget(self.lowerThresh_spinBox)

        self.lowerThresh_slider = QSlider(cystLabel_widget)
        self.lowerThresh_slider.setObjectName(u"lowerThresh_slider")
        self.lowerThresh_slider.setMinimum(0)
        self.lowerThresh_slider.setMaximum(255)
        self.lowerThresh_slider.setSingleStep(1)
        self.lowerThresh_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.lowerThresh_slider)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.upperThresh_title = QLabel(cystLabel_widget)
        self.upperThresh_title.setObjectName(u"upperThresh_title")

        self.verticalLayout_4.addWidget(self.upperThresh_title)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperThresh_spinBox = QSpinBox(cystLabel_widget)
        self.upperThresh_spinBox.setObjectName(u"upperThresh_spinBox")
        self.upperThresh_spinBox.setMaximum(255)

        self.verticalLayout.addWidget(self.upperThresh_spinBox)

        self.upperThresh_slider = QSlider(cystLabel_widget)
        self.upperThresh_slider.setObjectName(u"upperThresh_slider")
        self.upperThresh_slider.setMinimum(0)
        self.upperThresh_slider.setMaximum(255)
        self.upperThresh_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.upperThresh_slider)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.curser_verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.curser_verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.curserIntensity_label_3 = QLabel(cystLabel_widget)
        self.curserIntensity_label_3.setObjectName(u"curserIntensity_label_3")
        self.curserIntensity_label_3.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_5.addWidget(self.curserIntensity_label_3)

        self.segActiveLabel_combobox_2 = QComboBox(cystLabel_widget)
        self.segActiveLabel_combobox_2.setObjectName(u"segActiveLabel_combobox_2")

        self.horizontalLayout_5.addWidget(self.segActiveLabel_combobox_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.curserIntensity_label_2 = QLabel(cystLabel_widget)
        self.curserIntensity_label_2.setObjectName(u"curserIntensity_label_2")
        self.curserIntensity_label_2.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_4.addWidget(self.curserIntensity_label_2)

        self.segActiveLabel_combobox = QComboBox(cystLabel_widget)
        self.segActiveLabel_combobox.setObjectName(u"segActiveLabel_combobox")

        self.horizontalLayout_4.addWidget(self.segActiveLabel_combobox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.curser_verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.curser_verticalSpacer_2)

        self.segment = QPushButton(cystLabel_widget)
        self.segment.setObjectName(u"segment")

        self.verticalLayout_4.addWidget(self.segment)


        self.retranslateUi(cystLabel_widget)

        QMetaObject.connectSlotsByName(cystLabel_widget)
    # setupUi

    def retranslateUi(self, cystLabel_widget):
        cystLabel_widget.setWindowTitle(QCoreApplication.translate("cystLabel_widget", u"Form", None))
        self.widget_title.setText(QCoreApplication.translate("cystLabel_widget", u"Hemmorhagic Cysts", None))
        self.lowerThresh_title.setText(QCoreApplication.translate("cystLabel_widget", u"Cyst Lower Threshold", None))
        self.upperThresh_title.setText(QCoreApplication.translate("cystLabel_widget", u"Cyst Upper Threshold", None))
        self.curserIntensity_label_3.setText(QCoreApplication.translate("cystLabel_widget", u"Left Kidney", None))
        self.curserIntensity_label_2.setText(QCoreApplication.translate("cystLabel_widget", u"Right Kidney", None))
        self.segment.setText(QCoreApplication.translate("cystLabel_widget", u"Segment", None))
    # retranslateUi

