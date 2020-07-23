from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

path = os.path.dirname(os.path.dirname(__file__))


class treeWidgetClass(QWidget):
    def __init__(self):
        super(treeWidgetClass, self).__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.tree = QTreeWidget()
        layout.addWidget(self.tree)
        self.tree.header().hide()
        self.tree.itemChanged.connect(self.action)
        self.resize(500, 400)
        self.updateTree()

    # def fillTree(self):
    # item = QTreeWidgetItem()
    # item.setText(0, 'Item1')
    # self.tree.addTopLevelItem(item)
    #
    # item = QTreeWidgetItem()
    # item.setText(0, 'Item2')
    # self.tree.invisibleRootItem().addChild(item)

    def updateTree(self):
        self.tree.blockSignals(True)
        self.fillTree()
        self.tree.blockSignals(False)

    def fillTree(self, parent=None, root=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        if not root:
            root = path
        for f in os.listdir(root):
            if f[0] in ['.', '_']: continue
            item = QTreeWidgetItem()
            item.setText(0, f)
            parent.addChild(item)
            fullpath = os.path.join(root, f)
            if os.path.isdir(fullpath):
                self.fillTree(item, fullpath)
                item.setExpanded(1)
            else:
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                item.setData(0, Qt.UserRole, os.path.normpath(fullpath))

    def action(self, item):
        print(item.text(0))
        print(item.data(0, Qt.UserRole))


if __name__ == '__main__':
    app = QApplication([])
    window = treeWidgetClass()
    window.show()
    app.exec_()
