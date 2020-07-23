# -*- coding: utf-8 -*-


from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(429, 355)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi

