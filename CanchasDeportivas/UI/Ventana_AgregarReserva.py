# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_agregarReserva.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_agregarReserva(object):
    def setupUi(self, agregarReserva):
        agregarReserva.setObjectName("agregarReserva")
        agregarReserva.resize(434, 316)
        self.label = QtWidgets.QLabel(agregarReserva)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fechaHoraTXT = QtWidgets.QDateTimeEdit(agregarReserva)
        self.fechaHoraTXT.setGeometry(QtCore.QRect(190, 50, 194, 32))
        self.fechaHoraTXT.setObjectName("fechaHoraTXT")
        self.label_2 = QtWidgets.QLabel(agregarReserva)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 181, 20))
        self.label_2.setObjectName("label_2")
        self.horaFInTXT = QtWidgets.QTimeEdit(agregarReserva)
        self.horaFInTXT.setGeometry(QtCore.QRect(190, 90, 118, 32))
        self.horaFInTXT.setObjectName("horaFInTXT")
        self.label_5 = QtWidgets.QLabel(agregarReserva)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(agregarReserva)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 71, 20))
        self.label_3.setObjectName("label_3")
        self.clienteIDTXT = QtWidgets.QLineEdit(agregarReserva)
        self.clienteIDTXT.setGeometry(QtCore.QRect(190, 130, 113, 32))
        self.clienteIDTXT.setObjectName("clienteIDTXT")
        self.ClienteCIBTN = QtWidgets.QPushButton(agregarReserva)
        self.ClienteCIBTN.setGeometry(QtCore.QRect(320, 130, 71, 30))
        self.ClienteCIBTN.setObjectName("ClienteCIBTN")
        self.label_4 = QtWidgets.QLabel(agregarReserva)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 71, 20))
        self.label_4.setObjectName("label_4")
        self.canchaIDTXT = QtWidgets.QLineEdit(agregarReserva)
        self.canchaIDTXT.setGeometry(QtCore.QRect(190, 200, 113, 32))
        self.canchaIDTXT.setObjectName("canchaIDTXT")
        self.canchaIDBTN = QtWidgets.QPushButton(agregarReserva)
        self.canchaIDBTN.setGeometry(QtCore.QRect(320, 200, 71, 30))
        self.canchaIDBTN.setObjectName("canchaIDBTN")
        self.aceptarBTN = QtWidgets.QPushButton(agregarReserva)
        self.aceptarBTN.setGeometry(QtCore.QRect(100, 280, 94, 30))
        self.aceptarBTN.setObjectName("aceptarBTN")
        self.cancelarBTN = QtWidgets.QPushButton(agregarReserva)
        self.cancelarBTN.setGeometry(QtCore.QRect(250, 280, 94, 30))
        self.cancelarBTN.setObjectName("cancelarBTN")
        self.label_6 = QtWidgets.QLabel(agregarReserva)
        self.label_6.setGeometry(QtCore.QRect(190, 170, 201, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(agregarReserva)
        self.label_7.setGeometry(QtCore.QRect(190, 240, 201, 20))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(agregarReserva)
        QtCore.QMetaObject.connectSlotsByName(agregarReserva)

    def retranslateUi(self, agregarReserva):
        _translate = QtCore.QCoreApplication.translate
        agregarReserva.setWindowTitle(_translate("agregarReserva", "Form"))
        self.label.setText(_translate("agregarReserva", "Realizar una reserva"))
        self.label_2.setText(_translate("agregarReserva", "Seleccione fecha y Hora:"))
        self.label_5.setText(_translate("agregarReserva", "Fecha de Fin:"))
        self.label_3.setText(_translate("agregarReserva", "Cliente CI:"))
        self.ClienteCIBTN.setText(_translate("agregarReserva", "Buscar"))
        self.label_4.setText(_translate("agregarReserva", "Cancha ID:"))
        self.canchaIDBTN.setText(_translate("agregarReserva", "Buscar"))
        self.aceptarBTN.setText(_translate("agregarReserva", "Aceptar"))
        self.cancelarBTN.setText(_translate("agregarReserva", "Cancelar"))
        self.label_6.setText(_translate("agregarReserva", "."))
        self.label_7.setText(_translate("agregarReserva", "."))

