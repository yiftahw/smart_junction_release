# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QFrame,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resources_rc
import icons_resources_rc

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.setWindowModality(Qt.NonModal)
        AdminWindow.resize(685, 489)
        AdminWindow.setMinimumSize(QSize(685, 489))
        AdminWindow.setMaximumSize(QSize(685, 489))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(12)
        font.setBold(True)
        AdminWindow.setFont(font)
        AdminWindow.setAutoFillBackground(False)
        AdminWindow.setStyleSheet(u"background-image: url(:/newPrefix/MainBackground.jpg);")
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.AdminTitle_Label = QLabel(self.centralwidget)
        self.AdminTitle_Label.setObjectName(u"AdminTitle_Label")
        self.AdminTitle_Label.setGeometry(QRect(200, 30, 291, 71))
        font1 = QFont()
        font1.setFamilies([u"Eras Bold ITC"])
        font1.setPointSize(24)
        self.AdminTitle_Label.setFont(font1)
        self.AdminTitle_Label.setAutoFillBackground(False)
        self.AdminTitle_Label.setStyleSheet(u"background: transparent;\n"
"text-color: qconicalgradient(cx:0.477273, cy:0.494318, angle:20.6, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 33px;")
        self.AdminTitle_Label.setFrameShadow(QFrame.Plain)
        self.AdminTitle_Label.setScaledContents(False)
        self.AdminTitle_Label.setAlignment(Qt.AlignCenter)
        self.AdminTitle_Label.setOpenExternalLinks(False)
        self.close_PushButton = QPushButton(self.centralwidget)
        self.close_PushButton.setObjectName(u"close_PushButton")
        self.close_PushButton.setGeometry(QRect(230, 410, 91, 61))
        self.close_PushButton.setStyleSheet(u"QPushButton {\n"
"image: url(:/icons/resources/close.png);\n"
"color: rgb(0, 0, 0);\n"
"border: 3px solid #555;\n"
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
        self.check_PushButton = QPushButton(self.centralwidget)
        self.check_PushButton.setObjectName(u"check_PushButton")
        self.check_PushButton.setGeometry(QRect(350, 410, 91, 61))
        self.check_PushButton.setStyleSheet(u"\n"
"\n"
"QPushButton {\n"
"image: url(:/icons/resources/check.png);\n"
"color: rgb(0, 0, 0);\n"
"border: 3px solid #555;\n"
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
        self.Units_ListWidget = QListWidget(self.centralwidget)
        icon = QIcon()
        icon.addFile(u":/icons/resources/dor.png", QSize(), QIcon.Normal, QIcon.Off)
        font2 = QFont()
        font2.setFamilies([u"Myanmar Text"])
        font2.setPointSize(8)
        font2.setBold(True)
        __qlistwidgetitem = QListWidgetItem(self.Units_ListWidget)
        __qlistwidgetitem.setFont(font2);
        __qlistwidgetitem.setIcon(icon);
        __qlistwidgetitem1 = QListWidgetItem(self.Units_ListWidget)
        __qlistwidgetitem1.setFont(font2);
        __qlistwidgetitem1.setIcon(icon);
        __qlistwidgetitem2 = QListWidgetItem(self.Units_ListWidget)
        __qlistwidgetitem2.setFont(font2);
        __qlistwidgetitem2.setIcon(icon);
        QListWidgetItem(self.Units_ListWidget)
        QListWidgetItem(self.Units_ListWidget)
        QListWidgetItem(self.Units_ListWidget)
        QListWidgetItem(self.Units_ListWidget)
        self.Units_ListWidget.setObjectName(u"Units_ListWidget")
        self.Units_ListWidget.setEnabled(True)
        self.Units_ListWidget.setGeometry(QRect(10, 110, 431, 181))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Units_ListWidget.sizePolicy().hasHeightForWidth())
        self.Units_ListWidget.setSizePolicy(sizePolicy)
        self.Units_ListWidget.setFont(font)
        self.Units_ListWidget.setLayoutDirection(Qt.LeftToRight)
        self.Units_ListWidget.setAutoFillBackground(False)
        self.Units_ListWidget.setStyleSheet(u"QListWidget {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"QScrollBar{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QScrollBar::handle\n"
"{\n"
"color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QScrollBar::handle::pressed{\n"
"background:  white\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 25px;\n"
"}\n"
"\n"
"QScrollBar:slider{\n"
"background: white;\n"
"}\n"
"\n"
"QScrollBar:add-page{\n"
"border: white\n"
""
                        "}\n"
"\n"
"QScrollBar:up-arrow:horizontal, QScrollBar::down-arrow {\n"
"width: 1px;\n"
"height: 1px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page {\n"
"    background: none;\n"
"}")
        self.Units_ListWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Units_ListWidget.setResizeMode(QListView.Adjust)
        self.Units_ListWidget.setViewMode(QListView.ListMode)
        self.Units_ListWidget.setItemAlignment(Qt.AlignCenter)
        self.Units_ListWidget.setSortingEnabled(False)
        self.buttonsFrame = QFrame(self.centralwidget)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 300, 431, 91))
        self.buttonsFrame.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 3px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.removeUnit_PushBotton = QPushButton(self.buttonsFrame)
        self.removeUnit_PushBotton.setObjectName(u"removeUnit_PushBotton")
        self.removeUnit_PushBotton.setGeometry(QRect(11, 21, 131, 45))
        self.removeUnit_PushBotton.setFont(font)
        self.removeUnit_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.removeUnit_PushBotton.setFlat(False)
        self.addUnit_PushBotton = QPushButton(self.buttonsFrame)
        self.addUnit_PushBotton.setObjectName(u"addUnit_PushBotton")
        self.addUnit_PushBotton.setGeometry(QRect(149, 21, 131, 45))
        self.addUnit_PushBotton.setFont(font)
        self.addUnit_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.addUnit_PushBotton.setFlat(False)
        self.editUnit_PushBotton = QPushButton(self.buttonsFrame)
        self.editUnit_PushBotton.setObjectName(u"editUnit_PushBotton")
        self.editUnit_PushBotton.setGeometry(QRect(288, 21, 131, 45))
        self.editUnit_PushBotton.setFont(font)
        self.editUnit_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.editUnit_PushBotton.setFlat(False)
        self.buttonsFrame_2 = QFrame(self.centralwidget)
        self.buttonsFrame_2.setObjectName(u"buttonsFrame_2")
        self.buttonsFrame_2.setGeometry(QRect(450, 110, 221, 131))
        self.buttonsFrame_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 3px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;")
        self.buttonsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_2.setFrameShadow(QFrame.Raised)
        self.StationsNumber_SpinBox = QSpinBox(self.buttonsFrame_2)
        self.StationsNumber_SpinBox.setObjectName(u"StationsNumber_SpinBox")
        self.StationsNumber_SpinBox.setGeometry(QRect(50, 70, 121, 41))
        font3 = QFont()
        font3.setFamilies([u"Myanmar Text"])
        font3.setBold(True)
        self.StationsNumber_SpinBox.setFont(font3)
        self.StationsNumber_SpinBox.setStyleSheet(u"QSpinBox{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"QSpinBox::down-button{\n"
"	image: url(:/icons/resources/minus.png);\n"
"    width: 35px;\n"
"	height : 30px;\n"
"	subcontrol-position: right;\n"
"\n"
"}\n"
"QSpinBox::up-button{\n"
"	image: url(:/icons/resources/plus.png);\n"
"    subcontrol-position: left;\n"
"    width: 35px;\n"
"	height : 30px;\n"
"}")
        self.StationsNumber_SpinBox.setAlignment(Qt.AlignCenter)
        self.StationsNumber_SpinBox.setReadOnly(False)
        self.StationsNumber_SpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.editTimeFrame_PushBotton = QPushButton(self.buttonsFrame_2)
        self.editTimeFrame_PushBotton.setObjectName(u"editTimeFrame_PushBotton")
        self.editTimeFrame_PushBotton.setGeometry(QRect(30, 20, 161, 41))
        self.editTimeFrame_PushBotton.setFont(font)
        self.editTimeFrame_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.editTimeFrame_PushBotton.setFlat(False)
        self.buttonsFrame_3 = QFrame(self.centralwidget)
        self.buttonsFrame_3.setObjectName(u"buttonsFrame_3")
        self.buttonsFrame_3.setGeometry(QRect(450, 250, 221, 131))
        self.buttonsFrame_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: 3px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;")
        self.buttonsFrame_3.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame_3.setFrameShadow(QFrame.Raised)
        self.setCluster_PushBotton = QPushButton(self.buttonsFrame_3)
        self.setCluster_PushBotton.setObjectName(u"setCluster_PushBotton")
        self.setCluster_PushBotton.setGeometry(QRect(30, 20, 161, 41))
        self.setCluster_PushBotton.setFont(font)
        self.setCluster_PushBotton.setStyleSheet(u"QPushButton {\n"
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
        self.setCluster_PushBotton.setFlat(False)
        self.cluster_lineEdit = QLineEdit(self.buttonsFrame_3)
        self.cluster_lineEdit.setObjectName(u"cluster_lineEdit")
        self.cluster_lineEdit.setGeometry(QRect(50, 70, 121, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cluster_lineEdit.sizePolicy().hasHeightForWidth())
        self.cluster_lineEdit.setSizePolicy(sizePolicy1)
        self.cluster_lineEdit.setMinimumSize(QSize(121, 41))
        self.cluster_lineEdit.setMaximumSize(QSize(121, 41))
        font4 = QFont()
        font4.setFamilies([u"Myanmar Text"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.cluster_lineEdit.setFont(font4)
        self.cluster_lineEdit.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.cluster_lineEdit.setAlignment(Qt.AlignCenter)
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        self.addUnit_PushBotton.clicked["bool"].connect(AdminWindow.show)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Admin", None))
        self.AdminTitle_Label.setText(QCoreApplication.translate("AdminWindow", u"Admin setup", None))
        self.close_PushButton.setText("")
        self.check_PushButton.setText("")

        __sortingEnabled = self.Units_ListWidget.isSortingEnabled()
        self.Units_ListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.Units_ListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("AdminWindow", u"Unit_1 : Probe\n"
"Time : 2022-04-26 10:27:31.432", None));
        ___qlistwidgetitem1 = self.Units_ListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("AdminWindow", u"Unit_2 : Probe\n"
"Time : 2022-04-26 10:27:31.432", None));
        ___qlistwidgetitem2 = self.Units_ListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("AdminWindow", u"Unit_3 : Data\n"
"Time : 2022-04-26 10:27:31.432", None));
        ___qlistwidgetitem3 = self.Units_ListWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("AdminWindow", u"Unit_3 : Data\n"
"Time : 2022-04-26 10:27:31.432", None));
        ___qlistwidgetitem4 = self.Units_ListWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("AdminWindow", u"Unit_3 : Data\n"
"Time : 2022-04-26 10:27:31.432", None));
        ___qlistwidgetitem5 = self.Units_ListWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("AdminWindow", u"Unit_3 : Data\n"
"Time : 2022-04-26 10:27:31.432", None));
        ___qlistwidgetitem6 = self.Units_ListWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("AdminWindow", u"Unit_3 : Data\n"
"Time : 2022-04-26 10:27:31.432", None));
        self.Units_ListWidget.setSortingEnabled(__sortingEnabled)

        self.removeUnit_PushBotton.setText(QCoreApplication.translate("AdminWindow", u"Remove Unit", None))
        self.addUnit_PushBotton.setText(QCoreApplication.translate("AdminWindow", u"Add Unit", None))
        self.editUnit_PushBotton.setText(QCoreApplication.translate("AdminWindow", u"Edit Unit", None))
        self.editTimeFrame_PushBotton.setText(QCoreApplication.translate("AdminWindow", u"set time frame", None))
        self.setCluster_PushBotton.setText(QCoreApplication.translate("AdminWindow", u"set cluster distance", None))
        self.cluster_lineEdit.setText(QCoreApplication.translate("AdminWindow", u"100", None))
    # retranslateUi

