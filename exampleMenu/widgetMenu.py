from PySide2.QtCore import *
from PySide2.QtWidgets import *
import button

textArray = 'Click', 'Press', 'Enter'


class widgetMenuClass(QWidget):
    def __init__(self):
        super(widgetMenuClass, self).__init__()
        layout = QVBoxLayout(self)
        # self.btn = QPushButton('Click')
        self.btn = button.myButtonClass('Click')
        layout.addWidget(self.btn)
        self.line = QLineEdit()
        layout.addWidget(self.line)

        # right click button context menu
        self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        self.btn.customContextMenuRequested.connect(self.openMenu)

        self.line.setContextMenuPolicy(Qt.CustomContextMenu)
        self.line.customContextMenuRequested.connect(self.openMenu)

    def openMenu(self, pos):
        pos = self.sender().mapToGlobal(pos)
        try:
            menu = self.sender().createStandardContextMenu()
        except:
            menu = QMenu()
        for i in textArray:
            menu.addAction(QAction(i, self))
        a = menu.exec_(pos)  # or menu.exec_(QCursor.pos)
        if a:
            self.sender().setText(a.text())

    def openMenu2(self, pos):
        pos = self.line.mapToGlobal(pos)
        menu = self.line.createStandardContextMenu()
        menu.addSeparator()
        for i in textArray:
            menu.addAction(QAction(i, self))
        a = menu.exec_(pos)  # or menu.exec_(QCursor.pos)
        if a:
            self.line.setText(a.text())


if __name__ == '__main__':
    app = QApplication([])
    window = widgetMenuClass()
    window.show()
    app.exec_()
