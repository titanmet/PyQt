from PySide2.QtWidgets import *


class dialogClass(QDialog):
    def __init__(self):
        super(dialogClass, self).__init__()
        self.layout = QVBoxLayout(self)
        self.line = QLineEdit()
        self.layout.addWidget(self.line)

        self.ok_btn = QPushButton('OK')
        self.layout.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton('Cancel')
        self.layout.addWidget(self.cancel_btn)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

    def getData(self):
        return dict(text=self.line.text())
