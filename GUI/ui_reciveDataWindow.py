# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reciveDataWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resources_rc
import icons_resources_rc

class Ui_DataWindow(object):
    def setupUi(self, DataWindow):
        if not DataWindow.objectName():
            DataWindow.setObjectName(u"DataWindow")
        DataWindow.setWindowModality(Qt.NonModal)
        DataWindow.resize(685, 489)
        DataWindow.setMinimumSize(QSize(685, 489))
        DataWindow.setMaximumSize(QSize(685, 489))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(12)
        font.setBold(True)
        DataWindow.setFont(font)
        DataWindow.setAutoFillBackground(False)
        DataWindow.setStyleSheet(u"background-image: url(:/newPrefix/MainBackground.jpg);")
        self.centralwidget = QWidget(DataWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.ConfigurationTitle_Label = QLabel(self.centralwidget)
        self.ConfigurationTitle_Label.setObjectName(u"ConfigurationTitle_Label")
        self.ConfigurationTitle_Label.setGeometry(QRect(200, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Eras Bold ITC"])
        font1.setPointSize(24)
        self.ConfigurationTitle_Label.setFont(font1)
        self.ConfigurationTitle_Label.setAutoFillBackground(False)
        self.ConfigurationTitle_Label.setStyleSheet(u"background: transparent;\n"
"text-color: qconicalgradient(cx:0.477273, cy:0.494318, angle:20.6, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 33px;")
        self.ConfigurationTitle_Label.setFrameShadow(QFrame.Plain)
        self.ConfigurationTitle_Label.setScaledContents(False)
        self.ConfigurationTitle_Label.setAlignment(Qt.AlignCenter)
        self.ConfigurationTitle_Label.setOpenExternalLinks(False)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(400, 120, 215, 341))
        self.TimeFrame_Layout = QGridLayout(self.gridLayoutWidget)
        self.TimeFrame_Layout.setObjectName(u"TimeFrame_Layout")
        self.TimeFrame_Layout.setContentsMargins(0, 0, 0, 0)
        self.dates_ListWidget = QListWidget(self.gridLayoutWidget)
        self.dates_ListWidget.setObjectName(u"dates_ListWidget")
        self.dates_ListWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dates_ListWidget.sizePolicy().hasHeightForWidth())
        self.dates_ListWidget.setSizePolicy(sizePolicy)
        self.dates_ListWidget.setMinimumSize(QSize(159, 192))
        self.dates_ListWidget.setFont(font)
        self.dates_ListWidget.setStyleSheet(u"QListWidget {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.dates_ListWidget.setResizeMode(QListView.Adjust)
        self.dates_ListWidget.setViewMode(QListView.ListMode)
        self.dates_ListWidget.setItemAlignment(Qt.AlignCenter)
        self.dates_ListWidget.setSortingEnabled(True)

        self.TimeFrame_Layout.addWidget(self.dates_ListWidget, 2, 0, 1, 1)

        self.selectDate_PushBotton = QPushButton(self.gridLayoutWidget)
        self.selectDate_PushBotton.setObjectName(u"selectDate_PushBotton")
        self.selectDate_PushBotton.setMinimumSize(QSize(159, 45))
        self.selectDate_PushBotton.setMaximumSize(QSize(159, 45))
        self.selectDate_PushBotton.setFont(font)
        self.selectDate_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.selectDate_PushBotton.setFlat(False)

        self.TimeFrame_Layout.addWidget(self.selectDate_PushBotton, 3, 0, 1, 1, Qt.AlignHCenter)

        self.date_Label = QLabel(self.centralwidget)
        self.date_Label.setObjectName(u"date_Label")
        self.date_Label.setGeometry(QRect(40, 150, 131, 41))
        font2 = QFont()
        font2.setFamilies([u"Myanmar Text"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.date_Label.setFont(font2)
        self.date_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.date_Label.setAlignment(Qt.AlignCenter)
        self.timeFrame_Label = QLabel(self.centralwidget)
        self.timeFrame_Label.setObjectName(u"timeFrame_Label")
        self.timeFrame_Label.setGeometry(QRect(40, 210, 131, 41))
        self.timeFrame_Label.setFont(font2)
        self.timeFrame_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.timeFrame_Label.setAlignment(Qt.AlignCenter)
        self.dateSelected_Label = QLabel(self.centralwidget)
        self.dateSelected_Label.setObjectName(u"dateSelected_Label")
        self.dateSelected_Label.setGeometry(QRect(190, 150, 131, 41))
        self.dateSelected_Label.setFont(font2)
        self.dateSelected_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.dateSelected_Label.setAlignment(Qt.AlignCenter)
        self.timeFrameSelected_Label = QLabel(self.centralwidget)
        self.timeFrameSelected_Label.setObjectName(u"timeFrameSelected_Label")
        self.timeFrameSelected_Label.setGeometry(QRect(190, 210, 131, 41))
        self.timeFrameSelected_Label.setFont(font2)
        self.timeFrameSelected_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.timeFrameSelected_Label.setAlignment(Qt.AlignCenter)
        self.getData_PushBotton = QPushButton(self.centralwidget)
        self.getData_PushBotton.setObjectName(u"getData_PushBotton")
        self.getData_PushBotton.setGeometry(QRect(80, 320, 201, 101))
        font3 = QFont()
        font3.setFamilies([u"Myanmar Text"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.getData_PushBotton.setFont(font3)
        self.getData_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.getData_PushBotton.setFlat(False)
        DataWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataWindow)
        self.selectDate_PushBotton.clicked["bool"].connect(DataWindow.show)

        QMetaObject.connectSlotsByName(DataWindow)
    # setupUi

    def retranslateUi(self, DataWindow):
        DataWindow.setWindowTitle(QCoreApplication.translate("DataWindow", u"ReciveData", None))
        self.ConfigurationTitle_Label.setText(QCoreApplication.translate("DataWindow", u"Junction Data", None))
        self.selectDate_PushBotton.setText(QCoreApplication.translate("DataWindow", u"Select date", None))
        self.date_Label.setText(QCoreApplication.translate("DataWindow", u"Date", None))
        self.timeFrame_Label.setText(QCoreApplication.translate("DataWindow", u"Time frame", None))
        self.dateSelected_Label.setText("")
        self.timeFrameSelected_Label.setText("")
        self.getData_PushBotton.setText(QCoreApplication.translate("DataWindow", u"Get data", None))
    # retranslateUi

