# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\testpyqt5\renjigongxiao\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(710, 529)
        Form.setStyleSheet("*{\n"
"background:rgb(255, 255, 255);\n"
"font-size:15px;\n"
"font-family:Century Gothic,sans-serif;\n"
"}\n"
"QFrame{\n"
"border:sold 10px rgba(0,0,0);\n"
"background-image:url(D:/testpyqt5/renjigongxiao/bg2.jpeg);\n"
"}\n"
"QLineEdit{\n"
"color:#8d98a1;\n"
"background-color:#405361;\n"
"font-size:16px;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton{\n"
"background:#ced1d8;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(224,0,0);\n"
"border-style:inset;\n"
"}\n"
"QCheckBox{\n"
"background:rgba(85,170,255,0);\n"
"color:white;\n"
"}\n"
"QLabel{\n"
"background:rgba(85,170,255,0);\n"
"color:white;\n"
"font-style:italic bold;\n"
"font-size:14px;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 711, 531))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(200, 430, 301, 41))
        self.loginButton.setObjectName("loginButton")
        self.nameLineEdit = QtWidgets.QLineEdit(self.frame)
        self.nameLineEdit.setGeometry(QtCore.QRect(200, 230, 301, 41))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordLineEdit.setGeometry(QtCore.QRect(200, 300, 301, 41))
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(201, 391, 111, 22))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(430, 393, 70, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 691, 131))
        font = QtGui.QFont()
        font.setFamily("方正小标宋简体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 20pt \"方正小标宋简体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(228, 130, 291, 71))
        font = QtGui.QFont()
        font.setFamily("方正小标宋简体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 20pt \"方正小标宋简体\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginButton.setText(_translate("Form", "登录"))
        self.nameLineEdit.setPlaceholderText(_translate("Form", "用户名"))
        self.passwordLineEdit.setPlaceholderText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "记住用户名"))
        self.label.setText(_translate("Form", "忘记密码？"))
        self.label_2.setText(_translate("Form", "中国兵器工业计算机应用技术研究所"))
        self.label_3.setText(_translate("Form", "认知力可视化平台"))
import pic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
