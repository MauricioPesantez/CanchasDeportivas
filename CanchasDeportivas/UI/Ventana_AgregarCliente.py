# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_agregarCliente.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_agregarCliente(object):
    def setupUi(self, agregarCliente):
        agregarCliente.setObjectName("agregarCliente")
        agregarCliente.resize(354, 291)
        self.label = QtWidgets.QLabel(agregarCliente)
        self.label.setGeometry(QtCore.QRect(0, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.aceptarBTN = QtWidgets.QPushButton(agregarCliente)
        self.aceptarBTN.setGeometry(QtCore.QRect(60, 230, 94, 30))
        self.aceptarBTN.setObjectName("aceptarBTN")
        self.label_5 = QtWidgets.QLabel(agregarCliente)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 65, 20))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(agregarCliente)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 65, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(agregarCliente)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 65, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(agregarCliente)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 65, 20))
        self.label_4.setObjectName("label_4")
        self.cancelarBTN = QtWidgets.QPushButton(agregarCliente)
        self.cancelarBTN.setGeometry(QtCore.QRect(210, 230, 94, 30))
        self.cancelarBTN.setObjectName("cancelarBTN")
        self.apellidoTXT = QtWidgets.QLineEdit(agregarCliente)
        self.apellidoTXT.setGeometry(QtCore.QRect(90, 100, 161, 32))
        self.apellidoTXT.setObjectName("apellidoTXT")
        self.edadTXT = QtWidgets.QLineEdit(agregarCliente)
        self.edadTXT.setGeometry(QtCore.QRect(90, 180, 161, 32))
        self.edadTXT.setObjectName("edadTXT")
        self.nombreTXT = QtWidgets.QLineEdit(agregarCliente)
        self.nombreTXT.setGeometry(QtCore.QRect(90, 60, 161, 32))
        self.nombreTXT.setObjectName("nombreTXT")
        self.cedulaTXT = QtWidgets.QLineEdit(agregarCliente)
        self.cedulaTXT.setGeometry(QtCore.QRect(90, 140, 161, 32))
        self.cedulaTXT.setObjectName("cedulaTXT")

        self.retranslateUi(agregarCliente)
        QtCore.QMetaObject.connectSlotsByName(agregarCliente)

    def retranslateUi(self, agregarCliente):
        _translate = QtCore.QCoreApplication.translate
        agregarCliente.setWindowTitle(_translate("agregarCliente", "Form"))
        self.label.setText(_translate("agregarCliente", "Agregar Cliente"))
        self.aceptarBTN.setText(_translate("agregarCliente", "Aceptar"))
        self.label_5.setText(_translate("agregarCliente", "Edad:"))
        self.label_2.setText(_translate("agregarCliente", "Nombre:"))
        self.label_3.setText(_translate("agregarCliente", "Apellido:"))
        self.label_4.setText(_translate("agregarCliente", "Cedula:"))
        self.cancelarBTN.setText(_translate("agregarCliente", "Cancelar"))

