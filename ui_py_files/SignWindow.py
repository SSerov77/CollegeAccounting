# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sign(object):
    def setupUi(self, Sign):
        Sign.setObjectName("Sign")
        Sign.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Sign)
        self.pushButton.setGeometry(QtCore.QRect(90, 220, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Sign)
        self.widget.setGeometry(QtCore.QRect(30, 30, 341, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sign_login = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sign_login.setFont(font)
        self.label_sign_login.setObjectName("label_sign_login")
        self.verticalLayout.addWidget(self.label_sign_login)
        self.lineEdit_sign_login = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_sign_login.setObjectName("lineEdit_sign_login")
        self.verticalLayout.addWidget(self.lineEdit_sign_login)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_sign_password = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_sign_password.setFont(font)
        self.label_sign_password.setObjectName("label_sign_password")
        self.verticalLayout_2.addWidget(self.label_sign_password)
        self.lineEdit_sign_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_sign_password.setObjectName("lineEdit_sign_password")
        self.verticalLayout_2.addWidget(self.lineEdit_sign_password)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Sign)
        QtCore.QMetaObject.connectSlotsByName(Sign)

    def retranslateUi(self, Sign):
        _translate = QtCore.QCoreApplication.translate
        Sign.setWindowTitle(_translate("Sign", "Вход"))
        self.pushButton.setText(_translate("Sign", "Войти"))
        self.label_sign_login.setText(_translate("Sign", "Логин"))
        self.label_sign_password.setText(_translate("Sign", "Пароль"))
