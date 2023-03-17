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

class Ui_Formdemo(object):
    def setupUi(self, Formdemo):
        if not Formdemo.objectName():
            Formdemo.setObjectName(u"Formdemo")
        Formdemo.resize(669, 300)
        self.pushButton_5 = QPushButton(Formdemo)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(300, 210, 75, 24))
        self.layoutWidget = QWidget(Formdemo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 40, 431, 148))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

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


        self.retranslateUi(Formdemo)

        QMetaObject.connectSlotsByName(Formdemo)
    # setupUi

    def retranslateUi(self, Formdemo):
        Formdemo.setWindowTitle(QCoreApplication.translate("Formdemo", u"Formdemo", None))
        self.pushButton_5.setText(QCoreApplication.translate("Formdemo", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Formdemo", u"\u673a\u68b0\u53c2\u6570\u8868", None))
        self.btntest.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton_2.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.pushButton_4.setText(QCoreApplication.translate("Formdemo", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Formdemo", u"Geskon\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("Formdemo", u"DCM\u6587\u4ef6", None))
        self.label_4.setText(QCoreApplication.translate("Formdemo", u"A2L\u6587\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("Formdemo", u"Data\u8868", None))
    # retranslateUi

