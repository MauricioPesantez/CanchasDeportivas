# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


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