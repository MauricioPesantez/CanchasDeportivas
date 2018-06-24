# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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
