# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 503)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 450, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 1, 351, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_lastname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lastname.setFont(font)
        self.label_lastname.setObjectName("label_lastname")
        self.verticalLayout.addWidget(self.label_lastname)
        self.lineEdit_lastname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.verticalLayout.addWidget(self.lineEdit_lastname)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_firstname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_firstname.setFont(font)
        self.label_firstname.setObjectName("label_firstname")
        self.verticalLayout_2.addWidget(self.label_firstname)
        self.lineEdit_firstname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_firstname.setObjectName("lineEdit_firstname")
        self.verticalLayout_2.addWidget(self.lineEdit_firstname)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_thirdname = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_thirdname.setFont(font)
        self.label_thirdname.setObjectName("label_thirdname")
        self.verticalLayout_3.addWidget(self.label_thirdname)
        self.lineEdit_thirdname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_thirdname.setObjectName("lineEdit_thirdname")
        self.verticalLayout_3.addWidget(self.lineEdit_thirdname)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_login = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.verticalLayout_6.addWidget(self.label_login)
        self.lineEdit_login = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout_6.addWidget(self.lineEdit_login)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.verticalLayout_4.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_4.addWidget(self.lineEdit_password)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_password2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password2.setFont(font)
        self.label_password2.setObjectName("label_password2")
        self.verticalLayout_5.addWidget(self.label_password2)
        self.lineEdit_password2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password2.setObjectName("lineEdit_password2")
        self.verticalLayout_5.addWidget(self.lineEdit_password2)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.pushButton_back = QtWidgets.QPushButton(Form)
        self.pushButton_back.setGeometry(QtCore.QRect(30, 450, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.pushButton.setText(_translate("Form", "Зарегистрироваться"))
        self.label_lastname.setText(_translate("Form", "Фамилия"))
        self.label_firstname.setText(_translate("Form", "Имя"))
        self.label_thirdname.setText(_translate("Form", "Отчество"))
        self.label_login.setText(_translate("Form", "Логин"))
        self.label_password.setText(_translate("Form", "Пароль"))
        self.label_password2.setText(_translate("Form", "Повтор пароля"))
        self.pushButton_back.setText(_translate("Form", "Назад"))
