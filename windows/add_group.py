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

        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    def to_add(self):
        group = self.lineEdit.text().replace(' ', '').lower()
        total = [group]

        self.cur.execute("INSERT INTO groups(name) VALUES(?);", total)
        self.conn.commit()

        self.lineEdit.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddGroup()
    ex.show()
    sys.exit(app.exec())