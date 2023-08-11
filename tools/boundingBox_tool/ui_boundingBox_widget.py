# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boundingBox_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_boundingBox_widget(object):
    def setupUi(self, boundingBox_widget):
        if not boundingBox_widget.objectName():
            boundingBox_widget.setObjectName(u"boundingBox_widget")
        boundingBox_widget.resize(208, 198)
        self.verticalLayout = QVBoxLayout(boundingBox_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.curser_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer)

        self.widget_title = QLabel(boundingBox_widget)
        self.widget_title.setObjectName(u"widget_title")
        self.widget_title.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.widget_title)

        self.curser_verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_4)

        self.curser_verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rightKidney_label = QLabel(boundingBox_widget)
        self.rightKidney_label.setObjectName(u"rightKidney_label")
        self.rightKidney_label.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_4.addWidget(self.rightKidney_label)

        self.rightKidney_spinBox = QSpinBox(boundingBox_widget)
        self.rightKidney_spinBox.setObjectName(u"rightKidney_spinBox")
        self.rightKidney_spinBox.setMaximum(5000)
        self.rightKidney_spinBox.setValue(1)

        self.horizontalLayout_4.addWidget(self.rightKidney_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.curser_verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.curser_verticalSpacer_2)


        self.retranslateUi(boundingBox_widget)

        QMetaObject.connectSlotsByName(boundingBox_widget)
    # setupUi

    def retranslateUi(self, boundingBox_widget):
        boundingBox_widget.setWindowTitle(QCoreApplication.translate("boundingBox_widget", u"Form", None))
        self.widget_title.setText(QCoreApplication.translate("boundingBox_widget", u"Bounding Box", None))
        self.rightKidney_label.setText(QCoreApplication.translate("boundingBox_widget", u"Semantic Cyst Label", None))
    # retranslateUi

