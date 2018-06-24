# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_agregarEquipo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ingresarEquipo(object):
    def setupUi(self, ingresarEquipo):
        ingresarEquipo.setObjectName("ingresarEquipo")
        ingresarEquipo.resize(338, 269)
        self.label = QtWidgets.QLabel(ingresarEquipo)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ingresarEquipo)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 65, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ingresarEquipo)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 65, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ingresarEquipo)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 65, 20))
        self.label_4.setObjectName("label_4")
        self.codigoTXT = QtWidgets.QLineEdit(ingresarEquipo)
        self.codigoTXT.setGeometry(QtCore.QRect(80, 50, 141, 32))
        self.codigoTXT.setObjectName("codigoTXT")
        self.nombreTXT = QtWidgets.QLineEdit(ingresarEquipo)
        self.nombreTXT.setGeometry(QtCore.QRect(80, 90, 141, 32))
        self.nombreTXT.setObjectName("nombreTXT")
        self.ciudadTXT = QtWidgets.QLineEdit(ingresarEquipo)
        self.ciudadTXT.setGeometry(QtCore.QRect(80, 130, 141, 32))
        self.ciudadTXT.setObjectName("ciudadTXT")
        self.aceptarBTN = QtWidgets.QPushButton(ingresarEquipo)
        self.aceptarBTN.setGeometry(QtCore.QRect(50, 210, 94, 30))
        self.aceptarBTN.setObjectName("aceptarBTN")
        self.cancelarBTN = QtWidgets.QPushButton(ingresarEquipo)
        self.cancelarBTN.setGeometry(QtCore.QRect(190, 210, 94, 30))
        self.cancelarBTN.setObjectName("cancelarBTN")

        self.retranslateUi(ingresarEquipo)
        QtCore.QMetaObject.connectSlotsByName(ingresarEquipo)

    def retranslateUi(self, ingresarEquipo):
        _translate = QtCore.QCoreApplication.translate
        ingresarEquipo.setWindowTitle(_translate("ingresarEquipo", "Form"))
        self.label.setText(_translate("ingresarEquipo", "Agregar Equipo"))
        self.label_2.setText(_translate("ingresarEquipo", "Codigo:"))
        self.label_3.setText(_translate("ingresarEquipo", "Nombre:"))
        self.label_4.setText(_translate("ingresarEquipo", "Ciudad:"))
        self.aceptarBTN.setText(_translate("ingresarEquipo", "Aceptar"))
        self.cancelarBTN.setText(_translate("ingresarEquipo", "Cancelar"))

