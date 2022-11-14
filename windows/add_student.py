import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_py_files.AddStudent import Ui_Add_student


class AddStudent(QMainWindow, Ui_Add_student):
    def __init__(self):
            super().__init__()

            self.setupUi(self)

            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()
            self.pushButton.clicked.connect(self.to_add)

    def to_add(self):
        student = self.lineEdit.text()
        group = self.lineEdit_2.text()
        teacher = self.lineEdit_3.text()

        total = [student, group, teacher]

        self.cur.execute("INSERT INTO students(name, groups, teacher) VALUES(?, ?, ?);", total)

        self.conn.commit()

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddStudent()
    ex.show()
    sys.exit(app.exec())
