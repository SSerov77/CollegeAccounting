# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_student(object):
    def setupUi(self, Add_student):
        Add_student.setObjectName("Add_student")
        Add_student.resize(260, 291)
        self.lineEdit = QtWidgets.QLineEdit(Add_student)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Add_student)
        self.label.setGeometry(QtCore.QRect(20, 40, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Add_student)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Add_student)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 130, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Add_student)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Add_student)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 190, 221, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Add_student)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Add_student)
        QtCore.QMetaObject.connectSlotsByName(Add_student)

    def retranslateUi(self, Add_student):
        _translate = QtCore.QCoreApplication.translate
        Add_student.setWindowTitle(_translate("Add_student", "Добавить студента"))
        self.label.setText(_translate("Add_student", "ФИО студента:"))
        self.pushButton.setText(_translate("Add_student", "Добавить"))
        self.label_2.setText(_translate("Add_student", "Группа студента:"))
        self.label_3.setText(_translate("Add_student", "Главный преподаватель:"))
