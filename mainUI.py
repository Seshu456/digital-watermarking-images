# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(686, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cover_img = QtWidgets.QTextEdit(self.centralwidget)
        self.cover_img.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.cover_img.setObjectName("cover_img")
        self.img_open = QtWidgets.QPushButton(self.centralwidget)
        self.img_open.setGeometry(QtCore.QRect(130, 30, 41, 21))
        self.img_open.setCheckable(False)
        self.img_open.setObjectName("img_open")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 61, 16))
        self.label.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 61, 16))
        self.label_2.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.message_img = QtWidgets.QTextEdit(self.centralwidget)
        self.message_img.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.message_img.setObjectName("message_img")
        self.message_open = QtWidgets.QPushButton(self.centralwidget)
        self.message_open.setGeometry(QtCore.QRect(130, 90, 41, 21))
        self.message_open.setObjectName("message_open")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_3.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 150, 61, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.DWT = QtWidgets.QPushButton(self.centralwidget)
        self.DWT.setGeometry(QtCore.QRect(10, 200, 41, 21))
        self.DWT.setObjectName("DWT")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 61, 16))
        self.label_4.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 10, 61, 16))
        self.label_5.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 10, 91, 16))
        self.label_7.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 170, 91, 16))
        self.label_8.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(400, 170, 71, 16))
        self.label_9.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 170, 81, 16))
        self.label_10.setStyleSheet("font: 75 9pt \"Adobe Gothic Std B\";\n"
"background-color: rgb(170, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.img2 = QtWidgets.QLabel(self.centralwidget)
        self.img2.setGeometry(QtCore.QRect(360, 30, 131, 121))
        self.img2.setText("")
        self.img2.setObjectName("img2")
        self.img3 = QtWidgets.QLabel(self.centralwidget)
        self.img3.setGeometry(QtCore.QRect(520, 30, 131, 121))
        self.img3.setText("")
        self.img3.setObjectName("img3")
        self.img4 = QtWidgets.QLabel(self.centralwidget)
        self.img4.setGeometry(QtCore.QRect(210, 190, 131, 121))
        self.img4.setText("")
        self.img4.setObjectName("img4")
        self.img5 = QtWidgets.QLabel(self.centralwidget)
        self.img5.setGeometry(QtCore.QRect(360, 190, 131, 121))
        self.img5.setText("")
        self.img5.setObjectName("img5")
        self.img6 = QtWidgets.QLabel(self.centralwidget)
        self.img6.setGeometry(QtCore.QRect(520, 190, 131, 121))
        self.img6.setText("")
        self.img6.setObjectName("img6")
        self.img1 = QtWidgets.QLabel(self.centralwidget)
        self.img1.setGeometry(QtCore.QRect(210, 30, 131, 121))
        self.img1.setText("")
        self.img1.setObjectName("img1")
        self.DCT = QtWidgets.QPushButton(self.centralwidget)
        self.DCT.setGeometry(QtCore.QRect(60, 200, 41, 21))
        self.DCT.setObjectName("DCT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_open.setText(_translate("MainWindow", "Browser"))
        self.label.setText(_translate("MainWindow", " Cover   Image"))
        self.label_2.setText(_translate("MainWindow", "Input Message"))
        self.message_open.setText(_translate("MainWindow", "Browser"))
        self.label_3.setText(_translate("MainWindow", "Choose Attack Method"))
        self.comboBox.setItemText(0, _translate("MainWindow", "白噪声"))
        self.comboBox.setItemText(1, _translate("MainWindow", "旋转10°"))
        self.comboBox.setItemText(2, _translate("MainWindow", "旋转30°"))
        self.comboBox.setItemText(3, _translate("MainWindow", "椒盐噪声"))
        self.comboBox.setItemText(4, _translate("MainWindow", "小波压缩"))
        self.DWT.setText(_translate("MainWindow", "DWT"))
        self.label_4.setText(_translate("MainWindow", " Cover   Image"))
        self.label_5.setText(_translate("MainWindow", "Input Message"))
        self.label_7.setText(_translate("MainWindow", "Watermarked   Image"))
        self.label_8.setText(_translate("MainWindow", "Recovered   Message"))
        self.label_9.setText(_translate("MainWindow", "Attacked  Image"))
        self.label_10.setText(_translate("MainWindow", "Attacked  Message"))
        self.DCT.setText(_translate("MainWindow", "DCT"))
