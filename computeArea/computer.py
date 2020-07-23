from PySide2.QtWidgets import *
from computeArea import computeAreaUI
import math


class computeAreaClass(QMainWindow, computeAreaUI.Ui_MainWindow):
    def __init__(self):
        super(computeAreaClass, self).__init__()
        self.setupUi(self)
        self.live = False
        self.comboBox.currentIndexChanged.connect(self.updateUI)
        self.pushButton.clicked.connect(self.compute)
        if self.live:
            self.pushButton.setVisible(0)
            self.spinBox.valueChanged.connect(self.compute)
            self.spinBox_2.valueChanged.connect(self.compute)
            self.spinBox_3.valueChanged.connect(self.compute)
        self.updateUI()

    def compute(self):
        if self.comboBox.currentIndex() == 0:
            self.computeSquare()
        elif self.comboBox.currentIndex() == 1:
            self.computeCircle()

    def computeSquare(self):
        w = self.spinBox.value()
        h = self.spinBox_2.value()
        area = w * h
        self.showArea(area)

    def computeCircle(self):
        r = self.spinBox_3.value()
        area = math.pi * (r ** 2)
        self.showArea(area)

    def showArea(self, result):
        self.label_4.setText('result: %.3f' % result)

    def updateUI(self):
        self.groupBox_2.setVisible(self.comboBox.currentIndex() == 0)
        self.groupBox_3.setVisible(self.comboBox.currentIndex() == 1)
        self.compute()


if __name__ == '__main__':
    app = QApplication([])
    window = computeAreaClass()
    window.show()
    app.exec_()
