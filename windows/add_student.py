import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_py_files.AddStudent import Ui_Add_student


class AddStudent(QMainWindow, Ui_Add_student):
    def __init__(self):
        try:

            super().__init__()

            self.setupUi(self)

            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()
            self.pushButton.clicked.connect(self.to_add)

            self.bad_simbols = ['"', "'", '/', ';', ':', '&', '?', '!', '@', '#', '№', '$', '%', '^', '*', '(', ')',
                                '[',
                                ']', '{', '}', '>', '<', '`', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                                '=', '+', '-', '_']

        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    def to_add(self):
        try:
            student = self.lineEdit.text()
            group = self.lineEdit_2.text()
            teacher = self.lineEdit_3.text()
            not_error = True

            for i in student:
                if i in self.bad_simbols:
                    not_error = False
            for i in group:
                if i in self.bad_simbols:
                    not_error = False
            for i in teacher:
                if i in self.bad_simbols:
                    not_error = False

            if not_error:
                total = [student, group, teacher]
                self.cur.execute("INSERT INTO students(name, groups, teacher) VALUES(?, ?, ?);", total)
                self.conn.commit()

                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
            else:
                QMessageBox.about(self, "Ошибка", "Неправильно заполнена анкета, введены запрещенные символы")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddStudent()
    ex.show()
    sys.exit(app.exec())
