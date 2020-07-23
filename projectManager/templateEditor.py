from PySide2.QtGui import *
from PySide2.QtWidgets import *
from widget import templateEditorUI as ui
import os, json

templateFile = os.path.join(os.path.dirname(__file__), 'template.json')


class templateEditorClass(QWidget, ui.Ui_templateEditor):
    def __init__(self):
        super(templateEditorClass, self).__init__()
        self.setupUi(self)
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.pushButton.clicked.connect(self.addItem)
        self.pushButton_2.clicked.connect(self.removeItem)
        self.pushButton_3.clicked.connect(self.saveTemplate)
        self.pushButton_4.clicked.connect(self.close)
        self.loadTemplate()

    def addItem(self, name='Folder', parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        item = QTreeWidgetItem()
        item.setFlags(
            Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled)
        item.setText(0, name)
        parent.addChild(item)
        item.setExpanded(1)
        return item

    def removeItem(self):
        items = self.tree.selectedItems()
        for i in items:
            (i.parent() or self.tree.invisibleRootItem()).takeChild(self.tree.indexFromItem(i).row())

    def saveTemplate(self):
        template = self.getStructure()
        with open(templateFile, 'w') as f:
            json.dump(template, f, indent=4)
        self.close()

    def getStructure(self, parent=None):
        level = []
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in range(parent.childCount()):
            ch = parent.child(i)
            content = self.getStructure(ch)
            level.append({'name': ch.text(0), 'content': content})
        return level

    def loadTemplate(self):
        if os.path.exists(templateFile):
            with open(templateFile) as f:
                template = json.load(f)
                self.restoreStructure(template)

    def restoreStructure(self, data, parent=None):
        if not parent:
            parent = self.tree.invisibleRootItem()
        for i in data:
            item = self.addItem(i['name'], parent)
            self.restoreStructure(i['content'], item)

