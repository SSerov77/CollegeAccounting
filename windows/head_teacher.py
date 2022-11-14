# подключение библиотек
import csv
import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QTableWidgetItem

from ui_py_files.HeadTeacherWindow import Ui_HeadTeacherWindow

from windows import sign, add_student, add_group, add_schoudle, add_teacher


class HeadTeacher(QMainWindow, Ui_HeadTeacherWindow):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)

        self.pushButton_upload_shedule.setStyleSheet("background-color: #30AB0D")
        self.pushButton_upload_students.setStyleSheet("background-color: #30AB0D")
        self.pushButton_upload_groups.setStyleSheet("background-color: #30AB0D")
        self.pushButton_upload_teachers.setStyleSheet("background-color: #30AB0D")

        self.label.setText(name)
        self.pushButton_back.clicked.connect(self.back)
        self.tabWidget.currentChanged.connect(self.db)

        self.pushButton_search_groups.clicked.connect(self.to_find)
        self.pushButton_search_shedule.clicked.connect(self.to_find)
        self.pushButton_search_teachers.clicked.connect(self.to_find)
        self.pushButton_search_students.clicked.connect(self.to_find)

        self.pushButton_add_groups.clicked.connect(self.too_add)
        self.pushButton_add_students.clicked.connect(self.too_add)
        self.pushButton_add_teachers.clicked.connect(self.too_add)
        self.pushButton_add_shedule.clicked.connect(self.too_add)

        self.pushButton_upload_groups.clicked.connect(self.to_upload)
        self.pushButton_upload_shedule.clicked.connect(self.to_upload)
        self.pushButton_upload_teachers.clicked.connect(self.to_upload)
        self.pushButton_upload_students.clicked.connect(self.to_upload)

        self.conn = sqlite3.connect('database/database.db')
        self.cur = self.conn.cursor()

        self.db()

        self.tableWidget.itemChanged.connect(self.item_changed)
        self.tableWidget_2.itemChanged.connect(self.item_changed)
        self.tableWidget_3.itemChanged.connect(self.item_changed)
        self.tableWidget_4.itemChanged.connect(self.item_changed)

        self.modified = {}
        self.titles = None

    def db(self):
        try:
            if self.tabWidget.currentIndex() == 0:
                res = self.cur.execute(
                    f"SELECT id, name FROM groups").fetchall()
                self.tableWidget.setColumnCount(2)

                for i in range(3):
                    self.tableWidget.setColumnWidth(i, 347)  # постороения таблицы
                self.tableWidget.setHorizontalHeaderLabels(
                    ['Номер', 'ФИО'])

                rowcount = \
                    self.cur.execute(f"SELECT COUNT(*) FROM groups").fetchone()[0]
                self.db_res(res, rowcount, 1)

            elif self.tabWidget.currentIndex() == 1:
                res = self.cur.execute(
                    f"SELECT id, teacher, monday, tuesday, wednesday, thursday, friday, saturday, sunday FROM schedule").fetchall()
                self.tableWidget_2.setColumnCount(9)

                for i in range(7):
                    self.tableWidget_2.setColumnWidth(i, 73)  # постороения таблицы
                self.tableWidget_2.setHorizontalHeaderLabels(
                    ['Номер', 'Учитель', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])

                rowcount = \
                    self.cur.execute(f"SELECT COUNT(*) FROM schedule").fetchone()[0]
                self.db_res2(res, rowcount)

            elif self.tabWidget.currentIndex() == 2:
                res = self.cur.execute(
                    f"SELECT id, name FROM teachers").fetchall()
                self.tableWidget_3.setColumnCount(2)

                for i in range(2):
                    self.tableWidget_3.setColumnWidth(i, 347)  # постороения таблицы
                self.tableWidget_3.setHorizontalHeaderLabels(
                    ['Номер', 'ФИО'])

                rowcount = \
                    self.cur.execute(f"SELECT COUNT(*) FROM teachers").fetchone()[0]
                self.db_res(res, rowcount, 3)

            elif self.tabWidget.currentIndex() == 3:
                res = self.cur.execute(
                    f"SELECT id, name, groups FROM students").fetchall()
                self.tableWidget_4.setColumnCount(3)

                for i in range(3):
                    self.tableWidget_4.setColumnWidth(i, 230)  # постороения таблицы
                self.tableWidget_4.setHorizontalHeaderLabels(
                    ['Номер', 'ФИО', 'Группа'])

                rowcount = \
                    self.cur.execute(f"SELECT COUNT(*) FROM students").fetchone()[0]
                self.db_res3(res, rowcount)
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def db_res(self, result, rowcou, num):
        try:
            tab = 0
            if num == 1:
                self.tableWidget.setRowCount(rowcou)
                for row in result:
                    self.tableWidget.setItem(tab, 0, QTableWidgetItem(str(row[0])))
                    self.tableWidget.setItem(tab, 1, QTableWidgetItem(row[1]))
                    tab += 1
            else:
                self.tableWidget_3.setRowCount(rowcou)
                for row in result:
                    self.tableWidget_3.setItem(tab, 0, QTableWidgetItem(str(row[0])))
                    self.tableWidget_3.setItem(tab, 1, QTableWidgetItem(row[1]))
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
                self.tableWidget_2.setItem(tab, 7, QTableWidgetItem(row[7]))
                self.tableWidget_2.setItem(tab, 8, QTableWidgetItem(row[8]))

                tab += 1
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def db_res3(self, result, rowcou):
        try:
            self.tableWidget_4.setRowCount(rowcou)
            tab = 0
            for row in result:
                self.tableWidget_4.setItem(tab, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget_4.setItem(tab, 1, QTableWidgetItem(row[1]))
                self.tableWidget_4.setItem(tab, 2, QTableWidgetItem(row[2]))
                tab += 1
        except Exception:
            print()

    def back(self):
        try:
            self.open = sign.Sign()
            self.open.show()
            self.close()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def keyPressEvent(self, event):
        try:
            if self.tabWidget.currentIndex() == 0:
                if event.key() == Qt.Key_Delete:  # проверка нажатия
                    rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
                    ids = [self.tableWidget.item(i, 0).text() for i in rows]  # получение выделенных id
                    name = [self.tableWidget.item(i, 1).text() for i in rows]  # получение названия

                    valid = QMessageBox.question(  # всплывающее окно с уточнением
                        self, '', "Вы действительно хотите удалить " + ",".join(name) + '?',
                        QMessageBox.Yes, QMessageBox.No)

                    if valid == QMessageBox.Yes:  # Проверка ответа
                        self.cur.execute("DELETE FROM groups WHERE id IN (" + ", ".join(
                            '?' * len(ids)) + ")", ids)
                        self.conn.commit()
                    self.db()
            if self.tabWidget.currentIndex() == 1:
                if event.key() == Qt.Key_Delete:  # проверка нажатия
                    rows = list(set([i.row() for i in self.tableWidget_2.selectedItems()]))
                    ids = [self.tableWidget_2.item(i, 0).text() for i in rows]  # получение выделенных id
                    name = [self.tableWidget_2.item(i, 1).text() for i in rows]  # получение названия

                    valid = QMessageBox.question(  # всплывающее окно с уточнением
                        self, '', "Вы действительно хотите удалить " + ",".join(name) + '?',
                        QMessageBox.Yes, QMessageBox.No)

                    if valid == QMessageBox.Yes:  # Проверка ответа
                        self.cur.execute("DELETE FROM shedule WHERE id IN (" + ", ".join(
                            '?' * len(ids)) + ")", ids)
                        self.conn.commit()
                    self.db()
            if self.tabWidget.currentIndex() == 2:
                if event.key() == Qt.Key_Delete:  # проверка нажатия
                    rows = list(set([i.row() for i in self.tableWidget_3.selectedItems()]))
                    ids = [self.tableWidget_3.item(i, 0).text() for i in rows]  # получение выделенных id
                    name = [self.tableWidget_3.item(i, 1).text() for i in rows]  # получение названия

                    valid = QMessageBox.question(  # всплывающее окно с уточнением
                        self, '', "Вы действительно хотите удалить " + ",".join(name) + '?',
                        QMessageBox.Yes, QMessageBox.No)

                    if valid == QMessageBox.Yes:  # Проверка ответа
                        self.cur.execute("DELETE FROM teachers WHERE id IN (" + ", ".join(
                            '?' * len(ids)) + ")", ids)
                        self.conn.commit()
                    self.db()
            if self.tabWidget.currentIndex() == 3:
                if event.key() == Qt.Key_Delete:  # проверка нажатия
                    rows = list(set([i.row() for i in self.tableWidget_4.selectedItems()]))
                    ids = [self.tableWidget_4.item(i, 0).text() for i in rows]  # получение выделенных id
                    name = [self.tableWidget_4.item(i, 1).text() for i in rows]  # получение названия

                    valid = QMessageBox.question(  # всплывающее окно с уточнением
                        self, '', "Вы действительно хотите удалить " + ",".join(name) + '?',
                        QMessageBox.Yes, QMessageBox.No)

                    if valid == QMessageBox.Yes:  # Проверка ответа
                        self.cur.execute("DELETE FROM students WHERE id IN (" + ",".join(
                            '?' * len(ids)) + ")", ids)
                        self.conn.commit()
                    self.db()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def to_find(self):
        try:
            if self.tabWidget.currentIndex() == 0:
                select = 'name'
                fro_m = 'groups'
                text = self.lineEdit_groups.text()  # введёный текст
                self.to_find_help(select, fro_m, text)

            elif self.tabWidget.currentIndex() == 1:
                select = 'teacher'
                fro_m = 'schedule'
                text = self.lineEdit_shedule.text()
                self.to_find_help(select, fro_m, text)

            elif self.tabWidget.currentIndex() == 2:
                select = 'name'
                fro_m = 'teachers'
                text = self.lineEdit_teachers.text()  # введёный текст
                self.to_find_help(select, fro_m, text)

            elif self.tabWidget.currentIndex() == 3:
                text = self.lineEdit_students.text()  # введёный текст

                # запросы с БД
                result = self.cur.execute(f"SELECT groups FROM students").fetchall()
                result_2 = self.cur.execute(f"SELECT name FROM students").fetchall()
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
                                f"SELECT id, name, groups FROM students WHERE groups='{text}'").fetchall()
                            rowcount = self.cur.execute(
                                f"SELECT COUNT(*) FROM students WHERE groups='{text}'").fetchone()[
                                0]
                        else:
                            res = self.cur.execute(f"SELECT * FROM students").fetchall()
                            rowcount = \
                                self.cur.execute(f"SELECT COUNT(*) FROM students").fetchone()[0]

                    elif text in prod_2:
                        res = self.cur.execute(
                            f"SELECT id, name, groups FROM students WHERE name='{text}'").fetchall()
                        rowcount = self.cur.execute(
                            f"SELECT COUNT(*) FROM students WHERE name='{text}'").fetchone()[0]
                    self.db_res3(res, rowcount)
                else:
                    QMessageBox.about(self, "Ошибка", "Ничего не найдено!")
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def to_find_help(self, select, fro_m, text):
        try:
            result = self.cur.execute(f"SELECT {select} FROM {fro_m}").fetchall()
            prod = []

            # обработка полученных данных
            for i in result:
                prod.append(i[0])

            # основная часть функции - поиск
            if text in prod or text == '':
                if text in prod or text == '':
                    if text != '':
                        res = self.cur.execute(
                            f"SELECT * FROM {fro_m} WHERE {select}='{text}'").fetchall()
                        rowcount = self.cur.execute(
                            f"SELECT COUNT(*) FROM {fro_m} WHERE {select}='{text}'").fetchone()[
                            0]
                    else:
                        res = self.cur.execute(f"SELECT * FROM {fro_m}").fetchall()
                        rowcount = self.cur.execute(f"SELECT COUNT(*) FROM {fro_m}").fetchone()[0]

                if self.tabWidget.currentIndex() == 0:
                    self.db_res(res, rowcount, 1)
                elif self.tabWidget.currentIndex() == 1:
                    self.db_res2(res, rowcount)
                elif self.tabWidget.currentIndex() == 2:
                    self.db_res(res, rowcount, 3)
                elif self.tabWidget.currentIndex() == 3:
                    self.db_res3(res, rowcount)
            else:
                QMessageBox.about(self, "Ошибка", "Ничего не найдено!")

        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def to_upload(self):
        try:
            if self.tabWidget.currentIndex() == 0:
                text = 'groups.csv'
                table = self.tableWidget
            elif self.tabWidget.currentIndex() == 1:
                text = 'schedule.csv'
                table = self.tableWidget_2
            elif self.tabWidget.currentIndex() == 2:
                text = 'teachers.csv'
                table = self.tableWidget_3
            elif self.tabWidget.currentIndex() == 3:
                text = 'students.csv'
                table = self.tableWidget_4

            with open(text, 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)

                # Получение списка заголовков
                writer.writerow(
                    [table.horizontalHeaderItem(i).text()
                     for i in range(1, table.columnCount())])
                for i in range(table.rowCount()):
                    row = []
                    for j in range(1, table.columnCount()):
                        item = table.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")

    def item_changed(self, item):
        try:
            if self.tabWidget.currentIndex() == 0:
                table = 'groups'
            elif self.tabWidget.currentIndex() == 1:
                table = 'schedule'
            elif self.tabWidget.currentIndex() == 2:
                table = 'teachers'
            elif self.tabWidget.currentIndex() == 3:
                table = 'students'

            tot = []
            self.pays = {}
            self.total = self.cur.execute(f'''SELECT * FROM {table}''').fetchall()

            # получение данных в ячейках
            self.titles = [description[0] for description in self.cur.description]
            for i in self.total:
                tot.append(i[0])
            tot.sort()
            for j in range(len(tot)):
                self.pays[j] = tot[j]
            self.modified[self.titles[item.column()]] = [item.text(), item.row()]

            # обновление БД
            que = f"UPDATE {table} SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)[0]}'"
                              for key in self.modified.keys()])
            que += f"WHERE id = {self.pays[[self.modified.get(key)[1] for key in self.modified.keys()][0]]}"

            self.cur.execute(que)
            self.conn.commit()
            self.modified.clear()
        except Exception:
            pass

    def too_add(self):
        try:
            if self.tabWidget.currentIndex() == 0:
                self.open = add_group.AddGroup()
            elif self.tabWidget.currentIndex() == 1:
                self.open = add_schoudle.AddSchedule()
            elif self.tabWidget.currentIndex() == 2:
                self.open = add_teacher.AddTeacher()
            elif self.tabWidget.currentIndex() == 3:
                self.open = add_student.AddStudent()

            self.open.show()
        except Exception:
            QMessageBox.about(self, "Ошибка", "Извините, возможно произошла ошибка")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HeadTeacher()
    ex.show()
    sys.exit(app.exec())
