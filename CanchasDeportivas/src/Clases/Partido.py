# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Partido:
    """docstring for Partido"""
    def __init__(self, equipo1, equipo2, arbitro, fecha, hora, tipo):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.fecha = fecha
        self.hora = hora
        self.arbitro = arbitro
        self.tipo = tipo    #almacena el tipo de partido, puede se de campeonato... contiene el codigo del campeonato.

