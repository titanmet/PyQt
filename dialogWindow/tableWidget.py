from PySide2.QtCore import *
from PySide2.QtWidgets import *
import os

path = os.path.dirname(__file__)


class tableWidgetClass(QWidget):
    def __init__(self):
        super(tableWidgetClass, self).__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().setStretchLastSection(True)
        # self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.resize(500, 300)
        self.fillTable()

    def fillTable(self):
        files = os.listdir(path)
        self.table.setColumnCount(2)
        self.table.setRowCount(len(files))
        self.table.setHorizontalHeaderLabels(['Name', 'Size'])
        for i, f in enumerate(files):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(f)
            self.table.setItem(i, 0, item)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setText(str(os.stat(os.path.join(path, f)).st_size) + ' bytes')
            self.table.setItem(i, 1, item)
        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication([])
    window = tableWidgetClass()
    window.show()
    app.exec_()
