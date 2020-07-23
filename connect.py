from PySide2.QtWidgets import *
from PySide2.QtCore import *


class Connect(QWidget):
    def __init__(self):
        super(Connect, self).__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel('Напечатай текст')
        layout.addWidget(self.label)
        self.line = QLineEdit()
        layout.addWidget(self.line)
        self.button = QPushButton('Print')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.action_label)

        # button.clicked.connect(self.action)
        # line.textChanged.connect(self.text)
        # self.connect(button, SIGNAL('clicked()'), self, SLOT('action()'))  # deprecated

        # @button.clicked.connect  # decorator
        # def click():
        #     self.action()

    def action(self):
        print('ACTION')

    def text(self, arg):
        print(arg)

    def action_label(self):
        self.label.setText(self.line.text())


if __name__ == '__main__':
    app = QApplication([])
    window = Connect()
    window.show()
    app.exec_()
