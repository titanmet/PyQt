from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import os

icon = os.path.join(os.path.dirname(__file__), 'drag.png')


class dndWidgetClass(QListWidget):
    def __init__(self):
        super(dndWidgetClass, self).__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files = []

    def dropEvent(self, event):
        mimedata = event.mimeData()
        if mimedata.hasUrls():
            for f in mimedata.urls():
                self.addFile(f.toLocalFile())

    def dragEnterEvent(self, event):
        if event.source() is self:
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def dragMoveEvent(self, event):
        if event.source() is self:
            event.ignore()
        else:
            mimedata = event.mimeData()
            if mimedata.hasUrls():
                event.accept()
            else:
                event.ignore()

    def startDrag(self, dropAction):
        drag = QDrag(self)
        mimedata = QMimeData()
        url = []
        for i in self.selectedItems():
            url.append(i.data(Qt.UserRole))
        mimedata.setUrls([QUrl.fromLocalFile(x) for x in url])
        drag.setMimeData(mimedata)
        pix = QPixmap(icon)
        drag.setPixmap(pix)
        result = drag.exec_()
        if result == Qt.DropAction.MoveAction:
            self.deleteSelected()

    def deleteSelected(self):
        for s in self.selectedItems():
            self.files.remove(s.data(32))
            self.takeItem(self.indexFromItem(s).row())

    def addFile(self, path):
        if not path in self.files:
            item = QListWidgetItem(self)
            item.setText(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.files.append(path)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            pass
        elif event.button() == Qt.MouseButton.LeftButton:
            self.setDragDropMode(QAbstractItemView.NoDragDrop)
            super(dndWidgetClass, self).mousePressEvent(event)
        else:
            self.setDragDropMode(QAbstractItemView.DragDrop)
            super(dndWidgetClass, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setDragDropMode(QAbstractItemView.DragDrop)
        super(dndWidgetClass, self).mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    window = dndWidgetClass()
    window.show()
    app.exec_()
