import csv
import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem

from ui_py_files.TeacherWindow import Ui_TeacherWindow
from windows import sign


class Teacher(QMainWindow, Ui_TeacherWindow):
    def __init__(self, name):
        try:
            super().__init__()
            self.setupUi(self)
            self.name = name

            self.label.setText(str(name))
            self.pushButton.setStyleSheet("background-color: #30AB0D")
            self.tabWidget.currentChanged.connect(self.db)
            self.pushButton_back.clicked.connect(self.back)
            self.pushButton.clicked.connect(self.to_upload)
            self.pushButton_search.clicked.connect(self.to_find)

            self.conn = sqlite3.connect('database/database.db')
            self.cur = self.conn.cursor()

            self.db()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def db(self):
        try:
            if self.tabWidget.currentIndex() == 0:
                res = self.cur.execute(
                    f"SELECT id, name, groups FROM students WHERE teacher='{str(self.name)}'").fetchall()
                self.tableWidget.setColumnCount(3)

                for i in range(3):
                    self.tableWidget.setColumnWidth(i, 231)  # постороения таблицы
                self.tableWidget.setHorizontalHeaderLabels(
                    ['Номер', 'ФИО', 'Группа'])

                rowcount = \
                    self.cur.execute(f"SELECT COUNT(*) FROM students WHERE teacher='{str(self.name)}'").fetchone()[0]
                self.db_res(res, rowcount)
            else:
                res = self.cur.execute(
                    f"SELECT monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM schedule WHERE teacher='{str(self.name)}'").fetchall()
                self.tableWidget_2.setColumnCount(7)

                for i in range(7):
                    self.tableWidget_2.setColumnWidth(i, 97)  # постороения таблицы
                self.tableWidget_2.setHorizontalHeaderLabels(
                    ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])

                rowcount = \
                    self.cur.execute(f"SELECT COUNT(*) FROM schedule WHERE teacher='{str(self.name)}'").fetchone()[0]
                self.db_res2(res, rowcount)
            print(str(self.name))
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def db_res(self, result, rowcou):
        try:
            self.tableWidget.setRowCount(rowcou)
            tab = 0
            for row in result:
                self.tableWidget.setItem(tab, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(tab, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tab, 2, QTableWidgetItem(row[2]))
                tab += 1
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def db_res2(self, result, rowcou):
        try:
            self.tableWidget_2.setRowCount(rowcou)
            tab = 0
            for row in result:
                self.tableWidget_2.setItem(tab, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget_2.setItem(tab, 1, QTableWidgetItem(row[1]))
                self.tableWidget_2.setItem(tab, 2, QTableWidgetItem(row[2]))
                self.tableWidget_2.setItem(tab, 3, QTableWidgetItem(row[3]))
                self.tableWidget_2.setItem(tab, 4, QTableWidgetItem(row[4]))
                self.tableWidget_2.setItem(tab, 5, QTableWidgetItem(row[5]))
                self.tableWidget_2.setItem(tab, 6, QTableWidgetItem(row[6]))
                tab += 1
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def to_upload(self):
        try:
            with open('students.csv', 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                # Получение списка заголовков
                writer.writerow(
                    [self.tableWidget.horizontalHeaderItem(i).text()
                     for i in range(1, self.tableWidget.columnCount())])
                for i in range(self.tableWidget.rowCount()):
                    row = []
                    for j in range(1, self.tableWidget.columnCount()):
                        item = self.tableWidget.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def to_find(self):
        try:
            text = self.lineEdit.text()  # введёный текст

            # запросы с БД
            result = self.cur.execute(f"SELECT groups FROM students WHERE teacher='{str(self.name[0])}'").fetchall()
            result_2 = self.cur.execute(f"SELECT name FROM students WHERE teacher='{str(self.name[0])}'").fetchall()
            prod = []
            prod_2 = []

            # обработка полученных данных
            for i in result:
                prod.append(i[0])
            for i in result_2:
                prod_2.append(i[0])

            # основная часть функции - поиск
            if text in prod or text in prod_2 or text == '':
                if text in prod or text == '':
                    if text != '':
                        res = self.cur.execute(
                            f"SELECT id, name, groups FROM students WHERE groups='{text}' AND teacher='{self.name[0]}'").fetchall()
                        rowcount = self.cur.execute(
                            f"SELECT COUNT(*) FROM students WHERE groups='{text}' AND teacher='{self.name[0]}'").fetchone()[
                            0]
                    else:
                        res = self.cur.execute(f"SELECT * FROM students WHERE teacher='{self.name[0]}'").fetchall()
                        rowcount = \
                        self.cur.execute(f"SELECT COUNT(*) FROM students WHERE teacher='{self.name[0]}'").fetchone()[0]

                elif text in prod_2:
                    res = self.cur.execute(
                        f"SELECT id, name, groups FROM students WHERE name='{text}' AND teacher='{self.name[0]}'").fetchall()
                    rowcount = self.cur.execute(
                        f"SELECT COUNT(*) FROM students WHERE name='{text}' AND teacher='{self.name[0]}'").fetchone()[0]
                self.db_res(res, rowcount)
            else:
                QMessageBox.about(self, "Ошибка", "Ничего не найдено!")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def back(self):
        try:
            self.open = sign.Sign()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Teacher()
    ex.show()
    sys.exit(app.exec())
