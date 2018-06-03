# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import time
import random
class CanchaDeportiva:
    def __init__(self, codigo, nombre, direccion, valor):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.valor = valor

class Persona:
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad

class Responsable(Persona):
    def __init__(self, nombre, apellido, cedula, edad):
        Persona.__init__(self,nombre, apellido, cedula, edad)
        self.canchaResponsable = []

class Arbitro(Persona):
    def __init__(self, nombre, apellido, cedula, edad, costo):
        Persona.__init__(self,nombre, apellido, cedula, edad)
        self.costo = costo

class ClienteReserva(Persona):
    """docstring for ClienteReserva"""
    def __init__(self, nombre, apellido, cedula, edad):
        Persona.__init__(self,nombre, apellido, cedula, edad)
        self.reservasRealizadas = {}
        
class ClienteCampeonato(Persona):
    def __init__(self, nombre, apellido, cedula, edad):
        Persona.__init__(self,nombre, apellido, cedula, edad)
        self.campenato = campenato
        
class MiembroEquipo(Persona):
    def __init__(self, nombre, apellido, cedula, edad):
        Persona.__init__(self,nombre, apellido, cedula, edad)

class Reserva:
    def __init__(self, fecha, horaInicio, horaFin, clienteReserva, canchaDeportiva):
        self.canchaReserva = canchaDeportiva
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.clienteReserva = clienteReserva
        self.costoReserva = canchaDeportiva.valor

    def descuentoClienteFrecuente(self):
        """ Descuento de la reserva segun la cantidad de veces que ha reservado"""
        if (len(self.ClienteReserva.reservasRealizadas)>1):
            self.costoReserva = self.costoReserva - self.costoReserva*(len(self.ClienteReserva.reservasRealizadas)/100)

    def agregarArbitro(self, arbitro):
        self.Arbitro = Arbitro
        self.costoReserva = self.costoReserva + self.arbitro.costo

class Extra():
    """docstring for Extra"""
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Equipo:
    """docstring for Equipo"""
    def __init__(self, codigo, nombre, ciudad):
        self.codigo = codigo
        self.nombre = nombre
        self.ciudad = ciudad
        self.miembros = {}

    def agregarMiembro(self, MiembroEquipo):
        self.miembros[MiembroEquipo.cedula] = MiembroEquipo
        print("Miembro de Equipo Agregado Correctamente!!\n\n")

class Partido:
    """docstring for Partido"""
    def __init__(self, equipo1, equipo2, arbitro):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.arbitro = arbitro  

class Calendario:
    """docstring for Calendario"""
    def __init__(self, fecha, hora, cancha, modalidad, arbitro):
        self.fecha = fecha
        self.hora = hora
        self.cancha = cancha
        self.modalidad = modalidad
        self.arbitro = arbitro 

class Campeonato:
    """docstring for Campeonato"""
    def __init__(self, codigo, fechaInicio, fechaFin, modalidadCampeonato, clienteCampeonato):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.modalidadCampeonato = modalidadCampeonato       
        self.cliente = clienteCampeonato
        self.extras = {}     #puede ser una lista de extras
        self.equipos = {}

    def agregarEquipo(self, equipo):
        self.equipos[equipo.codigo] = equipo

    def agregarExtra(self, extra):
        self.extras[extra.codigo] = extra


"main"
equipos={}
equiposCampeonato={}
reservas={}
campenatos = {}
canchas={}
clientes = {}
extras={}
modalidadCampeonato = ['simple', "fase de grupos"]

''' agregar datos sin consola '''
def auxAddCanchas():
    #codigo, nombre, direccion, valor
    cancha1 = CanchaDeportiva("001Cancha", "CanchaDepor01", "Av. 010203", 25)
    cancha2 = CanchaDeportiva("002Cancha", "CanchaDepor02", "Av. 010203", 35)
    cancha3 = CanchaDeportiva("003Cancha", "CanchaDepor03", "Av. 010203", 30)
    cancha4 = CanchaDeportiva("004Cancha", "CanchaDepor04", "Av. 010203", 10)

    canchas[cancha1.codigo] = cancha1
    canchas[cancha2.codigo] = cancha2
    canchas[cancha3.codigo] = cancha3
    canchas[cancha4.codigo] = cancha4

def auxClientes():
    #nombre, apellido, cedula, edad
    clienteR1 = ClienteReserva("Juan", "Perez1", "0102030410", 45)
    clienteR2 = ClienteReserva("Juan", "Perez2", "0102030411", 35)
    clienteR3 = ClienteReserva("Juan", "Perez3", "0102030422", 40)

    clientes[clienteR1.cedula] = clienteR1
    clientes[clienteR2.cedula] = clienteR2
    clientes[clienteR3.cedula] = clienteR3

def auxExtras():
    #codigo, nombre, precio
    extraAdd = Extra("arb", "Arbitro", 50)
    extraAdd1 = Extra("h20", "Bebidas", 60)
    extraAdd2 = Extra("jz", "Juez", 30)

    extras[extraAdd.codigo] = extraAdd
    extras[extraAdd1.codigo] = extraAdd1
    extras[extraAdd2.codigo] = extraAdd2

def auxEquipo():
    #codigo, nombre, ciudad
    equipo = Equipo("001Eq", "DepCuenca", "Cuenca-Ecuador")
    equipo1 = Equipo("002Eq", "DepAzog", "Cuenca-Ecuador")
    equipo2 = Equipo("003Eq", "Ucuenca", "Cuenca-Ecuador")
    equipo3 = Equipo("004Eq", "Dep Uda", "Cuenca-Ecuador")
    equipo4 = Equipo("005Eq", "Dep Catolica", "Cuenca-Ecuador")
    equipo5 = Equipo("006Eq", "Amistad", "Cuenca-Ecuador")
    equipo6 = Equipo("007Eq", "Tomebamba", "Cuenca-Ecuador")
    equipo7 = Equipo("008Eq", "NUevoClub", "Cuenca-Ecuador")
    equipo8 = Equipo("009Eq", "ClubFriends", "Cuenca-Ecuador")
    equipo9 = Equipo("010Eq", "Amistad1", "Cuenca-Ecuador")
    equipo10 = Equipo("011Eq", "Tomebamba1", "Cuenca-Ecuador")
    equipo11 = Equipo("012Eq", "NUevoClub1", "Cuenca-Ecuador")
    equipo12 = Equipo("013Eq", "ClubFriends1", "Cuenca-Ecuador")
    equipo13 = Equipo("014Eq", "Amistad2", "Cuenca-Ecuador")
    equipo14 = Equipo("015Eq", "Tomebamba2", "Cuenca-Ecuador")
    equipo15 = Equipo("016Eq", "NUevoClub2", "Cuenca-Ecuador")
    equipo16 = Equipo("017Eq", "ClubFriends2", "Cuenca-Ecuador")    
    equipo17 = Equipo("018Eq", "Amistad3", "Cuenca-Ecuador")
    equipo18 = Equipo("019Eq", "Tomebamba3", "Cuenca-Ecuador")
    equipo19 = Equipo("020Eq", "NUevoClub3", "Cuenca-Ecuador")
    equipo20 = Equipo("021Eq", "ClubFriends3", "Cuenca-Ecuador")

    equipos[equipo.codigo] = equipo
    equipos[equipo1.codigo] = equipo1
    equipos[equipo2.codigo] = equipo2
    equipos[equipo3.codigo] = equipo3
    equipos[equipo4.codigo] = equipo4
    equipos[equipo5.codigo] = equipo5
    equipos[equipo6.codigo] = equipo6
    equipos[equipo7.codigo] = equipo7
    equipos[equipo8.codigo] = equipo8
    equipos[equipo9.codigo] = equipo9
    equipos[equipo10.codigo] = equipo10
    equipos[equipo11.codigo] = equipo11
    equipos[equipo12.codigo] = equipo12
    equipos[equipo13.codigo] = equipo13
    equipos[equipo14.codigo] = equipo14
    equipos[equipo15.codigo] = equipo15
    equipos[equipo16.codigo] = equipo16
    equipos[equipo17.codigo] = equipo17
    equipos[equipo18.codigo] = equipo18
    equipos[equipo19.codigo] = equipo19
    equipos[equipo20.codigo] = equipo20

def seleccionarEquipo():
    print("Seleccione el numero perteneciente al Equipo.")
    i=1
    for k in list(equipos.values()):
        print(i,k.nombre)
        i+=1
    numEquipo = int(input("Ingrese el numero correspondiente al equipo: "))
    
    return list(equipos.values())[numEquipo-1]

def seleccionarCliente():
    print("Seleccione el numero perteneciente al Cliente.")
    i=1
    for k in list(clientes.values()):
        print(i, k.nombre, k.apellido)
    numCliente = int(input("Ingrese el numero correspondiente al cliente: "))
    return list(clientes.values())[numCliente-1]

def seleccionarCancha():
    print("Seleccione el numero perteneciente a la cancha.")
    i=1
    for k in list(canchas.values()):
        print(i, k.nombre, k.valor)
    numCancha = int(input("Ingrese el numero correspondiente a la cancha: "))
    return list(canchas.values())[numCancha-1]

def seleccionarModalidad():
    i=1
    for k in modalidadCampeonato:
        print(i, k)
    numModalidad = int(input("Ingrese el numero de la modalidad: "))

    return modalidadCampeonato[numModalidad-1]

def seleccionarExtra():
    print("Seleccione el numero perteneciente a el extra a agregar.")
    i=1
    for k in list(extras.values()):
        print(i, k.nombre, k.precio)
    numExtra = int(input("Ingrese el numero correspondiente a el extra: "))
    return list(canchas.values())[numExtra-1]

def menu():
    print("\tSeleccione una Opcion: \n1. Agregar un Equipo\n2. Agregar un Miembro al Equipo\n3. Realizar una reserva\n4. Crear Torneo\n5. Salir")
    opc = int(input("Seleccione una Opcion: "))

    while(opc<0 and opc>5):
        print("Error!!\n\n")
        print("\tSeleccione una Opcion: \n1. Agregar un Equipo\n2. Agregar un Miembro al Equipo\n3. Realizar una reserva\n4. Crear Torneo\n5. Salir")
        opc = int(input("Seleccione una Opcion: "))
    return opc


''' menu principal y diferentes opciones del programa'''
opcion = menu()
while (opcion!=5):
    if(opcion==1):
        #Agregar Equipo
        codigoEquipo = input("Ingrese el codigo del Equipo: ")
        nombreEquipo = input("Ingrese el nombre del Equipo: ")
        ciudadEquipo = input("Ingrese la ciudad del Equipo: ")
        equipo = Equipo(codigoEquipo, nombreEquipo, ciudadEquipo)
        equipos[equipo.codigo] = equipo
        print("Equipo Agregado correctamente!!\n\n\n\n")
        
    elif (opcion ==2):
        #agregar miembro al equipo
        nombreMiembro = input("Ingrese el nombre: ")
        apellidoMiembro = input("Ingrese el apellido: ")
        cedulaMiembro = input("Ingrese la cedula: ")
        edadMiembro = input("Ingrese la edad: ")
        newMiembro = MiembroEquipo(nombreMiembro, apellidoMiembro, cedulaMiembro, edadMiembro)
        #listamosEquiposParaSeleccionar
        equipoMiembro = seleccionarEquipo()
        #agregamos el miembro
        equipoMiembro.agregarMiembro(newMiembro)
        print("Miembro agregado correctamente!\n\n")
    
    elif(opcion==3):
        #realizar reserva
        #fecha, horaInicio, horaFin, clienteReserva, canchaDeportiva
        fecha = input("Ingrese la fecha de la reserva: ")
        horaInicio = input("Ingrese la hora de la reserva: ")
        horaFin = input("Ingrese la hora se salida: ")
        cliente = seleccionarCliente()
        cancha = seleccionarCancha()
        reserva = Reserva(fecha, horaInicio, horaFin, cliente, cancha)
        reservas[cliente] = reserva
    elif (opcion==4):
        #crearCampeonato
        #codigo, fechaInicio, fechaFin, modalidadCampeonato, clienteCampeonato
        codigo = time.strftime("%c")   #codigo igual a la fecha de creacion del campeoonato, por lo tanto, no se puede repetir codigos
        fechaInicio = str(input("Ingrese la fecha de inicio del campeonato: "))
        fechaFin = str(input("Ingrese la fecha de finalizacion del campeonato: "))
        modalidad  = seleccionarModalidad()
        cliente = seleccionarCliente()

        newCampeonato = Campeonato(codigo, fechaInicio, fechaFin, modalidad, cliente)

        ex = (input("Para seleccionar un extra precione 1, caso contrario cualquier otra tecla: "))
        if(ex=='1'):
            #seleccionamos un extra
            extra = seleccionarExtra()
            newCampeonato.agregarExtra(extra)

        #agregacion de equipos al campeonato.....
        #elegimos 16 equipos al azar para el campeonato
        for i in range(15):
            #16 equipos para fase de grupos
            #obtenemos el equipo randomicamente
            eqSelected = random.choice(list(equipos))

            #verificamos que el equipo no se encuentre en el la lista de los equipos del torneo
            #si no esta, agregamos a la lista
            if(equiposCampeonato.get(eqSelected.codigo)==None):
                equiposCampeonato[eqSelected.codigo] = eqSelected
                
            #caso contrario, iteramos de nuevo, sin aumentar el coontador
            else:
                i--

    opcion = menu()
    