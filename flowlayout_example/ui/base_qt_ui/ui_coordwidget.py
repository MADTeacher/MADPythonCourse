# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_coordwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import res_rc

class Ui_CoordWidget(object):
    def setupUi(self, CoordWidget):
        if not CoordWidget.objectName():
            CoordWidget.setObjectName(u"CoordWidget")
        CoordWidget.resize(739, 106)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CoordWidget.sizePolicy().hasHeightForWidth())
        CoordWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        CoordWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(CoordWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(CoordWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.horizontalLayout.addWidget(self.doubleSpinBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/icon/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(CoordWidget)

        QMetaObject.connectSlotsByName(CoordWidget)
    # setupUi

    def retranslateUi(self, CoordWidget):
        CoordWidget.setWindowTitle(QCoreApplication.translate("CoordWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("CoordWidget", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("CoordWidget", u"Lat", None))
        self.label_2.setText(QCoreApplication.translate("CoordWidget", u"Lon", None))
        self.pushButton.setText("")
    # retranslateUi

