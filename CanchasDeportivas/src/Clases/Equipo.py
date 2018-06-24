# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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

