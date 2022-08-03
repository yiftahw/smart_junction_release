# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectTimeFrameDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QLabel,
    QListView, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)
import icons_resources_rc

class Ui_SelectTimeFrame_Dialog(object):
    def setupUi(self, SelectTimeFrame_Dialog):
        if not SelectTimeFrame_Dialog.objectName():
            SelectTimeFrame_Dialog.setObjectName(u"SelectTimeFrame_Dialog")
        SelectTimeFrame_Dialog.resize(582, 403)
        SelectTimeFrame_Dialog.setMinimumSize(QSize(582, 403))
        SelectTimeFrame_Dialog.setMaximumSize(QSize(582, 403))
        SelectTimeFrame_Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.977, y1:0.971455, x2:1, y2:1, stop:0.221591 rgba(106, 184, 226, 239), stop:1 rgba(255, 255, 255, 255));")
        SelectTimeFrame_Dialog.setLocale(QLocale(QLocale.English, QLocale.Israel))
        self.date_Label = QLabel(SelectTimeFrame_Dialog)
        self.date_Label.setObjectName(u"date_Label")
        self.date_Label.setGeometry(QRect(180, 20, 221, 51))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setBold(True)
        self.date_Label.setFont(font)
        self.date_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.date_Label.setAlignment(Qt.AlignCenter)
        self.TimeFrames_ListWidget = QListWidget(SelectTimeFrame_Dialog)
        self.TimeFrames_ListWidget.setObjectName(u"TimeFrames_ListWidget")
        self.TimeFrames_ListWidget.setEnabled(True)
        self.TimeFrames_ListWidget.setGeometry(QRect(130, 80, 321, 251))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeFrames_ListWidget.sizePolicy().hasHeightForWidth())
        self.TimeFrames_ListWidget.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Myanmar Text"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.TimeFrames_ListWidget.setFont(font1)
        self.TimeFrames_ListWidget.setStyleSheet(u"QListWidget {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.TimeFrames_ListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.TimeFrames_ListWidget.setResizeMode(QListView.Adjust)
        self.TimeFrames_ListWidget.setViewMode(QListView.ListMode)
        self.TimeFrames_ListWidget.setItemAlignment(Qt.AlignCenter)
        self.TimeFrames_ListWidget.setSortingEnabled(True)
        self.selectTimeFrame_PushBotton = QPushButton(SelectTimeFrame_Dialog)
        self.selectTimeFrame_PushBotton.setObjectName(u"selectTimeFrame_PushBotton")
        self.selectTimeFrame_PushBotton.setGeometry(QRect(200, 340, 181, 51))
        self.selectTimeFrame_PushBotton.setFont(font1)
        self.selectTimeFrame_PushBotton.setStyleSheet(u"QPushButton {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.selectTimeFrame_PushBotton.setFlat(False)

        self.retranslateUi(SelectTimeFrame_Dialog)

        QMetaObject.connectSlotsByName(SelectTimeFrame_Dialog)
    # setupUi

    def retranslateUi(self, SelectTimeFrame_Dialog):
        SelectTimeFrame_Dialog.setWindowTitle(QCoreApplication.translate("SelectTimeFrame_Dialog", u"Select Time Frame", None))
        self.date_Label.setText(QCoreApplication.translate("SelectTimeFrame_Dialog", u"06-05-22", None))
        self.selectTimeFrame_PushBotton.setText(QCoreApplication.translate("SelectTimeFrame_Dialog", u"Select time frames", None))
    # retranslateUi

