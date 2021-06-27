import os
import ONLINE
import time
import schedule
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog



class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.monit = QtWidgets.QPushButton(self.centralwidget)
        self.monit.setGeometry(QtCore.QRect(20, 140, 121, 23))
        self.monit.setObjectName("monit")
        self.plot_display = QtWidgets.QLabel(self.centralwidget)
        self.plot_display.setGeometry(QtCore.QRect(20, 180, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plot_display.setFont(font)
        self.plot_display.setStyleSheet("")
        self.plot_display.setObjectName("plot_display")
        self.dir_final = QtWidgets.QPushButton(self.centralwidget)
        self.dir_final.setGeometry(QtCore.QRect(300, 80, 261, 31))
        self.dir_final.setObjectName("dir_final")
        self.dir_png = QtWidgets.QPushButton(self.centralwidget)
        self.dir_png.setGeometry(QtCore.QRect(300, 30, 261, 31))
        self.dir_png.setObjectName("dir_png")
        self.do_stats = QtWidgets.QCheckBox(self.centralwidget)
        self.do_stats.setEnabled(True)
        self.do_stats.setGeometry(QtCore.QRect(20, 50, 171, 31))
        self.do_stats.setAcceptDrops(False)
        self.do_stats.setAutoFillBackground(False)
        self.do_stats.setChecked(True)
        self.do_stats.setTristate(False)
        self.do_stats.setObjectName("do_stats")
        self.dir_stats = QtWidgets.QPushButton(self.centralwidget)
        self.dir_stats.setGeometry(QtCore.QRect(20, 90, 171, 31))
        self.dir_stats.setObjectName("dir_stats")
        self.URL_adr = QtWidgets.QLineEdit(self.centralwidget)
        self.URL_adr.setGeometry(QtCore.QRect(20, 19, 191, 21))
        self.URL_adr.setObjectName("URL_adr")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 0, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(360, 150, 201, 23))
        self.start_button.setObjectName("start_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.in_dir = os.getcwd() + "\\"
        self.from_dir = os.getcwd() + "\\"
        self.stats_dir = os.getcwd() + "\\"

        self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)

        self.dir_png.clicked.connect(self.showdialog_for_from_dir)
        self.dir_stats.clicked.connect(self.showdialog_for_stat_dir)
        self.dir_final.clicked.connect(self.showdialog_for_in_dir)
        self.start_button.clicked.connect(self.do_chek)
        self.monit.clicked.connect(self.start_th_monit)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "сейсмограммы"))
        self.monit.setText(_translate("MainWindow", "Начать мониторинг"))
        self.plot_display.setText(_translate("MainWindow", "0.0000"))
        self.dir_final.setText(_translate("MainWindow", "Выберите папку для сохранения"))
        self.dir_png.setText(_translate("MainWindow", "Выберите папку с png файлами"))
        self.do_stats.setText(_translate("MainWindow", "Сохранение в excel"))
        self.dir_stats.setText(_translate("MainWindow", "Папка для статистики"))
        self.URL_adr.setText(_translate("MainWindow", "http://emsd.ru/~ddv/smkshe.png"))
        self.start_button.setText(_translate("MainWindow", "Провести исследование файла"))


    def showdialog_for_stat_dir(self):
        p = r'Выберите папку'
        p2 = self.stats_dir
        dir = QFileDialog.getExistingDirectory(self, p, p2)
        if dir:
            self.stats_dir = dir + "\\"

    def showdialog_for_from_dir(self):
        p = r'Выберите папку'
        p2 = self.from_dir
        dir = QFileDialog.getExistingDirectory(self, p, p2)
        if dir:
            self.from_dir = dir + "\\"

    def showdialog_for_in_dir(self):
        p = r'Выберите папку'
        p2 = self.in_dir
        dir = QFileDialog.getExistingDirectory(self, p, p2)
        print(dir)
        if dir:
            self.in_dir = dir + "\\"

    def start_th_monit(self):
        th2 = threading.Thread(target=self.start_cikl_monit)
        th2.start()

    def start_cikl_monit(self):
        self.plot_display.setText(ONLINE.online(self.URL_adr.text(), self.stats_dir, bool(self.do_stats.sender())))
        schedule.every(10).minutes.do(self.start_monit)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_monit(self):
        self.plot_display.setText(ONLINE.online(self.URL_adr.text(), self.stats_dir, bool(self.do_stats.sender())))

    def do_chek(self):
        th1 = threading.Thread(target=ONLINE.main, args=(self.from_dir, self.in_dir))
        th1.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
