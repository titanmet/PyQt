# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'templateEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_templateEditor(object):
    def setupUi(self, templateEditor):
        if not templateEditor.objectName():
            templateEditor.setObjectName(u"templateEditor")
        templateEditor.resize(339, 432)
        self.verticalLayout = QVBoxLayout(templateEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(templateEditor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(templateEditor)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setBaseSize(QSize(30, 30))
        self.pushButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tree = QTreeWidget(templateEditor)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree.setHeaderItem(__qtreewidgetitem)
        self.tree.setObjectName(u"tree")
        self.tree.header().setVisible(False)

        self.verticalLayout.addWidget(self.tree)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(templateEditor)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(templateEditor)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(templateEditor)

        QMetaObject.connectSlotsByName(templateEditor)
    # setupUi

    def retranslateUi(self, templateEditor):
        templateEditor.setWindowTitle(QCoreApplication.translate("templateEditor", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("templateEditor", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("templateEditor", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("templateEditor", u"Save", None))
        self.pushButton_4.setText(QCoreApplication.translate("templateEditor", u"Close", None))
    # retranslateUi

