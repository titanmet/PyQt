from PySide2.QtWidgets import *


class windowClass(QMainWindow):
    def __init__(self):
        super(windowClass, self).__init__()
        self.button = QPushButton('OK')
        self.setCentralWidget(self.button)
        self.menuBar = QMenuBar()
        self.setMenuBar(self.menuBar)
        self.menu = QMenu('File')
        self.menuBar.addMenu(self.menu)
        self.act1 = QAction('Open', self)
        self.menu.addAction(self.act1)


if __name__ == '__main__':
    app = QApplication([])
    window = windowClass()
    window.show()
    app.exec_()
