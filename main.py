# подключение библиотек
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.HomeWindow import Ui_Login
from windows import sign


class Window(QMainWindow, Ui_Login):
    def __init__(self):
        try:
            super().__init__()

            self.setupUi(self)
            self.enter_to_account.clicked.connect(self.sign_in)

        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def sign_in(self):
        try:
            self.open = sign.Sign()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
