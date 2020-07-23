from PySide2.QtWidgets import *


class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel('Date:')
        layout.addWidget(label)
        button = QPushButton('OK')
        layout.addWidget(button)

app = QApplication([])
widget = myWidget()
widget.show()
app.exec_()
