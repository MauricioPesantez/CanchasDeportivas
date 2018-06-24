# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import time
import random
import sys
import pickle
import operator

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from Clases.Persona import Persona, Responsable, Arbitro, ClienteReserva, ClienteCampeonato, MiembroEquipo
from Clases.Reserva import Reserva
from Clases.Cancha import CanchaDeportiva
from Clases.Archivo import Archivo
from Clases.UI import VentanaIngresarJugador, VentanaPrincipal
from Clases.Extra import Extra
from Clases.Equipo import Equipo
from Clases.Partido import Partido
from Clases.Calendario import Calendario
from Clases.Campeonato import Campeonato

"---------------------------------------main---------------------------------------------"
if __name__ == "__main__":
    print("Hello World")
    app = QtWidgets.QApplication(sys.argv)
    myApp = VentanaPrincipal()
    myApp.show()
    # @type app 
    app.exec_()
#    nombreListas = ["Jugadores.dat", "Canchas.dat", "Reservas.dat", "Campeonatos.dat",
#    "Equipos.dat", "Clientes.dat", "Calendario.dat", "Extras.dat"]
#
#    listaEquipos=Archivo.cargar(nombreListas[4])
#    listaCalendarioPartidosCampeonato = Archivo.cargar(nombreListas[6])
#    listaEquiposCampeonato = Archivo.cargar(nombreListas[4])
#    listaReservas=Archivo.cargar(nombreListas[2])
#    listaCampenatos = Archivo.cargar(nombreListas[3])
#    listaCanchas= Archivo.cargar(nombreListas[1])
#    listaClientes = Archivo.cargar(nombreListas[5])
#    listaExtras= Archivo.cargar(nombreListas[7])
#
#    modalidadCampeonato = ['simple', "fase de grupos"]
#
#    def seleccionarEquipo():
#        print("Seleccione el numero perteneciente al Equipo.")
#        i=1
#        for k in list(equipos.values()):
#            print(i,k.nombre)
#            i+=1
#        numEquipo = int(input("Ingrese el numero correspondiente al equipo: "))
#
#        return list(equipos.values())[numEquipo-1]
#
#    def seleccionarCliente():
#        print("Seleccione el numero perteneciente al Cliente.")
#        i=1
#        for k in list(clientes.values()):
#            print(i, k.nombre, k.apellido)
#        numCliente = int(input("Ingrese el numero correspondiente al cliente: "))
#        return list(clientes.values())[numCliente-1]
#
#    def seleccionarCancha():
#        print("Seleccione el numero perteneciente a la cancha.")
#        i=1
#        for k in list(canchas.values()):
#            print(i, k.nombre, k.valor)
#        numCancha = int(input("Ingrese el numero correspondiente a la cancha: "))
#        return list(canchas.values())[numCancha-1]
#
#    def seleccionarModalidad():
#        i=1
#        for k in modalidadCampeonato:
#            print(i, k)
#        numModalidad = int(input("Ingrese el numero de la modalidad: "))
#
#        return modalidadCampeonato[numModalidad-1]
#
#    def seleccionarExtra():
#        print("Seleccione el numero perteneciente a el extra a agregar.")
#        i=1
#        for k in list(extras.values()):
#            print(i, k.nombre, k.precio)
#        numExtra = int(input("Ingrese el numero correspondiente a el extra: "))
#        return list(canchas.values())[numExtra-1]
#
#    def menu():
#        print("\tSeleccione una Opcion: \n1. Agregar un Equipo\n2. Agregar un Miembro al Equipo\n3. Realizar una reserva\n4. Crear Torneo\n5. Salir")
#        opc = int(input("Seleccione una Opcion: "))
#
#        while(opc<0 and opc>5):
#            print("Error!!\n\n")
#            print("\tSeleccione una Opcion: \n1. Agregar un Equipo\n2. Agregar un Miembro al Equipo\n3. Realizar una reserva\n4. Crear Torneo\n5. Salir")
#            opc = int(input("Seleccione una Opcion: "))
#        return opc

#
#    ''' menu principal y diferentes opciones del programa'''
#
    

#
#    opcion = 5
#    while (opcion!=5):
#        if(opcion==1):
#            #Agregar Equipo
#            codigoEquipo = input("Ingrese el codigo del Equipo: ")
#            nombreEquipo = input("Ingrese el nombre del Equipo: ")
#            ciudadEquipo = input("Ingrese la ciudad del Equipo: ")
#            equipo = Equipo(codigoEquipo, nombreEquipo, ciudadEquipo)
#            equipos[equipo.codigo] = equipo
#
#        elif (opcion ==2):
#            #agregar miembro al equipo
#            nombreMiembro = input("Ingrese el nombre: ")
#            apellidoMiembro = input("Ingrese el apellido: ")
#            cedulaMiembro = input("Ingrese la cedula: ")
#            edadMiembro = input("Ingrese la edad: ")
#            newMiembro = MiembroEquipo(nombreMiembro, apellidoMiembro, cedulaMiembro, edadMiembro)
#            #listamosEquiposParaSeleccionar
#            equipoMiembro = seleccionarEquipo()
#            #agregamos el miembro
#            equipoMiembro.agregarMiembro(newMiembro)
#            print("Miembro agregado correctamente!\n\n")
#
#        elif(opcion==3):
#            #realizar reserva
#            #fecha, horaInicio, horaFin, clienteReserva, canchaDeportiva
#            fecha = input("Ingrese la fecha de la reserva: ")
#            horaInicio = input("Ingrese la hora de la reserva: ")
#            horaFin = input("Ingrese la hora se salida: ")
#            cliente = seleccionarCliente()
#            cancha = seleccionarCancha()
#            reserva = Reserva(fecha, horaInicio, horaFin, cliente, cancha)
#            reservas[cliente] = reserva
#        elif (opcion==4):
#            #crearCampeonato
#            #codigo, fechaInicio, fechaFin, modalidadCampeonato, clienteCampeonato
#            codigo = time.strftime("%c")   #codigo igual a la fecha de creacion del campeoonato, por lo tanto, no se puede repetir codigos
#            fechaInicio = str(input("Ingrese la fecha de inicio del campeonato: "))
#            fechaFin = str(input("Ingrese la fecha de finalizacion del campeonato: "))
#            modalidad  = seleccionarModalidad()
#            cliente = seleccionarCliente()
#
#            newCampeonato = Campeonato(codigo, fechaInicio, fechaFin, modalidad, cliente)
#
#            ex = (input("Para seleccionar un extra precione 1, caso contrario cualquier otra tecla: "))
#            if(ex=='1'):
#                #seleccionamos un extra
#                extra = seleccionarExtra()
#                newCampeonato.agregarExtra(extra)
#
#            #agregacion de equipos al campeonato.....
#            #elegimos 16 equipos al azar para el campeonato
#            i=1
#            while (i<=16):
#                eq = random.choice(list(equipos))
#                if(equiposCampeonato.get(eq)==None):
#                    equiposCampeonato[eq] = equipos[eq]
#                    i=i+1
#            #conformados los equipos, se tiene que jugar para ver los ganadores
#            #creamos los partidos del campeonato
#            for i in range(9):
#                #creamos los partidos
#                #equipo1, equipo2, arbitro, fecha, hora, tipo
#                partido = Partido()
#        opcion = menu()
