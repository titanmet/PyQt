from PySide2.QtWidgets import *
from widget import newProjectUI as ui


class createProjectDialogClass(QDialog, ui.Ui_Dialog):
    def __init__(self, parent):
        super(createProjectDialogClass, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.doCreate)
        self.pushButton_2.clicked.connect(self.reject)

    def doCreate(self):
        if self.lineEdit.text():
            self.accept()

    def getDialogData(self):
        return dict(
            name=self.lineEdit.text(),
            comment=self.plainTextEdit.toPlainText()
        )
