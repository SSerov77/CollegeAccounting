# подключение библиотек
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.SignWindow import Ui_Sign
from windows import admin
from windows import teacher
from windows import head_teacher


class Sign(QMainWindow, Ui_Sign):
    def __init__(self):
        try:
            super().__init__()
            self.setupUi(self)

            self.pushButton.clicked.connect(self.enter)
            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()
            self.lineEdit_sign_password.setEchoMode(self.lineEdit_sign_login.Password)


        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def enter(self):
        try:
            results_login_passw = []
            login = self.lineEdit_sign_login.text()
            password = self.lineEdit_sign_password.text()
            if login != '' or password != '':
                if login == "admin" and password == "admin":
                    self.open = admin.Admin()
                    self.open.show()
                    self.close()
                else:
                    result = self.cur.execute('''SELECT login, password FROM teachers''').fetchall()
                    for i in result:
                        results_login_passw.append(i)
                    total = (login, password)
                    if total in results_login_passw:
                        name = self.cur.execute(f"SELECT name, job FROM teachers WHERE login='{login}'").fetchall()[0]

                        if name[1] == 'Преподаватель':
                            self.open = teacher.Teacher(name[0])
                        elif name[1] == 'Завуч':
                            self.open = head_teacher.HeadTeacher(name[0])
                        self.open.show()
                        self.close()
                    else:
                        QMessageBox.about(self, "Ошибка", "Введен неправильно логин или пароль")
            else:
                QMessageBox.about(self, "Ошибка", "Введите логин или пароль")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sign()
    ex.show()
    sys.exit(app.exec())
