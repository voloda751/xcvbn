# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utel.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 251, 551))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 221, 51))
        self.label.setObjectName("label")
        self.list_1 = QtWidgets.QListWidget(self.centralwidget)
        self.list_1.setGeometry(QtCore.QRect(280, 50, 421, 161))
        self.list_1.setObjectName("list_1")
        self.btn_meke = QtWidgets.QPushButton(self.centralwidget)
        self.btn_meke.setGeometry(QtCore.QRect(280, 220, 171, 41))
        self.btn_meke.setObjectName("btn_meke")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(500, 220, 201, 41))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(320, 270, 341, 41))
        self.btn_save.setObjectName("btn_save")
        self.list_2 = QtWidgets.QListWidget(self.centralwidget)
        self.list_2.setGeometry(QtCore.QRect(290, 350, 391, 121))
        self.list_2.setObjectName("list_2")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(300, 580, 371, 41))
        self.btn_search.setObjectName("btn_search")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 310, 221, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(290, 530, 171, 41))
        self.btn_add.setObjectName("btn_add")
        self.btn_detach = QtWidgets.QPushButton(self.centralwidget)
        self.btn_detach.setGeometry(QtCore.QRect(510, 530, 171, 41))
        self.btn_detach.setObjectName("btn_detach")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 480, 391, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_search.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.list_1.raise_()
        self.btn_meke.raise_()
        self.btn_delete.raise_()
        self.btn_save.raise_()
        self.list_2.raise_()
        self.label_2.raise_()
        self.btn_add.raise_()
        self.btn_detach.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
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
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">Текст....</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Cписок заміток"))
        self.btn_meke.setText(_translate("MainWindow", "Створити замітку"))
        self.btn_delete.setText(_translate("MainWindow", "Видалити замітку"))
        self.btn_save.setText(_translate("MainWindow", "Зберегти замітку"))
        self.btn_search.setText(_translate("MainWindow", "Шукати замітку по тегу "))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.btn_add.setText(_translate("MainWindow", "Додати до замітки"))
        self.btn_detach.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.lineEdit.setText(_translate("MainWindow", "Ведіть тег....."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
