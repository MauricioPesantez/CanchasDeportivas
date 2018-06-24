# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_agregarJugador.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ingresarJugador(object):
    def setupUi(self, ingresarJugador):
        ingresarJugador.setObjectName("ingresarJugador")
        ingresarJugador.resize(364, 277)
        self.label = QtWidgets.QLabel(ingresarJugador)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ingresarJugador)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 65, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ingresarJugador)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 65, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ingresarJugador)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 65, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ingresarJugador)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 65, 20))
        self.label_5.setObjectName("label_5")
        self.aceptarBTN = QtWidgets.QPushButton(ingresarJugador)
        self.aceptarBTN.setGeometry(QtCore.QRect(50, 230, 94, 30))
        self.aceptarBTN.setObjectName("aceptarBTN")
        self.cancelarBTN = QtWidgets.QPushButton(ingresarJugador)
        self.cancelarBTN.setGeometry(QtCore.QRect(200, 230, 94, 30))
        self.cancelarBTN.setObjectName("cancelarBTN")
        self.nombreTXT = QtWidgets.QLineEdit(ingresarJugador)
        self.nombreTXT.setGeometry(QtCore.QRect(80, 60, 161, 32))
        self.nombreTXT.setObjectName("nombreTXT")
        self.apellidoTXT = QtWidgets.QLineEdit(ingresarJugador)
        self.apellidoTXT.setGeometry(QtCore.QRect(80, 100, 161, 32))
        self.apellidoTXT.setObjectName("apellidoTXT")
        self.cedulaTXT = QtWidgets.QLineEdit(ingresarJugador)
        self.cedulaTXT.setGeometry(QtCore.QRect(80, 140, 161, 32))
        self.cedulaTXT.setObjectName("cedulaTXT")
        self.edadTXT = QtWidgets.QLineEdit(ingresarJugador)
        self.edadTXT.setGeometry(QtCore.QRect(80, 180, 161, 32))
        self.edadTXT.setObjectName("edadTXT")

        self.retranslateUi(ingresarJugador)
        QtCore.QMetaObject.connectSlotsByName(ingresarJugador)

    def retranslateUi(self, ingresarJugador):
        _translate = QtCore.QCoreApplication.translate
        ingresarJugador.setWindowTitle(_translate("ingresarJugador", "Form"))
        self.label.setText(_translate("ingresarJugador", "Agregar Jugador"))
        self.label_2.setText(_translate("ingresarJugador", "Nombre:"))
        self.label_3.setText(_translate("ingresarJugador", "Apellido:"))
        self.label_4.setText(_translate("ingresarJugador", "Cedula:"))
        self.label_5.setText(_translate("ingresarJugador", "Edad:"))
        self.aceptarBTN.setText(_translate("ingresarJugador", "Aceptar"))
        self.cancelarBTN.setText(_translate("ingresarJugador", "Cancelar"))

