# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys

import pickle
import operator

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from Clases.Principal import Ui_MainWindow
from Clases.Ventana_AgregarJugador import Ui_ingresarJugador
from Clases.Ventana_AgregarEquipo import Ui_ingresarEquipo
from Clases.Ventana_AgregarCancha import Ui_ingresarCancha
from Clases.Ventana_AgregarReserva import Ui_agregarReserva
from Clases.Ventana_AgregarCliente import Ui_agregarCliente
from Clases.Venta_Listar import Ui_listado

from Clases.Persona import Persona, Responsable, Arbitro, ClienteReserva, ClienteCampeonato, MiembroEquipo
from Clases.Validacion import JugadorDao, EquipoDao, CanchaDao, ClienteDao, ReservaDao
from Clases.Archivo import Archivo

nombreListas = ["Jugadores.dat", "Canchas.dat", "Reservas.dat", "Campeonatos.dat",
    "Equipos.dat", "Clientes.dat", "Calendario.dat", "Extras.dat"]

listaEquipos=Archivo.cargar(nombreListas[4])
listaCalendarioPartidosCampeonato = Archivo.cargar(nombreListas[6])
listaReservas=Archivo.cargar(nombreListas[2])
listaCampenatos = Archivo.cargar(nombreListas[3])
listaCanchas= Archivo.cargar(nombreListas[1])
listaClientes = Archivo.cargar(nombreListas[5])
listaExtras= Archivo.cargar(nombreListas[7])
listaJugadores = Archivo.cargar(nombreListas[0])

class VentanaIngresarJugador(QtWidgets.QMainWindow, Ui_ingresarJugador):
    def __init__(self, parent=None):
        super(VentanaIngresarJugador, self).__init__(parent)
        self.setupUi(self)
        self.aceptarBTN.clicked.connect(self.guardar)
        self.cancelarBTN.clicked.connect(self.cancelar)
    
    def guardar(self):
        nombre = self.nombreTXT.text()
        apellido = self.apellidoTXT.text()
        cedula = self.cedulaTXT.text()
        edad = self.edadTXT.text()
        
        try:
            #retorna un jugador ya comprobado los datos de ingreso, caso contrario excep
            jugador = JugadorDao.validarJugador(nombre, apellido, cedula, edad)
            
            if(jugador.cedula not in listaJugadores):
                listaJugadores[jugador.cedula] = jugador
                Archivo.guardar(nombreListas[0],listaJugadores)

                QMessageBox.about(self, "Agregar Jugador", "Jugador Agregado Correctamente!!")
                self.close()
            else:
                QMessageBox.about(self, "Agregar Jugador", "El jugador ya existe!!!")

        except ValueError:
            QMessageBox.about(self, "Error", "Ups! Hubo un problema al registrar los datos.\nIntente de nuevo!")
            print("error")
    
    def cancelar(self):
        self.close()


class VentanaIngresarEquipo(QtWidgets.QMainWindow,Ui_ingresarEquipo):
    def __init__(self, parent=None):
        super(VentanaIngresarEquipo, self).__init__(parent)
        self.setupUi(self)
        self.aceptarBTN.clicked.connect(self.guardar)
        self.cancelarBTN.clicked.connect(self.cancelar)
    
    def guardar(self):
        codigo = self.codigoTXT.text()
        nombre = self.nombreTXT.text()
        ciudad = self.ciudadTXT.text()
        
        try:
            #retorna un equipo si los datos estan bien tomados, caso contrario excep
            equipo = EquipoDao.validarEquipo(codigo, nombre, ciudad)
            
            if(equipo.codigo not in listaEquipos):
                listaEquipos[equipo.codigo] = equipo

                Archivo.guardar(nombreListas[4],listaEquipos)
                QMessageBox.about(self, "Agregar Equipo", "Equipo Agregado Correctamente!!")
                self.close()
            else:
                QMessageBox.about(self, "Agregar Equipo", "El Equipo ya existe!!!")

        except ValueError:
            QMessageBox.about(self, "Error", "Ups! Hubo un problema al registrar los datos.\nIntente de nuevo!")
            print("error")
    
    def cancelar(self):
        self.close()

class VentanaIngresarCancha(QtWidgets.QMainWindow,Ui_ingresarCancha):
    def __init__(self, parent=None):
        super(VentanaIngresarCancha, self).__init__(parent)
        self.setupUi(self)
        self.aceptarBTN.clicked.connect(self.guardar)
        self.cancelarBTN.clicked.connect(self.cancelar)
        
    def guardar(self):
        codigo = self.codigoTXT.text()
        nombre = self.nombreTXT.text()
        direccion = self.direccionTXT.text()
        valor = self.valorTXT.text()
        
        try:
            cancha = CanchaDao.validarCancha(codigo, nombre, direccion, valor)
            
            if(cancha.codigo not in listaCanchas):
                listaCanchas[cancha.codigo] = cancha
                Archivo.guardar(nombreListas[1], listaCanchas)
                QMessageBox.about(self, "Agregar Cancha", "Cancha Agregado Correctamente!!")
                self.close()
            else:
                QMessageBox.about(self, "Agregar Cancha", "La Cancha ya existe!!!")

        except ValueError:
            QMessageBox.about(self, "Error", "Ups! Hubo un problema al registrar los datos.\nIntente de nuevo!")
            print("error")
        
    def cancelar(self):
        self.close()

class VentanaIngresarCliente(QtWidgets.QMainWindow, Ui_agregarCliente):
    def __init__(self, parent=None):
        super(VentanaIngresarCliente, self).__init__(parent)
        self.setupUi(self)
        self.aceptarBTN.clicked.connect(self.guardar)
        self.cancelarBTN.clicked.connect(self.cancelar)
    
    def guardar(self):
        nombre = self.nombreTXT.text()
        apellido = self.apellidoTXT.text()
        cedula = self.cedulaTXT.text()
        edad = self.edadTXT.text()
        
        try:
            cliente = ClienteDao.validarCliente(nombre, apellido, cedula, edad)
            if(cliente.cedula not in listaClientes):
                listaClientes[cliente.cedula] = cliente
                Archivo.guardar("Clientes.dat",listaClientes)
                QMessageBox.about(self, "Agregar Cliente", "Cliente Agregado Correctamente!!")
                self.close()
            else:
                QMessageBox.about(self, "Agregar Cliente", "El Cliente ya existe!!!")
                
        except ValueError:
            QMessageBox.about(self, "Error", "Ups! Hubo un problema al registrar los datos.\nIntente de nuevo!")
            
    def cancelar(self):
        self.close()
        

class VentanaIngresarReserva(QtWidgets.QMainWindow, Ui_agregarReserva):
    def __init__(self, parent=None):
        super(VentanaIngresarReserva, self).__init__(parent)
        self.setupUi(self)
        self.aceptarBTN.clicked.connect(self.guardar)
        self.cancelarBTN.clicked.connect(self.cancelar)#listo
        self.ClienteCIBTN.clicked.connect(self.findCliente)#listo
        self.canchaIDBTN.clicked.connect(self.findCancha)#listo
        
    def guardar(self):
        #fecha, horaInicio, horaFin, clienteReserva, canchaDeportiva
        horaFecha = self.fechaHoraTXT.text()
        horaFin = self.horaFInTXT.text()
        #print(horaFecha[:horaFecha.find(" ")])  #fecha
        #print(horaFecha[horaFecha.find(" ")+1:])  #hora
        clienteId = self.clienteIDTXT.text()
        canchaID = self.canchaIDTXT.text()
        
        if(clienteId!='.' and canchaID !='.'):
            #campos llenos
            try:
                cliente = self.findCliente()
                cancha = self.findCancha()
                reserva = ReservaDao.validarReserva(horaFecha[:horaFecha.find(" ")],
                horaFecha[horaFecha.find(" ")+1:], horaFin, cliente, cancha)
                
                listaReservas[cliente.cedula] = reserva
                Archivo.guardar("Reservas.dat",listaReservas)
                QMessageBox.about(self, "Agregar Reserva", "Reserva realizada Correctamente!!")
                self.close()
            except ValueError:
                QMessageBox.about(self, "Error", "Ups! Hubo un problema al registrar los datos.\nIntente de nuevo!")
    
    def findCliente(self):
        print(self.fechaHoraTXT.text())
        self.label_6.setText("")
        idCliente = self.clienteIDTXT.text()
        if(int(idCliente) not in listaClientes):
            QMessageBox.about(self, "Buscar Cliente", "El Cliente no existe!")
        else:
            #si esta en la lista se muestra en pantalla
            cliente=listaClientes[int(idCliente)]
            self.label_6.setText(cliente.nombre +" " +cliente.apellido)
            return cliente
    
    def findCancha(self):
        self.label_7.setText("")
        idCancha = self.canchaIDTXT.text()
        if(idCancha not in listaCanchas):
            QMessageBox.about(self, "Buscar Cancha", "La cancha no existe!")
        
        else:
            cancha = listaCanchas[idCancha]
            self.label_7.setText(cancha.nombre+", Dir:"+cancha.direccion+", val:"+ cancha.valor)
            return cancha
    def cancelar(self):
        self.close()

class VentanaListar(QtWidgets.QMainWindow,Ui_listado):
    def __init__(self, nombre, lista, parent=None):
        super(VentanaListar, self).__init__(parent)
        self.listaObj = lista
        self.setupUi(self)
        self.imprimir.setText(nombre)   #agregamos el nombre de la lista
        self.listarBTN.clicked.connect(self.listar)
        self.cancelarBTN.clicked.connect(self.cancelar)#listo
        
    def listar(self):
        #print(p.__dict__.keys())
        
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        
        numRows = len(self.listaObj)
        numColumns = len(list(self.listaObj.values())[0].__dict__.keys())
        
        #number assignment of rows and columns
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numColumns)
        
        listPlayers = self.obtainList(self.listaObj)#list of data
        x=0
        for i in range(numRows):
            for j in range(numColumns):
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(listPlayers[j+x])))
            x+=4
#        for i in range(numRows):
#            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(listPlayers[i].toString())))
##       self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("1,1"))
#       self.tableWidget.setItem(1,0,QtWidgets.QTableWidgetItem("2,1"))
        
    def obtainList(self, lista):
        containsAtributs = []
        for obj in list(lista.values()):
            atri = (obj.__dict__)
            for k in atri:
                containsAtributs.append(atri[k])
        return containsAtributs
    
    def cancelar(self):
        self.close()

class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        self.setupUi(self)
        self.actionJugador.triggered.connect(self.ingresoDatosJugador)
        self.actionEquipo.triggered.connect(self.ingresoDatosEquipo)
        self.actionCancha.triggered.connect(self.ingresoDatosCancha)
        self.actionCliente.triggered.connect(self.ingresoDatosCliente)
        self.actionRealizar_una_reserva.triggered.connect(self.ingresoDatosReserva)
        self.actionJugadores.triggered.connect(self.listarJugadores)
        self.actionCanchas.triggered.connect(self.listarCanchas)
        self.actionEquipos.triggered.connect(self.listarEquipos)
        self.actionClientes.triggered.connect(self.listarClientes)
        self.actionSalir.triggered.connect(self.salir)
        
    def ingresoDatosJugador(self):
        self.vl = VentanaIngresarJugador()
        self.vl.show()
        
    def ingresoDatosEquipo(self):
        self.vl = VentanaIngresarEquipo()
        self.vl.show()
    def ingresoDatosCancha(self):
        self.vl = VentanaIngresarCancha()
        self.vl.show()
    def ingresoDatosReserva(self):
        self.vl = VentanaIngresarReserva()
        self.vl.show()
    def ingresoDatosCliente(self):
        self.vl = VentanaIngresarCliente()
        self.vl.show()
        
    def listarJugadores(self):
        self.vl = VentanaListar("Jugadores",listaJugadores)
        self.vl.show()
        
    def listarCanchas(self):
        self.vl = VentanaListar("Canchas",listaCanchas)
        self.vl.show()
        
    def listarEquipos(self):
        self.vl = VentanaListar("Equipos",listaEquipos)
        self.vl.show()
        
    def listarClientes(self):
        self.vl = VentanaListar("Clientes",listaClientes)
        self.vl.show()
        
    def salir(self):
        sys.exit(0)
    
