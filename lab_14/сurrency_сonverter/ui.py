# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 751)
        font = QtGui.QFont()
        font.setFamily("Dhurjati")
        font.setPointSize(14)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e;")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 261))
        self.frame.setStyleSheet("background-color: #f79837;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, -10, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 60, 181, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("exchanging.png"))
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(25)
        font.setBold(True)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f79837;\n"
"border-radius: 30px;\n"
"color: white;\n"
"")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 390, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(25)
        font.setBold(True)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f79837;\n"
"border-radius: 30px;\n"
"color: white;\n"
"")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(25)
        font.setBold(True)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f79837;\n"
"border-radius: 30px;\n"
"color: white;\n"
"")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 570, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(25)
        font.setBold(True)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f79837;\n"
"border-radius: 30px;\n"
"color: white;\n"
"")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 660, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #f79837;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b26211;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "КОНВЕРТЕР"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРУЙ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
