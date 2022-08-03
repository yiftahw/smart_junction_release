# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UnitDataDialog.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import icons_resources_rc

class Ui_UnitData_Dialog(object):
    def setupUi(self, UnitData_Dialog):
        if not UnitData_Dialog.objectName():
            UnitData_Dialog.setObjectName(u"UnitData_Dialog")
        UnitData_Dialog.resize(512, 259)
        UnitData_Dialog.setMinimumSize(QSize(512, 259))
        UnitData_Dialog.setMaximumSize(QSize(512, 259))
        UnitData_Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.977, y1:0.971455, x2:1, y2:1, stop:0.221591 rgba(106, 184, 226, 239), stop:1 rgba(255, 255, 255, 255));")
        UnitData_Dialog.setLocale(QLocale(QLocale.English, QLocale.Israel))
        self.widget = QWidget(UnitData_Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 30, 411, 141))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.UnitMode_Label = QLabel(self.widget)
        self.UnitMode_Label.setObjectName(u"UnitMode_Label")
        self.UnitMode_Label.setMinimumSize(QSize(151, 41))
        self.UnitMode_Label.setMaximumSize(QSize(151, 41))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setBold(True)
        self.UnitMode_Label.setFont(font)
        self.UnitMode_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.UnitMode_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.UnitMode_Label, 0, 0, 1, 1)

        self.UnitNumber_Label = QLabel(self.widget)
        self.UnitNumber_Label.setObjectName(u"UnitNumber_Label")
        self.UnitNumber_Label.setMinimumSize(QSize(151, 41))
        self.UnitNumber_Label.setMaximumSize(QSize(151, 41))
        self.UnitNumber_Label.setFont(font)
        self.UnitNumber_Label.setStyleSheet(u"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}")
        self.UnitNumber_Label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.UnitNumber_Label, 0, 1, 1, 1)

        self.UnitMode_ComboBox = QComboBox(self.widget)
        self.UnitMode_ComboBox.addItem("")
        self.UnitMode_ComboBox.addItem("")
        self.UnitMode_ComboBox.setObjectName(u"UnitMode_ComboBox")
        self.UnitMode_ComboBox.setMinimumSize(QSize(151, 41))
        self.UnitMode_ComboBox.setMaximumSize(QSize(151, 41))
        self.UnitMode_ComboBox.setStyleSheet(u"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"background:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5, stop:0.272727 rgba(128, 191, 197, 186), stop:1 rgba(255, 255, 255, 255));\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: right;\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.UnitMode_ComboBox, 1, 0, 1, 1)

        self.UnitNumber_SpinBox = QSpinBox(self.widget)
        self.UnitNumber_SpinBox.setObjectName(u"UnitNumber_SpinBox")
        self.UnitNumber_SpinBox.setMinimumSize(QSize(151, 41))
        self.UnitNumber_SpinBox.setMaximumSize(QSize(151, 41))
        self.UnitNumber_SpinBox.setFont(font)
        self.UnitNumber_SpinBox.setStyleSheet(u"QSpinBox{\n"
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
        self.UnitNumber_SpinBox.setAlignment(Qt.AlignCenter)
        self.UnitNumber_SpinBox.setReadOnly(False)
        self.UnitNumber_SpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)

        self.gridLayout.addWidget(self.UnitNumber_SpinBox, 1, 1, 1, 1)

        self.widget1 = QWidget(UnitData_Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(120, 200, 281, 43))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.close_PushButton = QPushButton(self.widget1)
        self.close_PushButton.setObjectName(u"close_PushButton")
        self.close_PushButton.setMinimumSize(QSize(61, 41))
        self.close_PushButton.setMaximumSize(QSize(61, 41))
        self.close_PushButton.setStyleSheet(u"image: url(:/icons/resources/close.png);")

        self.gridLayout_2.addWidget(self.close_PushButton, 0, 1, 1, 1)

        self.check_PushButton = QPushButton(self.widget1)
        self.check_PushButton.setObjectName(u"check_PushButton")
        self.check_PushButton.setMinimumSize(QSize(61, 41))
        self.check_PushButton.setMaximumSize(QSize(61, 41))
        self.check_PushButton.setStyleSheet(u"image: url(:/icons/resources/check.png);")

        self.gridLayout_2.addWidget(self.check_PushButton, 0, 0, 1, 1)


        self.retranslateUi(UnitData_Dialog)

        QMetaObject.connectSlotsByName(UnitData_Dialog)
    # setupUi

    def retranslateUi(self, UnitData_Dialog):
        UnitData_Dialog.setWindowTitle(QCoreApplication.translate("UnitData_Dialog", u"Unit Data", None))
        self.UnitMode_Label.setText(QCoreApplication.translate("UnitData_Dialog", u"Unit mode", None))
        self.UnitNumber_Label.setText(QCoreApplication.translate("UnitData_Dialog", u"Unit number", None))
        self.UnitMode_ComboBox.setItemText(0, QCoreApplication.translate("UnitData_Dialog", u"disable ", None))
        self.UnitMode_ComboBox.setItemText(1, QCoreApplication.translate("UnitData_Dialog", u"enable", None))

        self.close_PushButton.setText("")
        self.check_PushButton.setText("")
    # retranslateUi

