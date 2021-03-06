# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj_disp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import ONLINE
import time
import schedule#pip install schedule
import threading
import sys
#для преобразования в .exe файл прописать в командной строке pyinstaller proj_disp.py -F

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog



class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.monit = QtWidgets.QPushButton(self.centralwidget)
        self.monit.setGeometry(QtCore.QRect(20, 150, 150, 30))
        self.monit.setObjectName("monit")
        self.plot_display = QtWidgets.QLabel(self.centralwidget)
        self.plot_display.setGeometry(QtCore.QRect(20, 190, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plot_display.setFont(font)
        self.plot_display.setStyleSheet("")
        self.plot_display.setObjectName("plot_display")
        self.dir_final = QtWidgets.QPushButton(self.centralwidget)
        self.dir_final.setGeometry(QtCore.QRect(260, 130, 260, 30))
        self.dir_final.setObjectName("dir_final")
        self.dir_png = QtWidgets.QPushButton(self.centralwidget)
        self.dir_png.setGeometry(QtCore.QRect(260, 40, 260, 30))
        self.dir_png.setObjectName("dir_png")
        self.do_stats = QtWidgets.QCheckBox(self.centralwidget)
        self.do_stats.setEnabled(True)
        self.do_stats.setGeometry(QtCore.QRect(20, 40, 170, 30))
        self.do_stats.setAcceptDrops(False)
        self.do_stats.setAutoFillBackground(False)
        self.do_stats.setChecked(True)
        self.do_stats.setTristate(False)
        self.do_stats.setObjectName("do_stats")
        self.dir_stats = QtWidgets.QPushButton(self.centralwidget)
        self.dir_stats.setGeometry(QtCore.QRect(20, 110, 170, 30))
        self.dir_stats.setObjectName("dir_stats")
        self.URL_adr = QtWidgets.QLineEdit(self.centralwidget)
        self.URL_adr.setGeometry(QtCore.QRect(20, 9, 190, 25))
        self.URL_adr.setObjectName("URL_adr")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 0, 20, 300))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(320, 190, 200, 30))
        self.start_button.setObjectName("start_button")
        self.line_from = QtWidgets.QLineEdit(self.centralwidget)
        self.line_from.setGeometry(QtCore.QRect(260, 10, 250, 20))
        self.line_from.setObjectName("line_from")
        self.line_in = QtWidgets.QLineEdit(self.centralwidget)
        self.line_in.setGeometry(QtCore.QRect(260, 100, 250, 20))
        self.line_in.setObjectName("line_in")
        self.line_stat = QtWidgets.QLineEdit(self.centralwidget)
        self.line_stat.setGeometry(QtCore.QRect(20, 80, 190, 20))
        self.line_stat.setObjectName("line_stat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.stop_monit = QtWidgets.QPushButton(self.centralwidget)
        self.stop_monit.setGeometry(QtCore.QRect(130, 200, 100, 40))
        self.stop_monit.setObjectName("stop_monit")
        self.proj_exit_bot = QtWidgets.QPushButton(self.centralwidget)
        self.proj_exit_bot.setGeometry(QtCore.QRect(420, 240, 100, 30))
        self.proj_exit_bot.setObjectName("proj_exit_bot")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)


        self.dir_png.clicked.connect(self.showdialog_for_line_from)
        self.dir_stats.clicked.connect(self.showdialog_for_line_stat)
        self.dir_final.clicked.connect(self.showdialog_for_line_in)
        self.start_button.clicked.connect(self.do_chek)
        self.monit.clicked.connect(self.start_th_monit)
        self.stop_monit.clicked.connect(lambda: self.stop_monit.setText("Завершение..."))
        self.proj_exit_bot.clicked.connect(self.init_proj_exit)



    def retranslateUi(self, MainWindow):
        my_plase = os.getcwd() + "\\"
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Оптическая плотность сейсмограмм"))
        self.monit.setText(_translate("MainWindow", "Начать мониторинг"))
        self.plot_display.setText(_translate("MainWindow", "0.0000"))
        self.dir_final.setText(_translate("MainWindow", "Выберите папку для сохранения"))
        self.dir_png.setText(_translate("MainWindow", "Выберите папку с png файлами"))
        self.do_stats.setText(_translate("MainWindow", "Сохранение в excel"))
        self.dir_stats.setText(_translate("MainWindow", "Папка для статистики"))
        self.URL_adr.setText(_translate("MainWindow", "http://emsd.ru/~ddv/smkshe.png"))
        self.start_button.setText(_translate("MainWindow", "Провести исследование файла"))
        self.line_in.setText(_translate("MainWindow", my_plase))
        self.line_from.setText(_translate("MainWindow", my_plase))
        self.line_stat.setText(_translate("MainWindow", my_plase))
        self.stop_monit.setText(_translate("MainWindow", "Завершить\nмониторинг"))
        self.proj_exit_bot.setText(_translate("MainWindow", "Выход"))


    def showdialog_for_line_stat(self):
        p = r'Выберите папку'
        p2 = self.line_stat.text()
        dir = QFileDialog.getExistingDirectory(self, p, p2)
        if dir:
            self.line_stat.setText(dir + "/")

    def showdialog_for_line_from(self):
        p = r'Выберите папку'
        p2 = self.line_from.text()
        dir = QFileDialog.getExistingDirectory(self, p, p2)
        if dir:
            self.line_from.setText(dir + "/")

    def showdialog_for_line_in(self):
        p = r'Выберите папку'
        p2 = self.line_in.text()
        dir = QFileDialog.getExistingDirectory(self, p, p2)
        print(dir)
        if dir:
            self.line_in.setText(dir + "/")

    def start_th_monit(self):
        if self.monit.text() == "Начать мониторинг":
            th2 = threading.Thread(target=self.start_cikl_monit)
            th2.start()
            self.monit.setText("Мониторинг запущен...")

    def start_cikl_monit(self):
        URL_adr = self.URL_adr.text()
        line_stat = self.line_stat.text()
        do_stats = bool(self.do_stats.isChecked())
        ONLINE.all_monit(URL_adr, line_stat)
        self.plot_display.setText(ONLINE.online(URL_adr, line_stat, do_stats))

        schedule.every(10).minutes.do(self.start_monit, URL_adr, line_stat, do_stats).tag("monit")
        schedule.every(12).hours.do(ONLINE.all_monit, URL_adr, line_stat).tag("monit")
        while True:
            schedule.run_pending()
            time.sleep(1)
            if self.stop_monit.text() == "Завершение...":
                schedule.clear("monit")
                self.stop_monit.setText("Завершить\nмониторинг")
                self.monit.setText("Начать мониторинг")
                break

    def init_proj_exit(self):
        th3 = threading.Thread(target=self.proj_exit)
        th3.start()
        pass

    def proj_exit(self):
        if self.monit.text() == "Начать мониторинг":
            print("Проект - Оптическая плотность сейсмограмм\nСтудент 2 курса Луков Виталий\nДВФУ, кафедра - Информатика и математическое моделирование,\nнаправление - Прикладная математика и информатика, специальность - системное програмирование\n\nКозырев Иван\nКамчатская Вулканологическая станция им. Ф. Ю. Левинсона-Лессинга   ИВиС ДВО РАН")
            sys.exit(app.exec())
        self.proj_exit_bot.setText("Выход...")
        self.stop_monit.setText("Завершение...")
        while True:
            if self.monit.text() == "Начать мониторинг":
                print("Проект - Оптическая плотность сейсмограмм\nСтудент 2 курса Луков Виталий\nДВФУ, кафедра - Информатика и математическое моделирование,\nнаправление - Прикладная математика и информатика, специальность - системное програмирование\n\nКозырев Иван\nКамчатская Вулканологическая станция им. Ф. Ю. Левинсона-Лессинга   ИВиС ДВО РАН")
                sys.exit(app.exec())
                break
            time.sleep(1)

    def start_monit(self, URL_adr, line_stat, do_stats):
        self.plot_display.setText(ONLINE.online(URL_adr, line_stat, do_stats))

    def do_chek(self):
        line_from = self.line_from.text()
        line_in = self.line_in.text()
        th1 = threading.Thread(target=ONLINE.main, args=(line_from, line_in))
        th1.start()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
