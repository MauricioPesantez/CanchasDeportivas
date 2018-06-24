# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pickle
import operator
class Archivo:
    def guardar(direccion,lista):
        with open(direccion, 'wb') as f:
            pickle.dump(lista, f,3) 

    def cargar(direccion):
        lista = None
        try:
            with open(direccion, 'rb') as f:
                lista = pickle.load(f)
        except FileNotFoundError:
            lista = {}
        return lista
