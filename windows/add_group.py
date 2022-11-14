import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.AddGroup import Ui_Add_group


class AddGroup(QMainWindow, Ui_Add_group):
    def __init__(self):
        try:

            super().__init__()

            self.setupUi(self)
            self.pushButton.clicked.connect(self.to_add)

            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()

            self.bad_simbols = ['"', "'", '/', ';', ':', '&', '?', '!', '@', '#', '№', '$', '%', '^', '*', '(', ')',
                                '[',
                                ']', '{', '}', '>', '<', '`', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                                '=', '+', '-', '_']


        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def to_add(self):
        try:
            group = self.lineEdit.text().replace(' ', '').lower()
            not_error = True

            for i in group:
                if i in self.bad_simbols:
                    error = False

            if not_error:
                total = [group]

                self.cur.execute("INSERT INTO groups(name) VALUES(?);", total)
                self.conn.commit()

                self.lineEdit.setText('')
            else:
                QMessageBox.about(self, "Ошибка", "Неправильно заполнена анкета, введены запрещенные символы")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddGroup()
    ex.show()
    sys.exit(app.exec())