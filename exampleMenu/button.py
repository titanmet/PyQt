from PySide2.QtCore import *
from PySide2.QtWidgets import *

textArray = 'Click', 'Press', 'Enter'


class myButtonClass(QPushButton):
    def __init__(self, text):
        super(myButtonClass, self).__init__(text)
        # self.btn.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.btn.customContextMenuRequested.connect(self.openMenu)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            super(myButtonClass, self).mousePressEvent(event)
        elif event.button() == Qt.MouseButton.RightButton:
            pos = event.globalPos()
            menu = QMenu()
            for i in textArray:
                menu.addAction(QAction(i, self))
            a = menu.exec_(pos)  # or menu.exec_(QCursor.pos)
            if a:
                self.setText(a.text())
        elif event.button() == Qt.MouseButton.MiddleButton:
            pass
