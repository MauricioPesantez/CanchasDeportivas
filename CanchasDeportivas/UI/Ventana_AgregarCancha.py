# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_agregarCancha.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ingresarCancha(object):
    def setupUi(self, ingresarCancha):
        ingresarCancha.setObjectName("ingresarCancha")
        ingresarCancha.resize(340, 293)
        self.label = QtWidgets.QLabel(ingresarCancha)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ingresarCancha)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 65, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ingresarCancha)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 65, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ingresarCancha)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 65, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ingresarCancha)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 65, 20))
        self.label_5.setObjectName("label_5")
        self.nombreTXT = QtWidgets.QLineEdit(ingresarCancha)
        self.nombreTXT.setGeometry(QtCore.QRect(90, 80, 161, 32))
        self.nombreTXT.setObjectName("nombreTXT")
        self.valorTXT = QtWidgets.QLineEdit(ingresarCancha)
        self.valorTXT.setGeometry(QtCore.QRect(90, 160, 161, 32))
        self.valorTXT.setObjectName("valorTXT")
        self.direccionTXT = QtWidgets.QLineEdit(ingresarCancha)
        self.direccionTXT.setGeometry(QtCore.QRect(90, 120, 161, 32))
        self.direccionTXT.setObjectName("direccionTXT")
        self.codigoTXT = QtWidgets.QLineEdit(ingresarCancha)
        self.codigoTXT.setGeometry(QtCore.QRect(90, 40, 161, 32))
        self.codigoTXT.setObjectName("codigoTXT")
        self.cancelarBTN = QtWidgets.QPushButton(ingresarCancha)
        self.cancelarBTN.setGeometry(QtCore.QRect(180, 230, 94, 30))
        self.cancelarBTN.setObjectName("cancelarBTN")
        self.aceptarBTN = QtWidgets.QPushButton(ingresarCancha)
        self.aceptarBTN.setGeometry(QtCore.QRect(40, 230, 94, 30))
        self.aceptarBTN.setObjectName("aceptarBTN")

        self.retranslateUi(ingresarCancha)
        QtCore.QMetaObject.connectSlotsByName(ingresarCancha)

    def retranslateUi(self, ingresarCancha):
        _translate = QtCore.QCoreApplication.translate
        ingresarCancha.setWindowTitle(_translate("ingresarCancha", "Form"))
        self.label.setText(_translate("ingresarCancha", "Agregar Cancha Deportiva"))
        self.label_2.setText(_translate("ingresarCancha", "Codigo:"))
        self.label_3.setText(_translate("ingresarCancha", "Nombre:"))
        self.label_4.setText(_translate("ingresarCancha", "Direccion:"))
        self.label_5.setText(_translate("ingresarCancha", "Valor:"))
        self.cancelarBTN.setText(_translate("ingresarCancha", "Cancelar"))
        self.aceptarBTN.setText(_translate("ingresarCancha", "Aceptar"))

