# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_demo.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QPushButton, QSizePolicy, QWidget)
import img

class Ui_Formdemo(object):
    def setupUi(self, Formdemo):
        if not Formdemo.objectName():
            Formdemo.setObjectName(u"Formdemo")
        Formdemo.resize(700, 300)
        Formdemo.setMinimumSize(QSize(700, 300))
        Formdemo.setMaximumSize(QSize(700, 500))
        Formdemo.setWindowOpacity(6.000000000000000)
        Formdemo.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(56, 56, 56);")
        self.startbtn = QPushButton(Formdemo)
        self.startbtn.setObjectName(u"startbtn")
        self.startbtn.setGeometry(QRect(280, 200, 121, 51))
        self.startbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startbtn.setMouseTracking(True)
        self.startbtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3E8E41;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2E6739;\n"
"}")
        self.layoutWidget = QWidget(Formdemo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 40, 431, 163))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.btntest = QPushButton(self.layoutWidget)
        self.btntest.setObjectName(u"btntest")

        self.gridLayout.addWidget(self.btntest, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 5, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_info = QLineEdit(Formdemo)
        self.lineEdit_info.setObjectName(u"lineEdit_info")
        self.lineEdit_info.setEnabled(False)
        self.lineEdit_info.setGeometry(QRect(220, 259, 241, 31))
        self.lineEdit_info.setStyleSheet(u"background-color: rgb(248, 255, 239);\n"
"color: rgb(170, 0, 0);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"border: none;")
        self.lineEdit_info.setAlignment(Qt.AlignCenter)
        self.lineEdit_info.setReadOnly(False)
        self.lineEdit_ver = QLineEdit(Formdemo)
        self.lineEdit_ver.setObjectName(u"lineEdit_ver")
        self.lineEdit_ver.setEnabled(False)
        self.lineEdit_ver.setGeometry(QRect(590, 280, 113, 20))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(False)
        self.lineEdit_ver.setFont(font)
        self.lineEdit_ver.setStyleSheet(u"font: 700 6pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(240, 240, 240);\n"
"border: none;")
        self.lineEdit_ver.setAlignment(Qt.AlignCenter)
        self.logo = QLabel(Formdemo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 260, 121, 31))
        self.logo.setPixmap(QPixmap(u":/img/bosch_icon.png"))
        self.logo.setScaledContents(True)

        self.retranslateUi(Formdemo)

        QMetaObject.connectSlotsByName(Formdemo)
    # setupUi

    def retranslateUi(self, Formdemo):
        Formdemo.setWindowTitle(QCoreApplication.translate("Formdemo", u"SysEng2.0 Data Query Tool", None))
#if QT_CONFIG(whatsthis)
        self.startbtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.startbtn.setText(QCoreApplication.translate("Formdemo", u"\u5f00\u59cb\u66f4\u65b0", None))
        self.label.setText(QCoreApplication.translate("Formdemo", u"\u673a\u68b0\u53c2\u6570\u8868", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Formdemo", u"\u8bf7\u9009\u62e9\u673a\u68b0\u53c2\u6570\u8868", None))
        self.btntest.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Formdemo", u"\u8bf7\u9009\u62e9Geskon\u6587\u4ef6", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Formdemo", u"\u8bf7\u9009\u62e9DCM\u6587\u4ef6", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Formdemo", u"\u8bf7\u9009\u62e9A2L\u6587\u4ef6", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Formdemo", u"\u8bf7\u9009\u62e9Data\u8868", None))
        self.pushButton.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton_2.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton_4.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Formdemo", u"Geskon\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("Formdemo", u"DCM\u6587\u4ef6", None))
        self.label_4.setText(QCoreApplication.translate("Formdemo", u"A2L\u6587\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("Formdemo", u"Data\u8868", None))
        self.lineEdit_info.setText("")
        self.lineEdit_info.setPlaceholderText(QCoreApplication.translate("Formdemo", u"\u7b49\u5f85\u8fd0\u884c... ...", None))
        self.lineEdit_ver.setText(QCoreApplication.translate("Formdemo", u"Ver: 1.1 Demo", None))
        self.logo.setText("")
    # retranslateUi

