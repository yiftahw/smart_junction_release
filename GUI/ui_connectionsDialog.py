# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectionsDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)
import icons_resources_rc

class Ui_Connections_Dialog(object):
    def setupUi(self, Connections_Dialog):
        if not Connections_Dialog.objectName():
            Connections_Dialog.setObjectName(u"Connections_Dialog")
        Connections_Dialog.resize(549, 392)
        Connections_Dialog.setMinimumSize(QSize(320, 194))
        Connections_Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.977, y1:0.971455, x2:1, y2:1, stop:0.221591 rgba(106, 184, 226, 239), stop:1 rgba(255, 255, 255, 255));")
        Connections_Dialog.setLocale(QLocale(QLocale.English, QLocale.Israel))
        self.check_PushButton = QPushButton(Connections_Dialog)
        self.check_PushButton.setObjectName(u"check_PushButton")
        self.check_PushButton.setGeometry(QRect(290, 330, 61, 31))
        self.check_PushButton.setStyleSheet(u"image: url(:/icons/resources/check.png);")
        self.close_PushButton = QPushButton(Connections_Dialog)
        self.close_PushButton.setObjectName(u"close_PushButton")
        self.close_PushButton.setGeometry(QRect(180, 330, 61, 31))
        self.close_PushButton.setStyleSheet(u"image: url(:/icons/resources/close.png);")
        self.Connection_checkBox = QCheckBox(Connections_Dialog)
        self.Connection_checkBox.setObjectName(u"Connection_checkBox")
        self.Connection_checkBox.setGeometry(QRect(400, 120, 81, 31))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(14)
        font.setBold(True)
        self.Connection_checkBox.setFont(font)
        self.Connection_checkBox.setIconSize(QSize(20, 16))
        self.label = QLabel(Connections_Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 30, 211, 41))
        font1 = QFont()
        font1.setFamilies([u"Myanmar Text"])
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Connections_Dialog)

        QMetaObject.connectSlotsByName(Connections_Dialog)
    # setupUi

    def retranslateUi(self, Connections_Dialog):
        Connections_Dialog.setWindowTitle(QCoreApplication.translate("Connections_Dialog", u"Add Time Frame", None))
        self.check_PushButton.setText("")
        self.close_PushButton.setText("")
        self.Connection_checkBox.setText(QCoreApplication.translate("Connections_Dialog", u"[1,2]", None))
        self.label.setText(QCoreApplication.translate("Connections_Dialog", u"Start", None))
    # retranslateUi

