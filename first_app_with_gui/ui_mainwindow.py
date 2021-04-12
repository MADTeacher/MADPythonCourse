# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 466)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.name_line_edit = QLineEdit(self.centralwidget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.verticalLayout.addWidget(self.name_line_edit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.otput_hello_label = QLabel(self.centralwidget)
        self.otput_hello_label.setObjectName(u"otput_hello_label")
        self.otput_hello_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.otput_hello_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 38))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0451 \u043f\u0435\u0440\u0432\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0441 GUI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u0442\u0435\u0431\u044f \u0437\u043e\u0432\u0443\u0442?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0422\u044b\u0446", None))
        self.otput_hello_label.setText("")
    # retranslateUi

