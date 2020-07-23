from PySide2.QtWidgets import *
from dialogWindow import dialog

class dialogWindowClass(QWidget):
    def __init__(self):
        super(dialogWindowClass, self).__init__()
        layout = QVBoxLayout(self)
        self.btn = QPushButton('Open')
        layout.addWidget(self.btn)
        self.resize(300, 200)
        self.btn.clicked.connect(self.showMessage4)

    def showMessage(self):
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setDetailedText("Detailed Text")
        ret = msgBox.exec_()
        print(ret == QMessageBox.save)

    def showMessage2(self):
        i = QInputDialog().getText(self, 'Enter name', 'Name:')
        print(i)

    def showMessage3(self):
        _filter = 'Python file(*.py);; All file(*.*);; *.txt *.doc'
        # df = QFileDialog.getExistingDirectory(self, 'Set folder', '/home/')
        df = QFileDialog.getOpenFileName(self, 'Open File', '/home/', _filter)
        print(df)

    def showMessage4(self):
        self.dial = dialog.dialogClass()
        r = self.dial.exec_()
        if r:
            print(self.dial.getData())

if __name__ == '__main__':
    app = QApplication([])
    window = dialogWindowClass()
    window.show()
    app.exec_()
