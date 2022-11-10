import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.AdminWindow import Ui_Admin


class Admin(QMainWindow, Ui_Admin):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)

            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()

            self.pushButton.clicked.connect(self.registration)

        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    def registration(self):
        logins = []
        errors = True
        first_name = self.lineEdit_firstname.text().replace(" ", "").capitalize()
        last_name = self.lineEdit_lastname.text().replace(" ", "").capitalize()
        third_name = self.lineEdit_thirdname.text().replace(" ", "").capitalize()
        login = self.lineEdit_login.text().replace(" ", "")
        password = self.lineEdit_password.text()
        password2 = self.lineEdit_password2.text()

        result = self.cur.execute("SELECT login FROM teachers").fetchall()
        for i in result:
            logins.append(i[0])

        if first_name == '' or last_name == '' or third_name == '' or login == '' or password == '' or password2 == '':
            QMessageBox.about(self, "Ошибка", "Вы заполнили не все поля")
        elif (login in logins) or login == 'admin':
            QMessageBox.about(self, "Ошибка", "Такой логин уже существует")
        elif password2 != password:
            QMessageBox.about(self, "Ошибка", "Пароли не совпадают")
        else:
            errors = False

        if errors is False:
            name = f"{last_name} {first_name} {third_name}"
            total = (name, login, password)
            self.cur.execute("INSERT INTO teachers(name, login, password)"
                             "VALUES(?, ?, ?);", total)
            self.conn.commit()

            self.lineEdit_firstname.setText('')
            self.lineEdit_lastname.setText('')
            self.lineEdit_thirdname.setText('')
            self.lineEdit_login.setText('')
            self.lineEdit_password.setText('')
            self.lineEdit_password2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin()
    ex.show()
    sys.exit(app.exec())
