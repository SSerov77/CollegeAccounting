# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGroup.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_group(object):
    def setupUi(self, Add_group):
        Add_group.setObjectName("Add_group")
        Add_group.resize(231, 211)
        self.lineEdit = QtWidgets.QLineEdit(Add_group)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Add_group)
        self.label.setGeometry(QtCore.QRect(20, 40, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Add_group)
        self.pushButton.setGeometry(QtCore.QRect(50, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Add_group)
        QtCore.QMetaObject.connectSlotsByName(Add_group)

    def retranslateUi(self, Add_group):
        _translate = QtCore.QCoreApplication.translate
        Add_group.setWindowTitle(_translate("Add_group", "Добавить группу"))
        self.label.setText(_translate("Add_group", "Название группы:"))
        self.pushButton.setText(_translate("Add_group", "Добавить"))
