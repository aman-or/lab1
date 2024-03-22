# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 698)
        MainWindow.setCursor(QCursor(Qt.OpenHandCursor))
        MainWindow.setStyleSheet(u"QWidget {\n"
"  background-color: #5f6df2;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 30, 300, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: #939ff5;\n"
"border-radius: 10;\n"
"color: white")
        self.label.setAlignment(Qt.AlignCenter)
        self.lbl_name = QLineEdit(self.centralwidget)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(150, 110, 471, 51))
        font1 = QFont()
        font1.setPointSize(18)
        self.lbl_name.setFont(font1)
        self.lbl_name.setStyleSheet(u"background-color: #939ff5;\n"
"border-radius: 10;\n"
"color: white;")
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(200, 190, 371, 51))
        font2 = QFont()
        font2.setPointSize(15)
        self.btn_start.setFont(font2)
        self.btn_start.setCursor(QCursor(Qt.ClosedHandCursor))
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(92, 105, 242, 255), stop:1 rgba(181, 192, 248, 255));\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #b6c1f7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b6c1f7;\n"
"}\n"
"")
        self.lbl_temper = QLabel(self.centralwidget)
        self.lbl_temper.setObjectName(u"lbl_temper")
        self.lbl_temper.setGeometry(QRect(240, 280, 291, 111))
        font3 = QFont()
        font3.setPointSize(45)
        self.lbl_temper.setFont(font3)
        self.lbl_temper.setStyleSheet(u"border-radius: 10;\n"
"color: white;")
        self.lbl_temper.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(90, 430, 561, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_humid = QLabel(self.gridLayoutWidget)
        self.lbl_humid.setObjectName(u"lbl_humid")
        font4 = QFont()
        font4.setPointSize(14)
        self.lbl_humid.setFont(font4)
        self.lbl_humid.setStyleSheet(u"background-color: #939ff5;\n"
"border-radius: 10;\n"
"color: white;")
        self.lbl_humid.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_humid, 0, 0, 1, 1)

        self.label_wind = QLabel(self.gridLayoutWidget)
        self.label_wind.setObjectName(u"label_wind")
        self.label_wind.setFont(font4)
        self.label_wind.setStyleSheet(u"background-color: #939ff5;\n"
"border-radius: 10;\n"
"color: white;")
        self.label_wind.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_wind, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 560, 761, 131))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background-color: #939ff5;\n"
"border-radius: 10;\n"
"color: white;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"What's whether?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0439 \u0441\u0432\u043e\u044e \u043f\u043e\u0433\u043e\u0434\u0443", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
        self.lbl_temper.setText("")
        self.lbl_humid.setText("")
        self.label_wind.setText("")
        self.label_2.setText("")
    # retranslateUi

