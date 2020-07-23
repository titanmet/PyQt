from PySide2.QtWidgets import *
from exampleWindow import window_UIs


class exampleWindowClass(QWidget, window_UIs.Ui_Form):
    def __init__(self):
        super(exampleWindowClass, self).__init__()
        self.count = 1
        self.setupUi(self)
        self.setWindowTitle('Item list')
        self.pushButton.clicked.connect(self.addItem)
        self.lineEdit.returnPressed.connect(self.addItem)

    def addItem(self):
        text = self.lineEdit.text()
        if text:
            lb = QLabel('%s: %s' % (self.count, text))
            self.verticalLayout.addWidget(lb)
            self.count += 1


if __name__ == '__main__':
    app = QApplication([])
    window = exampleWindowClass()
    window.show()
    app.exec_()
