# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_imageConverter(object):
    def setupUi(self, imageConverter):
        if not imageConverter.objectName():
            imageConverter.setObjectName(u"imageConverter")
        imageConverter.resize(363, 387)
        self.centralwidget = QWidget(imageConverter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.iconvert_lb = QLabel(self.centralwidget)
        self.iconvert_lb.setObjectName(u"iconvert_lb")

        self.horizontalLayout.addWidget(self.iconvert_lb)

        self.path_btn = QPushButton(self.centralwidget)
        self.path_btn.setObjectName(u"path_btn")
        self.path_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.path_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.files_layout = QVBoxLayout()
        self.files_layout.setObjectName(u"files_layout")

        self.verticalLayout.addLayout(self.files_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.out_line_edit = QLineEdit(self.centralwidget)
        self.out_line_edit.setObjectName(u"out_line_edit")

        self.horizontalLayout_2.addWidget(self.out_line_edit)

        self.out_btn = QPushButton(self.centralwidget)
        self.out_btn.setObjectName(u"out_btn")
        self.out_btn.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.out_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout.addWidget(self.start_btn)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.verticalLayout.setStretch(1, 1)
        imageConverter.setCentralWidget(self.centralwidget)

        self.retranslateUi(imageConverter)

        QMetaObject.connectSlotsByName(imageConverter)
    # setupUi

    def retranslateUi(self, imageConverter):
        imageConverter.setWindowTitle(QCoreApplication.translate("imageConverter", u"MainWindow", None))
        self.iconvert_lb.setText(QCoreApplication.translate("imageConverter", u"Path", None))
        self.path_btn.setText(QCoreApplication.translate("imageConverter", u"..", None))
        self.out_btn.setText(QCoreApplication.translate("imageConverter", u"...", None))
        self.start_btn.setText(QCoreApplication.translate("imageConverter", u"Start", None))
    # retranslateUi

