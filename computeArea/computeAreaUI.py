# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 30, 281, 23))

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 64, 261, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 0))
        self.label_2.setBaseSize(QSize(100, 0))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(self.layoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setValue(10)

        self.horizontalLayout_2.addWidget(self.spinBox_2)

        self.horizontalLayout_2.setStretch(1, 1)
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 261, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(70, 0))
        self.label.setBaseSize(QSize(100, 0))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(999999999)
        self.spinBox.setValue(10)

        self.horizontalLayout.addWidget(self.spinBox)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.layoutWidget_2 = QWidget(self.groupBox_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 32, 261, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(70, 0))
        self.label_3.setBaseSize(QSize(100, 0))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_3 = QSpinBox(self.layoutWidget_2)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(999999999)
        self.spinBox_3.setValue(10)

        self.horizontalLayout_3.addWidget(self.spinBox_3)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Computer", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select shape", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Square", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Circle", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Square", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Circle", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"COMPUTE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Result", None))
    # retranslateUi

