from PySide2.QtWidgets import *

import settingsDialog, createProgectDialog, templateEditor, settings, createProject
from widget import projectManager_UI as ui
from widget import projectListWidget
import webbrowser


class projectManagerClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super(projectManagerClass, self).__init__()
        self.setupUi(self)
        self.projectList_lwd = projectListWidget.projectListClass()
        self.verticalLayout_4.addWidget(self.projectList_lwd)
        self.pushButton.clicked.connect(self.createProject)
        self.pushButton_2.clicked.connect(self.openTemplateEditorDialog)
        self.pushButton_3.clicked.connect(self.openSettingsDialog)
        self.projectList_lwd.itemClicked.connect(self.showInfo)
        self.projectList_lwd.itemDoubleClicked.connect(self.openProject)
        self.label.setText('')
        self.updateList()

    def updateList(self):
        if not self.projectList_lwd.updateProjectList():
            self.pushButton.setEnabled(0)
        else:
            self.pushButton.setEnabled(1)

    def openSettingsDialog(self):
        self.dial = settingsDialog.settingsDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getTableData()
            settings.settingsClass().save(data)
        self.updateList()

    def openTemplateEditorDialog(self):
        self.dial = templateEditor.templateEditorClass()
        self.dial.show()

    def createProject(self):
        self.dial = createProgectDialog.createProjectDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getDialogData()
            createProject.createProject(data)
            self.updateList()

    def showInfo(self, item):
        info = createProject.getProjectInfo(item.data(32))
        if info:
            text = '''Name:
%s

Comment:
%s''' % (info['name'], info['comment'])
        else:
            text = ''
        self.label.setText(text)

    def openProject(self, item):
        path = item.data(32)
        webbrowser.open(path)


if __name__ == '__main__':
    app = QApplication([])
    window = projectManagerClass()
    window.show()
    app.exec_()
