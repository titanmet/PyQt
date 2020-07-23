from PySide2.QtWidgets import *
import os

path = os.path.dirname(__file__)


class listWidgetClass(QWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.list = QListWidget()
        layout.addWidget(self.list)
        self.textBrowser = QTextBrowser()
        layout.addWidget(self.textBrowser)
        self.list.itemClicked.connect(self.updateText)
        self.list.itemDoubleClicked.connect(self.openFile)
        self.resize(500, 300)
        self.fillList()

    def fillList(self):
        # self.list.addItem('ITEM')
        for f in os.listdir(path):
            self.list.addItem(f)

    def fullPath(self, item):
        return os.path.join(path, item.text())

    def updateText(self, item):
        text = open(self.fullPath(item)).read()
        self.textBrowser.setText(text)

    def openFile(self, item):
        path = self.fullPath(item)
        os.system(path)


if __name__ == '__main__':
    app = QApplication([])
    window = listWidgetClass()
    window.show()
    app.exec_()
