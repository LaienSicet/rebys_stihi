from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 10, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 130, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 360, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 490, 420, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 85, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(440, 120, 25, 25))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 530, 460, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 590, 230, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 650, 270, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(305, 600, 190, 85))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.label_9 = QtWidgets.QLabel(self.centralwidget)  #
        self.label_9.setGeometry(QtCore.QRect(375, 685, 180, 20))  #
        font = QtGui.QFont()  #
        font.setFamily("Segoe Script")
        font.setPointSize(7)  #
        self.label_9.setFont(font)
        font.setFamily("Segoe Script")
        self.label_9.setObjectName("label")  #

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "имя свитка:"))
        self.pushButton.setText(_translate("MainWindow", "открыть"))
        self.label_2.setText(_translate("MainWindow", "*тех инфа.....................................................*"))
        self.label_3.setText(_translate("MainWindow", "сохранять"))
        self.label_4.setText(_translate("MainWindow", "*строка - подсказка*"))
        self.label_5.setText(_translate("MainWindow", "последнее слово \n(без знаков препинания):"))
        self.pushButton_2.setText(_translate("MainWindow", "проверить"))
        self.label_9.setText(_translate("MainWindow", "разработчик: Тарасов Д. Л."))  ########



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
