import os
import sys
import pandas as pd
import json

from preprocessing import compile_clustered_log
from firestore_api import *
from Engine import StatesM

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pandasModel import PandasModel
from ui_SelectTimeFrameDialog import Ui_SelectTimeFrame_Dialog
from ui_addTimeFrameDialog import Ui_AddTimeFrame_Dialog
from ui_adminWindow import Ui_AdminWindow
from ui_configWindow import Ui_ConfigWindow
from ui_connectionsDialog import Ui_Connections_Dialog
from ui_dataFrameTable import Ui_DataFrameTableWindow
from ui_mainWindow import Ui_MainWindow
from ui_receiveDataWindow import Ui_DataWindow
from ui_unitDataDialog import Ui_UnitData_Dialog
from ui_WaitingDialog import Ui_Waiting_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configWin = ConfigWindow()
        self.dataWin = ReceiveDataWindow()
        self.adminWin = AdminWindow()
        self.ui.setupSystem_PushBotton.clicked.connect(self.toggle_configWin)
        self.ui.receiveData_PushBotton.clicked.connect(self.toggle_dataWin)
        self.ui.admin_PushBotton.clicked.connect(self.toggle_adminWin)

    def toggle_configWin(self, checked):
        self.configWin.setWindowLabes()
        if self.configWin.isVisible():
            self.configWin.hide()

        else:
            self.configWin.show()

    def toggle_dataWin(self, checked):
        if self.dataWin.isVisible():
            self.dataWin.hide()

        else:
            self.dataWin.show()

    def toggle_adminWin(self, checked):
        if self.adminWin.isVisible():
            self.adminWin.hide()

        else:
            self.adminWin.ui.Units_ListWidget.clear()
            self.adminWin.configData = get_config_data(self.adminWin.token)
            print(self.adminWin.configData)
            self.adminWin.setAdminView()
            self.adminWin.show()


class AdminWindow(QMainWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.token = json.load(open("ServiceAccountKey.json", "r"))
        self.configData = get_config_data(self.token)
        self.thresholds_data = get_thresholds_data(self.token)
        self.ui.addUnit_PushBotton.clicked.connect(self.addUnit)
        self.ui.removeUnit_PushBotton.clicked.connect(self.removeSelectedUnit)
        self.ui.editUnit_PushBotton.clicked.connect(self.editSelectedUnit)
        self.ui.editTimeFrame_PushBotton.clicked.connect(self.editTimeFrame)
        self.ui.setCluster_PushBotton.clicked.connect(self.setCluster)
        self.ui.check_PushButton.clicked.connect(self.saveAdmin)
        self.ui.close_PushButton.clicked.connect(self.cancelChangesInAdmin)

    def editTimeFrame(self):
        self.configData['timeframe_minutes'] = self.ui.StationsNumber_SpinBox.value()
        print(self.configData)

    def setCluster(self):
        self.thresholds_data['cluster_distance'] = int(self.ui.cluster_lineEdit.text())
        print(self.thresholds_data['cluster_distance'])

    def createUnitItem(self, unit_number: str, unit_type: str, time_stamp: str, error_msg: str):
        icon = QIcon()
        icon.addFile(u":/icons/resources/dor.png", QSize(), QIcon.Normal, QIcon.Off)
        font2 = QFont()
        font2.setFamilies([u"Myanmar Text"])
        font2.setPointSize(8)
        font2.setBold(True)
        item = QListWidgetItem(self.ui.Units_ListWidget)
        item.setFont(font2)
        item.setIcon(icon)
        item.setText(QCoreApplication.translate("AdminWindow", u"Unit_" + unit_number + " : " + unit_type + "\n"
                                                + "Time stamp : " + time_stamp + "\n" + "Error: " + error_msg, None))
        return item

    def setAdminView(self):
        self.ui.StationsNumber_SpinBox.setValue(int(self.configData['timeframe_minutes']))
        self.ui.cluster_lineEdit.setText(str(self.thresholds_data['cluster_distance']))
        for unitNumber in range(100):
            if 'unit' + str(unitNumber) in self.configData:
                unit_error_msg = 'NA'
                if 'unit' + str(unitNumber) + '_error' in self.configData:
                    unit_error_msg = self.configData['unit' + str(unitNumber) + '_error']
                    unit_error_msg = unit_error_msg.replace('\t\t', '\n')
                self.ui.Units_ListWidget.addItem(self.createUnitItem(str(unitNumber),
                                                                     self.configData['unit' + str(unitNumber)],
                                                                     self.configData[
                                                                         'unit' + str(unitNumber) + '_timestamp'],
                                                                     unit_error_msg))

    def removeSelectedUnit(self):
        unitNumber = ""
        timeStamp = ""
        listItems = self.ui.Units_ListWidget.selectedItems()
        if not listItems:
            return
        for item in listItems:
            textList = item.text().split()
            unit = textList[0].replace('_', "").lower()
            self.ui.Units_ListWidget.takeItem(self.ui.Units_ListWidget.row(item))
            del self.configData[unit]
            del self.configData[unit + '_timestamp']
            print(self.configData)

    def addUnit(self):
        unitNumber = ""
        timeStamp = ""
        unitMode = ""
        dialog = UnitDataDialog()
        dialog.exec()
        if dialog.receive_Data:
            unitNumber = dialog.ui.UnitNumber_SpinBox.text()
            unitMode = dialog.ui.UnitMode_ComboBox.currentText()
            self.ui.Units_ListWidget.addItem(self.createUnitItem(unitNumber, unitMode, '0000-00-00 00:00:00.000'))
            self.configData['unit' + unitNumber] = unitMode
            self.configData['unit' + unitNumber + '_timestamp'] = timeStamp[:-1]
        print(self.configData)

    def editSelectedUnit(self):
        listItems = self.ui.Units_ListWidget.selectedItems()
        if not listItems:
            return
        for item in listItems:
            textList = item.text().split()
            unit = textList[0].replace('_', "").lower()
            unitNumber = ""
            timeStamp = self.configData[unit + '_timestamp']
            unitMode = ""
            dialog = UnitDataDialog()
            dialog.exec()
            if dialog.receive_Data:
                unitNumber = dialog.ui.UnitNumber_SpinBox.text()
                unitMode = dialog.ui.UnitMode_ComboBox.currentText()
                item.setText(QCoreApplication.translate("AdminWindow", u"Unit_" + unitNumber + " : " + unitMode + "\n"
                                                        + "Time stamp : " + timeStamp, None))
                del self.configData[unit]
                del self.configData[unit + '_timestamp']
                self.configData['unit' + unitNumber] = unitMode
                self.configData['unit' + unitNumber + '_timestamp'] = timeStamp
            print(self.configData)

    def saveAdmin(self):
        upload_config_to_server(self.token, self.configData, False)
        upload_thresholds_to_server(self.token, self.thresholds_data, False)
        self.close()

    def cancelChangesInAdmin(self):
        self.configData = None
        self.close()


class ConfigWindow(QMainWindow):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.ui = Ui_ConfigWindow()
        self.ui.setupUi(self)
        self.token = json.load(open("ServiceAccountKey.json", "r"))
        self.thresholdData = None
        self.ui.AddTimeFrame_PushBotton.clicked.connect(self.openTimeFrameDialog)
        self.ui.removeSelected_PushBotton.clicked.connect(self.removeSelected)
        self.ui.SetJunction_PushBotton.clicked.connect(self.setThresholdParams)

    def removeSelected(self):
        listItems = self.ui.TimeFrames_ListWidget.selectedItems()
        if not listItems:
            return
        for item in listItems:
            self.ui.TimeFrames_ListWidget.takeItem(self.ui.TimeFrames_ListWidget.row(item))

    def openTimeFrameDialog(self):
        dialog = AddTimeFrameDialog()
        dialog.setModal(True)
        dialog.exec()
        if dialog.receive_Data:
            item = QListWidgetItem(dialog.ui.timeEdit.text() + ' - ' + dialog.ui.timeEdit_2.text())
            item.setTextAlignment(Qt.AlignCenter)
            self.ui.TimeFrames_ListWidget.addItem(item)

    def setThresholdParams(self):
        self.thresholdData['unit_radius'] = self.ui.UnitRadius_lineEdit.text()
        self.thresholdData['system_upper_limit'] = self.ui.UpperLimit_lineEdit.text()
        self.thresholdData['arrive'] = self.ui.Arrive_lineEdit.text()
        self.thresholdData['depart'] = self.ui.Departure_lineEdit.text()
        upload_thresholds_to_server(self.token, self.thresholdData)
        self.close()

    def setWindowLabes(self):
        self.thresholdData = get_thresholds_data(self.token)
        self.ui.UnitRadius_lineEdit.setText(str(self.thresholdData['unit_radius']))
        self.ui.UpperLimit_lineEdit.setText(str(self.thresholdData['system_upper_limit']))
        self.ui.Arrive_lineEdit.setText(str(self.thresholdData['arrive']))
        self.ui.Departure_lineEdit.setText(str(self.thresholdData['depart']))

class ReceiveDataWindow(QMainWindow):
    def __init__(self):
        super(ReceiveDataWindow, self).__init__()
        self.ui = Ui_DataWindow()
        self.ui.setupUi(self)
        self.ui.selectDate_PushBotton.clicked.connect(self.openSelectTimeFrameDialog)
        self.selectedTimeFrames = []
        self.selectedDate = ''
        self.availableDates = ''
        self.token = json.load(open("ServiceAccountKey.json", "r"))
        self.availableDates = get_dates(self.token)
        for date in self.availableDates:
            item_t = QListWidgetItem(date)
            item_t.setTextAlignment(Qt.AlignCenter)
            self.ui.dates_ListWidget.addItem(item_t)
        self.ui.dates_ListWidget.sortItems()
        self.ui.getData_PushBotton.clicked.connect(self.getData)
        self.dataFrameWin = DataFrameTableWindow()

    def toggle_dataFrameWin(self, checked):
        if self.dataFrameWin.isVisible():
            self.dataFrameWin.hide()
        else:
            self.dataFrameWin.show()

    def getData(self):
        data = {}
        for tf in self.selectedTimeFrames:
            # tf_c = self.getFromCache(str(self.selectedDate) + ' ' + str(tf))
            # if tf_c is not None:
            #     data[tf] = tf_c
            # else:
            data[tf] = get_data_from_date_timestamp(self.token, self.selectedDate, tf)
        merged_data = merge_logs(data)
        cluster_threshold = get_thresholds_data(self.token)['cluster_distance']
        preprocessed_data = compile_clustered_log(merged_data, cluster_threshold)  # NOT SORTED!
        self.dataFrameWin.processedData = preprocessed_data
        df = pd.DataFrame(preprocessed_data)
        self.dataFrameWin.setDF(df, self.selectedDate, self.ui.timeFrameSelected_Label.text())
        self.toggle_dataFrameWin(checked=True)

    # def getFromCache(self, tf: str):
    #     with open('Cache')

    def setSelected(self, listWidget):
        self.selectedTimeFrames = []
        listItems = listWidget.selectedItems()
        if not listItems:
            return
        print(len(listItems))
        for item in listItems:
            self.selectedTimeFrames.append(item.text())
            self.selectedTimeFrames.sort()
            self.ui.timeFrameSelected_Label.setText(self.selectedTimeFrames[0].split('_')[0]
                                                    + '-' + self.selectedTimeFrames[-1].split('_')[1])

    def openSelectTimeFrameDialog(self):
        self.selectedDate = self.ui.dates_ListWidget.selectedItems()[0].text()
        self.ui.dateSelected_Label.setText(self.selectedDate)
        dialog = SelectTimeFrameDialog(self.selectedDate, self.token)
        dialog.setModal(True)
        dialog.exec()
        if dialog.receiveData:
            self.setSelected(dialog.ui.TimeFrames_ListWidget)


class ConnectionsDialog(QDialog):
    def __init__(self):
        super(ConnectionsDialog, self).__init__()
        self.ui = Ui_Connections_Dialog()
        self.ui.setupUi(self)
        self.ui.check_PushButton.clicked.connect(self.acceptFrame)
        self.ui.close_PushButton.clicked.connect(self.closeDialog)
        self.receive_Data = False

    def acceptFrame(self):
        self.receive_Data = True
        self.close()

    def closeDialog(self):
        self.close()


class AddTimeFrameDialog(QDialog):
    def __init__(self):
        super(AddTimeFrameDialog, self).__init__()
        self.ui = Ui_AddTimeFrame_Dialog()
        self.ui.setupUi(self)
        self.ui.check_PushButton.clicked.connect(self.acceptFrame)
        self.ui.close_PushButton.clicked.connect(self.closeDialog)
        self.receive_Data = False

    def acceptFrame(self):
        self.receive_Data = True
        self.close()

    def closeDialog(self):
        self.close()


class SelectTimeFrameDialog(QDialog):
    def __init__(self, date: str, token):
        super(SelectTimeFrameDialog, self).__init__()
        self.ui = Ui_SelectTimeFrame_Dialog()
        self.ui.setupUi(self)
        self.ui.selectTimeFrame_PushBotton.clicked.connect(self.selectFrame)
        self.receiveData = False
        self.ui.date_Label.setText(date)
        self.token = token
        self.availableTimeFrames = ''
        self.availableTimeFrames = get_times_from_date(self.token, date)
        for tf in self.availableTimeFrames:
            item_t = QListWidgetItem(tf)
            item_t.setTextAlignment(Qt.AlignCenter)
            self.ui.TimeFrames_ListWidget.addItem(item_t)
        self.ui.TimeFrames_ListWidget.sortItems()

    def selectFrame(self):
        self.receiveData = True
        self.close()


class UnitDataDialog(QDialog):
    def __init__(self):
        super(UnitDataDialog, self).__init__()
        self.ui = Ui_UnitData_Dialog()
        self.ui.setupUi(self)
        self.ui.check_PushButton.clicked.connect(self.acceptUnit)
        self.ui.close_PushButton.clicked.connect(self.closeDialog)
        self.receive_Data = False

    def acceptUnit(self):
        self.receive_Data = True
        self.close()

    def closeDialog(self):
        self.close()


class WaitingDialog(QDialog):
    def __init__(self):
        super(WaitingDialog, self).__init__()
        self.ui = Ui_Waiting_Dialog()
        self.ui.setupUi(self)
        self.counter = 0
        self.maxVal = self.ui.progressBar.maximum()


class DataFrameTableWindow(QMainWindow):
    def __init__(self):
        super(DataFrameTableWindow, self).__init__()
        self.ui = Ui_DataFrameTableWindow()
        self.ui.setupUi(self)
        self.ui.export_PushBotton.clicked.connect(self.ExportPush)
        self.token = json.load(open("ServiceAccountKey.json", "r"))
        self.df = None
        self.processedData = None
        self.date = ''
        self.timeFrame = ''

    def ExportPush(self):
        print("Export")
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        my_dir = QFileDialog.getExistingDirectory(
            self,
            "Select folder",
            desktop,
            QFileDialog.ShowDirsOnly
        )
        if my_dir is None or my_dir == '':
            return
        print(my_dir)
        self.df.to_csv(os.path.join(my_dir, (self.date + '__' + self.timeFrame.replace(':', '-')
                                             + '__RawData' + '.csv')))
        with open(os.path.join(my_dir, 'processed_' + self.date + '.txt'), 'w') as f:
            for element in self.processedData:
                f.write(json.dumps(element))
                f.write('\n')
        StatesM.configData.set(get_thresholds_data(self.token))
        StatesM.analyze(my_dir, self.date, self.processedData)

    def setDF(self, df, date, timeFrame):
        self.df = df
        self.date = date
        self.timeFrame = timeFrame
        self.ui.tableView.setModel(PandasModel(df.head(1000)))
        self.ui.dateSelected_Label.setText(date)
        self.ui.timeFrameSelected_Label.setText(timeFrame)
        self.ui.tableView.setStyleSheet('color: rgb(0, 0, 0);\n border: 2px solid #555;\n border-radius: 20px;'
                                        '\nborder-style: outset;\nbackground:  qradialgradient(spread:pad, '
                                        'cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.5,'
                                        ' stop:0.272727 rgba(128, 191, 197, 186), '
                                        'stop:1 rgba(255, 255, 255, 255));')
        self.ui.tableView.resizeRowsToContents()
        self.ui.tableView.setLayoutDirection(Qt.RightToLeft)
        self.ui.tableView.style().pixelMetric(QStyle.PM_ScrollBarExtent)
        self.ui.tableView.frameWidth() * 2
        vwidth = self.ui.tableView.verticalHeader().width()
        hwidth = self.ui.tableView.horizontalHeader().length()
        swidth = self.ui.tableView.style().pixelMetric(QStyle.PM_ScrollBarExtent)
        fwidth = self.ui.tableView.frameWidth() * 2
        self.ui.tableView.setFixedWidth(vwidth + hwidth + swidth + fwidth)
        self.ui.tableView.verticalHeader().setDefaultAlignment(Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
