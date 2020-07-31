from PySide2.QtWidgets import *
from PySide2.QtCore import *
from widgets import imageConverter_UI as ui
from widgets import fileWidget
import converter


class imageConverterWindowClass(QMainWindow, ui.Ui_imageConverter):
    def __init__(self):
        super(imageConverterWindowClass, self).__init__()
        self.setupUi(self)
        self.list = fileWidget.fileWidgetClass()
        self.files_layout.addWidget(self.list)
        self.start_btn.clicked.connect(self.start)

    def start(self):
        files = self.list.getAllFiles()
        if files:
            out = self.out_line_edit.text()
            inc = 100 / len(files)
            for f in files:
                converter.convert(f, out)
                self.progressBar.setValue(self.progressBar.value() + inc)
        self.progressBar.setValue(0)


if __name__ == '__main__':
    app = QApplication([])
    window = imageConverterWindowClass()
    window.show()
    app.exec_()
