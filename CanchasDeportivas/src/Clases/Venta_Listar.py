# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Venta_listar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_listado(object):
    def setupUi(self, listado):
        listado.setObjectName("listado")
        listado.resize(443, 421)
        self.label = QtWidgets.QLabel(listado)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.imprimir = QtWidgets.QLabel(listado)
        self.imprimir.setGeometry(QtCore.QRect(10, 40, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.imprimir.setFont(font)
        self.imprimir.setText("")
        self.imprimir.setObjectName("imprimir")
        self.tableWidget = QtWidgets.QTableWidget(listado)
        self.tableWidget.setGeometry(QtCore.QRect(0, 90, 431, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.listarBTN = QtWidgets.QPushButton(listado)
        self.listarBTN.setGeometry(QtCore.QRect(60, 380, 94, 30))
        self.listarBTN.setObjectName("listarBTN")
        self.cancelarBTN = QtWidgets.QPushButton(listado)
        self.cancelarBTN.setGeometry(QtCore.QRect(250, 380, 94, 30))
        self.cancelarBTN.setObjectName("cancelarBTN")

        self.retranslateUi(listado)
        QtCore.QMetaObject.connectSlotsByName(listado)

    def retranslateUi(self, listado):
        _translate = QtCore.QCoreApplication.translate
        listado.setWindowTitle(_translate("listado", "Form"))
        self.label.setText(_translate("listado", "Listado"))
        self.listarBTN.setText(_translate("listado", "Listar"))
        self.cancelarBTN.setText(_translate("listado", "Cancelar"))

