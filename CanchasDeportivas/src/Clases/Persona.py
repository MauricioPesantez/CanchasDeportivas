# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Persona:
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
    def toString(self):
        return(self.nombre, self.apellido, self.cedula, self.edad)

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