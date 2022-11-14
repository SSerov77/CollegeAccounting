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

        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    def to_add(self):
        teacher = self.lineEdit.text()
        monday = self.lineEdit_2.text()
        tuesday = self.lineEdit_3.text()
        wednesday = self.lineEdit_4.text()
        thursday = self.lineEdit_5.text()
        friday = self.lineEdit_6.text()
        saturday = self.lineEdit_7.text()
        sunday = self.lineEdit_8.text()

        total = [teacher, monday, tuesday, wednesday, thursday, friday, saturday, sunday]

        self.cur.execute(
            "INSERT INTO schedule(teacher, monday, tuesday, wednesday, thursday, friday, saturday, sunday) VALUES(?, ?, ?, ?, ?, ?, ?, ?);",
            total)
        self.conn.commit()

        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddSchedule()
    ex.show()
    sys.exit(app.exec())
