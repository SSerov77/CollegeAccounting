import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

from ui_py_files.TeacherWindow import Ui_TeacherWindow


class Teacher(QMainWindow, Ui_TeacherWindow):
    def __init__(self, name):
        try:
            super().__init__()
            self.setupUi(self)

            self.label.setText(str(name[0]))

        except Exception:
            QMessageBox.about(self, "Ошибка", "Произошла ошибка!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Teacher()
    ex.show()
    sys.exit(app.exec())
