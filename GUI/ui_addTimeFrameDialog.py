# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTimeFrameDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTimeEdit, QVBoxLayout, QWidget)
import icons_resources_rc

class Ui_AddTimeFrame_Dialog(object):
    def setupUi(self, AddTimeFrame_Dialog):
        if not AddTimeFrame_Dialog.objectName():
            AddTimeFrame_Dialog.setObjectName(u"AddTimeFrame_Dialog")
        AddTimeFrame_Dialog.resize(320, 194)
        AddTimeFrame_Dialog.setMinimumSize(QSize(320, 194))
        AddTimeFrame_Dialog.setMaximumSize(QSize(320, 194))
        AddTimeFrame_Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.977, y1:0.971455, x2:1, y2:1, stop:0.221591 rgba(106, 184, 226, 239), stop:1 rgba(255, 255, 255, 255));")
        AddTimeFrame_Dialog.setLocale(QLocale(QLocale.English, QLocale.Israel))
        self.check_PushButton = QPushButton(AddTimeFrame_Dialog)
        self.check_PushButton.setObjectName(u"check_PushButton")
        self.check_PushButton.setGeometry(QRect(180, 140, 61, 31))
        self.check_PushButton.setStyleSheet(u"image: url(:/icons/resources/check.png);")
        self.horizontalLayoutWidget = QWidget(AddTimeFrame_Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 121, 65))
        self.verticalLayout = QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.timeEdit = QTimeEdit(self.horizontalLayoutWidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setStyleSheet(u"QTimeEdit::down-button{\n"
"	image: url(:/icons/resources/DW.png);\n"
"    width: 35px;\n"
"	height : 30px;\n"
"	subcontrol-position: right;\n"
"\n"
"}\n"
"QTimeEdit::up-button{\n"
"	image: url(:/icons/resources/UW.png);\n"
"    subcontrol-position: left;\n"
"    width: 35px;\n"
"	height : 30px;\n"
"}")
        self.timeEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.timeEdit, 0, Qt.AlignBottom)

        self.horizontalLayoutWidget_2 = QWidget(AddTimeFrame_Dialog)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(170, 30, 121, 65))
        self.verticalLayout_2 = QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignTop)

        self.timeEdit_2 = QTimeEdit(self.horizontalLayoutWidget_2)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setStyleSheet(u"QTimeEdit::down-button{\n"
"	image: url(:/icons/resources/DW.png);\n"
"    width: 35px;\n"
"	height : 30px;\n"
"	subcontrol-position: right;\n"
"\n"
"}\n"
"QTimeEdit::up-button{\n"
"	image: url(:/icons/resources/UW.png);\n"
"    subcontrol-position: left;\n"
"    width: 35px;\n"
"	height : 30px;\n"
"}")
        self.timeEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.timeEdit_2, 0, Qt.AlignBottom)

        self.close_PushButton = QPushButton(AddTimeFrame_Dialog)
        self.close_PushButton.setObjectName(u"close_PushButton")
        self.close_PushButton.setGeometry(QRect(70, 140, 61, 31))
        self.close_PushButton.setStyleSheet(u"image: url(:/icons/resources/close.png);")

        self.retranslateUi(AddTimeFrame_Dialog)

        QMetaObject.connectSlotsByName(AddTimeFrame_Dialog)
    # setupUi

    def retranslateUi(self, AddTimeFrame_Dialog):
        AddTimeFrame_Dialog.setWindowTitle(QCoreApplication.translate("AddTimeFrame_Dialog", u"Add Time Frame", None))
        self.check_PushButton.setText("")
        self.label.setText(QCoreApplication.translate("AddTimeFrame_Dialog", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("AddTimeFrame_Dialog", u"End", None))
        self.close_PushButton.setText("")
    # retranslateUi

