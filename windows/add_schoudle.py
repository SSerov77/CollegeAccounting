import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.AddSchedule import Ui_Add_schedule


class AddSchedule(QMainWindow, Ui_Add_schedule):
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
            teacher = self.lineEdit.text()
            monday = self.lineEdit_2.text()
            tuesday = self.lineEdit_3.text()
            wednesday = self.lineEdit_4.text()
            thursday = self.lineEdit_5.text()
            friday = self.lineEdit_6.text()
            saturday = self.lineEdit_7.text()
            sunday = self.lineEdit_8.text()

            not_error = True

            result = teacher + monday + tuesday + wednesday + thursday + friday + sunday + saturday

            for i in result:
                if i in self.bad_simbols:
                    error = False

            if not_error:

                total = [teacher, monday, tuesday, wednesday, thursday, friday, saturday, sunday]
                print(total)
                self.cur.execute(
                    "INSERT INTO schedule(teacher, monday, tuesday, wednesday, thursday, friday, saturday, sunday) VALUES(?, ?, ?, ?, ?, ?, ?, ?);",
                    total)
                print(1)
                self.conn.commit()

                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_6.setText('')
                self.lineEdit_7.setText('')
                self.lineEdit_8.setText('')
            else:
                QMessageBox.about(self, "Ошибка", "Неправильно заполнена анкета, введены запрещенные символы")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddSchedule()
    ex.show()
    sys.exit(app.exec())
