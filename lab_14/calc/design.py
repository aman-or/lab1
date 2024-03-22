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
                           QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(518, 750)
        MainWindow.setMinimumSize(QSize(518, 750))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculator.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"    border-radius: 60px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 60px; /* \u041e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}\n"
"\n"
"QPushButton#btn_div,\n"
"QPushButton#btn_mul,\n"
"QPushButton#btn_sub,\n"
"QPushButton#btn_plus,\n"
"QPushButton#btn_calc {\n"
"    color: white;\n"
"    background-color: #fe9f0a;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton#btn_div:hover,\n"
"QPushButton#btn_mul:hover,\n"
"QPushButton#btn_sub:hover,\n"
"QPushButton#btn_plus:hover,\n"
"QPushButton#btn_calc:hover {\n"
"    backgrou"
                        "nd-color: #666;\n"
"}\n"
"\n"
"QPushButton#btn_div:pressed,\n"
"QPushButton#btn_mul:pressed,\n"
"QPushButton#btn_sub:pressed,\n"
"QPushButton#btn_plus:pressed,\n"
"QPushButton#btn_calc:pressed {\n"
"    background-color: #888;\n"
"}\n"
"\n"
"QPushButton#btn_backspace,\n"
"QPushButton#btn_neg,\n"
"QPushButton#btn_clear {\n"
"    color: white;\n"
"    background-color: #a5a5a5;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton#btn_backspace:hover,\n"
"QPushButton#btn_neg:hover,\n"
"QPushButton#btn_clear:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton#btn_backspace:pressed,\n"
"QPushButton#btn_neg:pressed,\n"
"QPushButton#btn_clear:pressed {\n"
"    background-color: #888;\n"
"}\n"
"\n"
"QPushButton#btn_0,\n"
"QPushButton#btn_1,\n"
"QPushButton#btn_2,\n"
"QPushButton#btn_3,\n"
"QPushButton#btn_4,\n"
"QPushButton#btn_5,\n"
"QPushButton#btn_6,\n"
"QPushButton#btn_7,\n"
"QPushButton#btn_8,\n"
"QPushButton#btn_9,\n"
"QPushButton#btn_point {\n"
""
                        "    color: white;\n"
"    background-color: #333333;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton#btn_0:hover,\n"
"QPushButton#btn_1:hover,\n"
"QPushButton#btn_2:hover,\n"
"QPushButton#btn_3:hover,\n"
"QPushButton#btn_4:hover,\n"
"QPushButton#btn_5:hover,\n"
"QPushButton#btn_6:hover,\n"
"QPushButton#btn_7:hover,\n"
"QPushButton#btn_8:hover,\n"
"QPushButton#btn_9:hover,\n"
"QPushButton#btn_point:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton#btn_0:pressed,\n"
"QPushButton#btn_1:pressed,\n"
"QPushButton#btn_2:pressed,\n"
"QPushButton#btn_3:pressed,\n"
"QPushButton#btn_4:pressed,\n"
"QPushButton#btn_5:pressed,\n"
"QPushButton#btn_6:pressed,\n"
"QPushButton#btn_7:pressed,\n"
"QPushButton#btn_8:pressed,\n"
"QPushButton#btn_9:pressed,\n"
"QPushButton#btn_point:pressed {\n"
"    background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(16)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy2.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy2)
        self.btn_clear.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_clear.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy2.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy2)
        self.btn_plus.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_plus, 4, 3, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_1, 4, 0, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_neg, 0, 1, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_3, 4, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_point, 5, 2, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_2, 4, 1, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_calc, 5, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout.addWidget(self.btn_0, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"calc", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        # 6
        for sc in '6':
            QShortcut(sc, self.btn_6).activated.connect(self.btn_6.animateClick)

        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        # subtraction
        for sc in '-':
            QShortcut(sc, self.btn_sub).activated.connect(self.btn_sub.animateClick)

        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        # 9
        for sc in '9':
            QShortcut(sc, self.btn_9).activated.connect(self.btn_9.animateClick)

        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        # 7
        for sc in '7':
            QShortcut(sc, self.btn_7).activated.connect(self.btn_7.animateClick)

        self.btn_backspace.setText("")
        # if QT_CONFIG(shortcut)
        # del symbol
        for sc in 'Backspace':
            QShortcut(sc, self.btn_backspace).activated.connect(self.btn_backspace.animateClick)
        # endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        # 5
        for sc in '5':
            QShortcut(sc, self.btn_5).activated.connect(self.btn_5.animateClick)

        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        # division
        for sc in '/':
            QShortcut(sc, self.btn_div).activated.connect(self.btn_div.animateClick)

        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        # clear all
        for sc in 'Del':
            QShortcut(sc, self.btn_clear).activated.connect(self.btn_clear.animateClick)

        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        # addition
        for sc in '+':
            QShortcut(sc, self.btn_plus).activated.connect(self.btn_plus.animateClick)

        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        # 1
        for sc in '1':
            QShortcut(sc, self.btn_1).activated.connect(self.btn_1.animateClick)

        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        # multiplication
        for sc in '*':
            QShortcut(sc, self.btn_mul).activated.connect(self.btn_mul.animateClick)

        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        # 4
        for sc in '4':
            QShortcut(sc, self.btn_4).activated.connect(self.btn_4.animateClick)

        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        # 2
        for sc in '3':
            QShortcut(sc, self.btn_3).activated.connect(self.btn_3.animateClick)

        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        # 8
        for sc in '8':
            QShortcut(sc, self.btn_8).activated.connect(self.btn_8.animateClick)

        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))

        for sc in ('.', ','):
            QShortcut(sc, self.btn_point).activated.connect(self.btn_point.animateClick)

        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        # 2
        for sc in '2':
            QShortcut(sc, self.btn_2).activated.connect(self.btn_2.animateClick)

        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
        # equal
        for sc in ('=', 'Enter', 'Return'):
            QShortcut(sc, self.btn_calc).activated.connect(self.btn_calc.animateClick)

        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        # 0
        for sc in '0':
            QShortcut(sc, self.btn_0).activated.connect(self.btn_0.animateClick)
    # retranslateUi

