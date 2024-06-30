import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import random

from UI import Ui_MainWindow

class Generator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submitButton.clicked.connect(self.generate_random_number)

    def generate_random_number(self):
        try:
            lowerBound = int(self.lowerBound.text())
            upperBound = int(self.upperBound.text())

            if upperBound <= lowerBound:
                raise ValueError("Upper bound must be greater than lower bound")

            random_number = random.randint(lowerBound, upperBound)

            text = f"Random Number: {random_number}"

            self.outputField.setText(text)

        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Input Error", str(e))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Generator()
    window.show()
    sys.exit(app.exec_())