import math

from PySide2.QtWidgets import *

from calculatorNUM import calculatorUI


class calculatorClass(QMainWindow, calculatorUI.Ui_MainWindow):
    def __init__(self):
        super(calculatorClass, self).__init__()
        self.setupUi(self)
        self.lineEdit.setText('0')
        self.first_value = None
        self.second_value = None
        self.result = None
        self.example = ""
        self.equal = ""
        self.pushButton.clicked.connect(self.num_press)
        self.pushButton_2.clicked.connect(self.num_press)
        self.pushButton_3.clicked.connect(self.num_press)
        self.pushButton_4.clicked.connect(self.num_press)
        self.pushButton_5.clicked.connect(self.num_press)
        self.pushButton_6.clicked.connect(self.num_press)
        self.pushButton_7.clicked.connect(self.num_press)
        self.pushButton_8.clicked.connect(self.num_press)
        self.pushButton_9.clicked.connect(self.num_press)
        self.pushButton_12.clicked.connect(self.num_press)
        self.pushButton_13.clicked.connect(self.equal_press)
        self.pushButton_14.clicked.connect(self.equal_press)
        self.pushButton_15.clicked.connect(self.equal_press)
        self.pushButton_16.clicked.connect(self.equal_press)
        self.pushButton_17.clicked.connect(self.equal_press)
        self.pushButton_19.clicked.connect(self.equal_press)
        self.pushButton_20.clicked.connect(self.function_clear)
        self.pushButton_23.clicked.connect(self.function_result)
        self.pushButton_22.clicked.connect(self.delete)
        self.pushButton_11.clicked.connect(self.fractional)
        self.pushButton_17.clicked.connect(self.log)
        self.pushButton_15.clicked.connect(self.subtraction)
        self.pushButton_14.clicked.connect(self.multiply)
        self.pushButton_16.clicked.connect(self.divison)
        self.pushButton_10.clicked.connect(self.percent)
        self.pushButton_19.clicked.connect(self.exponentiation)


    def num_press(self):
        button = self.sender()
        if self.lineEdit.text() == '0':
            self.lineEdit.setText(button.text())
        else:
            if self.result == self.lineEdit.text():
                self.lineEdit.setText(button.text)
            else:
                self.lineEdit.setText(self.lineEdit.text() + button.text())
        self.result = 0

    def subtraction(self):
        self.determinate_second_value()
        self.result = float(self.first_value - self.second_value)
        self.form_result()

    def divison(self):
        self.determinate_second_value()
        self.result = float(self.first_value / self.second_value)
        self.form_result()

    def multiply(self):
        self.determinate_second_value()
        self.result = float(self.first_value * self.second_value)
        self.form_result()

    def exponentiation(self):
        self.determinate_second_value()
        self.result = float(self.first_value ** self.second_value)
        self.form_result()

    def percent(self):
        self.determinate_second_value()
        self.result = float(self.first_value * (self.second_value / 100))
        self.form_result()

    def log(self):
        self.determinate_second_value()
        self.result = float(math.log(self.first_value, self.second_value))
        self.form_result()

    def fractional(self):
        value = self.lineEdit.text()
        if '.' not in value:
            self.lineEdit.setText(value + '.')

    def equal_press(self):
        button = self.sender()
        self.first_value = float(self.lineEdit.text())
        self.lineEdit.clear()
        self.label.setText(str(self.first_value) + button.text())
        self.equal = button.text()

    def delete(self):
        value = self.lineEdit.text()
        self.lineEdit.setText(value[:-1])

    def form_result(self):
        self.result = str(self.result)
        if self.result[-2:] == '.0':
            self.result = self.result[:-2]
        self.lineEdit.setText(str(self.result))
        self.label.clear()

    def function_result(self):
        if self.equal == '+':
            self.addition()
        elif self.equal == '-':
            self.subtraction()
        elif self.equal == "/":
            self.divison()
        elif self.equal == '*':
            self.multiply()
        elif self.equal == "^":
            self.exponentiation()
        elif self.equal == "%":
            self.function_percent()
        elif self.equal == "log":
            self.function_log()

    def function_clear(self):
        self.lineEdit.setText('0')

    def addition(self):
        self.determinate_second_value()
        self.result = float(self.first_value + self.second_value)
        self.form_result()

    def determinate_second_value(self):
        self.second_value = float(self.lineEdit.text())
        self.lineEdit.clear()
        self.label.setText(str(self.first_value) + self.equal + str(self.second_value))


if __name__ == '__main__':
    app = QApplication([])
    window = calculatorClass()
    window.show()
    app.exec_()
