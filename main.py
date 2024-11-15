import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.roll.textChanged.connect(self.roll_counter)
        self.ui.rollCount.textChanged.connect(self.roll_counter)
        self.ui.nut.textChanged.connect(self.nut_counter)
        self.ui.nutWeight.textChanged.connect(self.nut_counter)
        self.show()

    def roll_counter(self):
        price = self.ui.roll.text()
        count = self.ui.rollCount.value()
        try:
            price = float(price)
            self.ui.rollTotal.setText(f'{price * count:.2f} zł')
        except ValueError:
            self.ui.roll.setText("")

    def nut_counter(self):
        price = self.ui.nut.text()
        count = self.ui.nutWeight.value()
        try:
            price = float(price)
            self.ui.nutTotal.setText(f'{price * count:.2f} zł')
        except ValueError:
            self.ui.roll.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())