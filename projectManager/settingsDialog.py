from PySide2.QtWidgets import *
from widget import settingsDialogUI as ui
import settings

class settingsDialogClass(QDialog, ui.Ui_Dialog):
    def __init__(self, parent):
        super(settingsDialogClass, self).__init__(parent)
        self.setupUi(self)
        self.tableView.setColumnCount(2)
        self.fiilTable()

    def fiilTable(self):
        data = settings.settingsClass().load()
        for key, value in data.items():
            self.addParm(key, value)

    def addParm(self, parm, value):
        self.tableView.insertRow(self.tableView.rowCount())
        item = QTableWidgetItem()
        item.setText(parm)
        self.tableView.setItem(self.tableView.rowCount()-1, 0, item)

        item = QTableWidgetItem()
        item.setText(value)
        self.tableView.setItem(self.tableView.rowCount()-1, 1, item)

    def getTableData(self):
        data = dict()
        for i in range(self.tableView.rowCount()):
            parm = self.tableView.item(i, 0).text()
            value = self.tableView.item(i, 1).text()
            data[parm] = value
        return data
