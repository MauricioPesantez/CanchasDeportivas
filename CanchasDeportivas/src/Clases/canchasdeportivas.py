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
