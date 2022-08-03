# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import resources_rc
import icons_resources_rc

class Ui_ConfigWindow(object):
    def setupUi(self, ConfigWindow):
        if not ConfigWindow.objectName():
            ConfigWindow.setObjectName(u"ConfigWindow")
        ConfigWindow.setWindowModality(Qt.NonModal)
        ConfigWindow.resize(685, 489)
        ConfigWindow.setMinimumSize(QSize(685, 489))
        ConfigWindow.setMaximumSize(QSize(685, 489))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(12)
        font.setBold(True)
        ConfigWindow.setFont(font)
        ConfigWindow.setAutoFillBackground(False)
        ConfigWindow.setStyleSheet(u"background-image: url(:/newPrefix/MainBackground.jpg);")
        self.centralwidget = QWidget(ConfigWindow)
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
        self.SetJunction_PushBotton = QPushButton(self.centralwidget)
        self.SetJunction_PushBotton.setObjectName(u"SetJunction_PushBotton")
        self.SetJunction_PushBotton.setGeometry(QRect(240, 400, 201, 71))
        self.SetJunction_PushBotton.setFont(font)
        self.SetJunction_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.SetJunction_PushBotton.setFlat(False)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 140, 324, 211))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(151, 41))
        self.label_4.setMaximumSize(QSize(151, 41))
        font2 = QFont()
        font2.setFamilies([u"Myanmar Text"])
        font2.setPointSize(8)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.UnitRadius_lineEdit = QLineEdit(self.widget)
        self.UnitRadius_lineEdit.setObjectName(u"UnitRadius_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UnitRadius_lineEdit.sizePolicy().hasHeightForWidth())
        self.UnitRadius_lineEdit.setSizePolicy(sizePolicy)
        self.UnitRadius_lineEdit.setMinimumSize(QSize(151, 41))
        self.UnitRadius_lineEdit.setMaximumSize(QSize(151, 41))
        self.UnitRadius_lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.UnitRadius_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.UnitRadius_lineEdit)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(151, 41))
        self.label_5.setMaximumSize(QSize(151, 41))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.Arrive_lineEdit = QLineEdit(self.widget)
        self.Arrive_lineEdit.setObjectName(u"Arrive_lineEdit")
        sizePolicy.setHeightForWidth(self.Arrive_lineEdit.sizePolicy().hasHeightForWidth())
        self.Arrive_lineEdit.setSizePolicy(sizePolicy)
        self.Arrive_lineEdit.setMinimumSize(QSize(151, 41))
        self.Arrive_lineEdit.setMaximumSize(QSize(151, 41))
        self.Arrive_lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.Arrive_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.Arrive_lineEdit)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(151, 41))
        self.label_7.setMaximumSize(QSize(151, 41))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_7)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(151, 41))
        self.label_6.setMaximumSize(QSize(151, 41))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_6)

        self.UpperLimit_lineEdit = QLineEdit(self.widget)
        self.UpperLimit_lineEdit.setObjectName(u"UpperLimit_lineEdit")
        sizePolicy.setHeightForWidth(self.UpperLimit_lineEdit.sizePolicy().hasHeightForWidth())
        self.UpperLimit_lineEdit.setSizePolicy(sizePolicy)
        self.UpperLimit_lineEdit.setMinimumSize(QSize(151, 41))
        self.UpperLimit_lineEdit.setMaximumSize(QSize(151, 41))
        self.UpperLimit_lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.UpperLimit_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.UpperLimit_lineEdit)

        self.Departure_lineEdit = QLineEdit(self.widget)
        self.Departure_lineEdit.setObjectName(u"Departure_lineEdit")
        sizePolicy.setHeightForWidth(self.Departure_lineEdit.sizePolicy().hasHeightForWidth())
        self.Departure_lineEdit.setSizePolicy(sizePolicy)
        self.Departure_lineEdit.setMinimumSize(QSize(151, 41))
        self.Departure_lineEdit.setMaximumSize(QSize(151, 41))
        self.Departure_lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.Departure_lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Departure_lineEdit)

        self.TimeFrames_ListWidget = QListWidget(self.centralwidget)
        self.TimeFrames_ListWidget.setObjectName(u"TimeFrames_ListWidget")
        self.TimeFrames_ListWidget.setEnabled(True)
        self.TimeFrames_ListWidget.setGeometry(QRect(360, 140, 311, 151))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TimeFrames_ListWidget.sizePolicy().hasHeightForWidth())
        self.TimeFrames_ListWidget.setSizePolicy(sizePolicy1)
        self.TimeFrames_ListWidget.setFont(font)
        self.TimeFrames_ListWidget.setStyleSheet(u"QListWidget {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.TimeFrames_ListWidget.setResizeMode(QListView.Adjust)
        self.TimeFrames_ListWidget.setViewMode(QListView.ListMode)
        self.TimeFrames_ListWidget.setItemAlignment(Qt.AlignCenter)
        self.TimeFrames_ListWidget.setSortingEnabled(True)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(360, 300, 296, 43))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.removeSelected_PushBotton = QPushButton(self.widget1)
        self.removeSelected_PushBotton.setObjectName(u"removeSelected_PushBotton")
        self.removeSelected_PushBotton.setMinimumSize(QSize(141, 41))
        self.removeSelected_PushBotton.setMaximumSize(QSize(141, 41))
        font3 = QFont()
        font3.setFamilies([u"Myanmar Text"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.removeSelected_PushBotton.setFont(font3)
        self.removeSelected_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.removeSelected_PushBotton.setFlat(False)

        self.horizontalLayout.addWidget(self.removeSelected_PushBotton)

        self.AddTimeFrame_PushBotton = QPushButton(self.widget1)
        self.AddTimeFrame_PushBotton.setObjectName(u"AddTimeFrame_PushBotton")
        self.AddTimeFrame_PushBotton.setMinimumSize(QSize(141, 41))
        self.AddTimeFrame_PushBotton.setMaximumSize(QSize(141, 41))
        self.AddTimeFrame_PushBotton.setFont(font3)
        self.AddTimeFrame_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.AddTimeFrame_PushBotton.setFlat(False)

        self.horizontalLayout.addWidget(self.AddTimeFrame_PushBotton)

        ConfigWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ConfigWindow)
        self.removeSelected_PushBotton.clicked["bool"].connect(ConfigWindow.show)

        QMetaObject.connectSlotsByName(ConfigWindow)
    # setupUi

    def retranslateUi(self, ConfigWindow):
        ConfigWindow.setWindowTitle(QCoreApplication.translate("ConfigWindow", u"Configuration", None))
        self.ConfigurationTitle_Label.setText(QCoreApplication.translate("ConfigWindow", u"Configuration", None))
        self.SetJunction_PushBotton.setText(QCoreApplication.translate("ConfigWindow", u"Set Junction ", None))
        self.label_4.setText(QCoreApplication.translate("ConfigWindow", u"Unit radius", None))
        self.label_5.setText(QCoreApplication.translate("ConfigWindow", u"Arrive Threshold  ", None))
        self.label_7.setText(QCoreApplication.translate("ConfigWindow", u"System upper limit", None))
        self.label_6.setText(QCoreApplication.translate("ConfigWindow", u"Departure Threshold  ", None))
        self.removeSelected_PushBotton.setText(QCoreApplication.translate("ConfigWindow", u"Remove selected ", None))
        self.AddTimeFrame_PushBotton.setText(QCoreApplication.translate("ConfigWindow", u"Add time frame", None))
    # retranslateUi

