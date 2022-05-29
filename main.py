import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon

from PyQt5 import QtCore, QtGui, QtWidgets
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  QAbstractTableModel, QVariant, Qt

class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(935, 654)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(991, 681))
        MainWindow.setBaseSize(QtCore.QSize(991, 681))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 0, 20, 671))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.findPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.findPushButton.setGeometry(QtCore.QRect(20, 510, 331, 111))
        self.findPushButton.setObjectName("findPushButton")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 350, 331, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.namesLabel = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.namesLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.namesLabel.setFont(font)
        self.namesLabel.setObjectName("namesLabel")
        self.verticalLayout_4.addWidget(self.namesLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.isTypeChanged = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.isTypeChanged.setObjectName("isTypeChanged")
        self.verticalLayout_3.addWidget(self.isTypeChanged)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 320, 971, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.infoLabel = QtWidgets.QTextBrowser(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(390, 20, 381, 51))
        self.infoLabel.setObjectName("infoLabel")
        self.fishGraphics = QtWidgets.QGraphicsView(self.centralwidget)
        self.fishGraphics.setGeometry(QtCore.QRect(390, 350, 521, 251))
        self.fishGraphics.setObjectName("fishGraphics")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 20, 361, 251))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.productText = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.productText.setObjectName("productText")
        self.horizontalLayout_5.addWidget(self.productText)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.catchText = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.catchText.setObjectName("catchText")
        self.horizontalLayout_7.addWidget(self.catchText)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ext1Text = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.ext1Text.setObjectName("ext1Text")
        self.horizontalLayout_2.addWidget(self.ext1Text)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ext2Text = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.ext2Text.setObjectName("ext2Text")
        self.horizontalLayout_8.addWidget(self.ext2Text)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_8.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(170, 290, 191, 31))
        self.loadButton.setObjectName("loadButton")
        self.fishTables = QtWidgets.QTableView(self.centralwidget)
        self.fishTables.setGeometry(QtCore.QRect(400, 120, 256, 192))
        self.fishTables.setObjectName("fishTables")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.findPushButton.setText(_translate("MainWindow", "Искать аномалии!"))
        self.namesLabel.setText(_translate("MainWindow", "Выберите аномалии для поиска:"))
        self.isTypeChanged.setText(_translate("MainWindow", "Подмена вида"))
        self.checkBox_2.setText(_translate("MainWindow", "Неправильная маркировка"))
        self.checkBox_3.setText(_translate("MainWindow", "....."))
        self.infoLabel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Выявлены отклонения в данных в виде разницы объема вылова и объема переработки. Обратите внимание на следующие записи:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Product"))
        self.label_3.setText(_translate("MainWindow", "Catch"))
        self.label_4.setText(_translate("MainWindow", "Ext1"))
        self.label_5.setText(_translate("MainWindow", "Ext2"))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "...."))
        self.pushButton_5.setText(_translate("MainWindow", "...."))
        self.loadButton.setText(_translate("MainWindow", "Загрузить"))

        self.infoLabel.setHidden(1)
        self.fishGraphics.setHidden(1)
        self.fishTables.setHidden(1)
        self.findPushButton.clicked.connect(self.showResults)

    def showResults(self):
        self.infoLabel.setHidden(0)
        self.fishGraphics.setHidden(0)

        self.fishTables.setColumnWidth(0, 250)
        self.fishTables.setColumnWidth(1, 100)
        self.fishTables.setColumnWidth(2, 350)
        self.fishTables.setHidden(0)


    def mergeTables(self):
        import pandas as pd
        pd.set_option('display.max_rows', 1000)
        pd.set_option('display.max_columns', 1000)
        from sklearn.ensemble import IsolationForest

        catch = pd.read_csv("catch.csv")
        product = pd.read_csv("product.csv")
        ext1 = pd.read_csv("Ext.csv")
        ext2 = pd.read_csv("Ext2.csv")

        catch_product = pd.merge(catch, product, how="outer", on=['id_ves', 'date'])
        catch_product['catch_volume'] = catch_product['catch_volume'].apply(lambda x: x * 1000)

        ext1_2 = pd.merge(ext1, ext2, how="outer", on=['id_vsd'])
        pd.options.display.float_format = '{:.0f}'.format

        catch_volume = catch_product[['catch_volume', 'id_fish', 'id_ves', 'id_own']]
        ext1_2_volume = ext1_2[['id_fish', 'volume', 'id_ves', 'id_own']]

        grouped_catch_volume = catch_volume.groupby(['id_ves', 'id_own', 'id_fish'])["catch_volume"].sum().reset_index()
        grouped_ext1_2_volume = ext1_2_volume.groupby(['id_ves', 'id_own', 'id_fish'])["volume"].sum().reset_index()
        grouped_volumes = pd.merge(grouped_catch_volume, grouped_ext1_2_volume, how="inner",
                                   on=['id_own', 'id_fish', 'id_ves'])
        grouped_volumes['volumes_diff'] = grouped_volumes['catch_volume'] - grouped_volumes['volume']

        grouped_volumes_iforest = grouped_volumes
        model = IsolationForest(n_estimators=110, max_samples='auto', contamination=float(0.25), max_features=1.0,
                                random_state=0)
        model.fit(grouped_volumes_iforest[['volumes_diff']])

        grouped_volumes_iforest['scores'] = model.decision_function(grouped_volumes_iforest[['volumes_diff']])
        grouped_volumes_iforest['anomaly'] = model.predict(grouped_volumes_iforest[['volumes_diff']])

        anomaly_if = grouped_volumes_iforest.loc[grouped_volumes_iforest['anomaly'] == -1]
        anomaly_index = list(anomaly_if.index)

        anomaly_if.id_own.unique()  # это владельцы
        anomaly_if.id_fish.unique()  # это айди рыбы


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
