# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Clases.Persona import MiembroEquipo
from Clases.Equipo import Equipo
from Clases.Cancha import CanchaDeportiva
from Clases.Persona import ClienteReserva
from Clases.Reserva import Reserva

class JugadorDao:
    def validarJugador(noombre, apellido, cedula, edad):
        #validacion de los datos el ingreso de un jugador
        if(len(noombre)>1 and len(apellido)>1 and len(cedula)>1 and cedula.isdigit() and edad.isdigit()):
            return(MiembroEquipo(noombre, apellido, int(cedula), int(edad)))
        
        else:
            raise Exception("Error al ingresar los datos!")
        
class EquipoDao:
    def validarEquipo(codigo, nombre, ciudad):
        #validacion de los datos ingresados para el equipoo
        if(len(nombre)>1 and len(codigo)>1 and len(ciudad)>1):
            return (Equipo(codigo, nombre, ciudad))
        else:
            raise ValueError("Error al Ingresar Datos")
        
class CanchaDao:
    def validarCancha(codigo, nombre, direccion, valor):
        if(len(codigo)>1 and len(nombre)>1 and len(direccion) and len(valor) and valor.isdigit()):
            return (CanchaDeportiva(codigo, nombre, direccion, valor))
        else:
            raise ValueError("Error al ingresar los datos")
        
class ClienteDao:
    def validarCliente(noombre, apellido, cedula, edad):
        #validacion de los datos el ingreso de un jugador
        if(len(noombre)>1 and len(apellido)>1 and len(cedula)>1 and cedula.isdigit() and edad.isdigit()):
            return(ClienteReserva(noombre, apellido, int(cedula), int(edad)))
        
        else:
            raise Exception("Error al ingresar los datos!")
        
class ReservaDao:
    def validarReserva(fecha, horaInicio, horaFin, cliente, cancha):
        return(Reserva(fecha, horaInicio, horaFin, cliente, cancha))