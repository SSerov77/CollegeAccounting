import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.AdminWindow import Ui_Admin
from windows import sign


class Admin(QMainWindow, Ui_Admin):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)

            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()
            self.errors_job = True
            self.job = ''
            self.radioButton_teacher.toggled.connect(self.jober)
            self.radioButton_head_teacher.toggled.connect(self.jober)
            self.pushButton.clicked.connect(self.registration)
            self.pushButton_back.clicked.connect(self.back)
            self.bad_simbols = ['"', "'", '/', ';', ':', '&', '?', '!', '@', '#', '№', '$', '%', '^', '*', '(', ')',
                                '[',
                                ']', '{', '}', '>', '<', '`', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                                '=', '+', '-', '_']

        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")

    def jober(self):
        radioBtn = self.sender()
        self.job = radioBtn.text()
        print(self.job)
        self.errors_job = False

    def registration(self):
        logins = []
        errors = True
        errors_2 = False
        first_name = self.lineEdit_firstname.text().replace(" ", "").capitalize()
        last_name = self.lineEdit_lastname.text().replace(" ", "").capitalize()
        third_name = self.lineEdit_thirdname.text().replace(" ", "").capitalize()
        login = self.lineEdit_login.text().replace(" ", "")
        password = self.lineEdit_password.text()
        password2 = self.lineEdit_password2.text()

        for i in first_name:
            if i in self.bad_simbols:
                errors_2 = True
        for i in last_name:
            if i in self.bad_simbols:
                errors_2 = True
        for i in third_name:
            if i in self.bad_simbols:
                errors_2 = True

        result = self.cur.execute("SELECT login FROM teachers").fetchall()
        for i in result:
            logins.append(i[0])

        print(self.errors_job)
        if first_name == '' or last_name == '' or third_name == '' or login == '' or password == '' or password2 == '' or self.errors_job:
            QMessageBox.about(self, "Ошибка", "Вы заполнили не все поля")

        elif (login in logins) or login == 'admin':
            QMessageBox.about(self, "Ошибка", "Такой логин уже существует")
        elif password2 != password:
            QMessageBox.about(self, "Ошибка", "Пароли не совпадают")
        elif errors_2:
            QMessageBox.about(self, "Ошибка", "В фамилии, имени или отчестве присутствуют запрещенные символы")
        else:
            errors = False

        if errors is False:
            name = f"{last_name} {first_name} {third_name}"
            total = (name, login, password, self.job)
            self.cur.execute("INSERT INTO teachers(name, login, password, job)"
                             "VALUES(?, ?, ?, ?);", total)
            self.conn.commit()

            self.lineEdit_firstname.setText('')
            self.lineEdit_lastname.setText('')
            self.lineEdit_thirdname.setText('')
            self.lineEdit_login.setText('')
            self.lineEdit_password.setText('')
            self.lineEdit_password2.setText('')

    def back(self):
        self.open = sign.Sign()
        self.open.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Admin()
    ex.show()
    sys.exit(app.exec())
