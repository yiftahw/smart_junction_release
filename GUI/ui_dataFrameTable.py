# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataFrameTable.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)
import resources_rc
import icons_resources_rc

class Ui_DataFrameTableWindow(object):
    def setupUi(self, DataFrameTableWindow):
        if not DataFrameTableWindow.objectName():
            DataFrameTableWindow.setObjectName(u"DataFrameTableWindow")
        DataFrameTableWindow.setWindowModality(Qt.NonModal)
        DataFrameTableWindow.resize(977, 650)
        DataFrameTableWindow.setMinimumSize(QSize(977, 650))
        DataFrameTableWindow.setMaximumSize(QSize(977, 650))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(12)
        font.setBold(True)
        DataFrameTableWindow.setFont(font)
        DataFrameTableWindow.setAutoFillBackground(False)
        DataFrameTableWindow.setStyleSheet(u"background-image: url(:/newPrefix/MainBackground.jpg);")
        self.centralwidget = QWidget(DataFrameTableWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.ConfigurationTitle_Label = QLabel(self.centralwidget)
        self.ConfigurationTitle_Label.setObjectName(u"ConfigurationTitle_Label")
        self.ConfigurationTitle_Label.setGeometry(QRect(350, 20, 291, 71))
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
        self.date_Label = QLabel(self.centralwidget)
        self.date_Label.setObjectName(u"date_Label")
        self.date_Label.setGeometry(QRect(710, 10, 111, 41))
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
        self.timeFrame_Label.setGeometry(QRect(710, 60, 111, 41))
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
        self.dateSelected_Label.setGeometry(QRect(840, 10, 131, 41))
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
        self.timeFrameSelected_Label.setGeometry(QRect(840, 60, 131, 41))
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
        self.export_PushBotton = QPushButton(self.centralwidget)
        self.export_PushBotton.setObjectName(u"export_PushBotton")
        self.export_PushBotton.setGeometry(QRect(800, 570, 141, 61))
        font3 = QFont()
        font3.setFamilies([u"Myanmar Text"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.export_PushBotton.setFont(font3)
        self.export_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.export_PushBotton.setFlat(False)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(25, 120, 711, 501))
        self.tableView.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"")
        DataFrameTableWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DataFrameTableWindow)

        QMetaObject.connectSlotsByName(DataFrameTableWindow)
    # setupUi

    def retranslateUi(self, DataFrameTableWindow):
        DataFrameTableWindow.setWindowTitle(QCoreApplication.translate("DataFrameTableWindow", u"DataTable", None))
        self.ConfigurationTitle_Label.setText(QCoreApplication.translate("DataFrameTableWindow", u"Data", None))
        self.date_Label.setText(QCoreApplication.translate("DataFrameTableWindow", u"Date", None))
        self.timeFrame_Label.setText(QCoreApplication.translate("DataFrameTableWindow", u"Time frame", None))
        self.dateSelected_Label.setText("")
        self.timeFrameSelected_Label.setText("")
        self.export_PushBotton.setText(QCoreApplication.translate("DataFrameTableWindow", u"Analyze", None))
    # retranslateUi

