from abc import ABC, abstractmethod
from excepciones import ErrorValidacion, ErrorServicioNoDisponible


class Servicio(ABC):
    def __init__(self, codigo, nombre, precio_base, disponible=True):
        if not codigo:
            raise ErrorValidacion("El código del servicio no puede estar vacío.")
        if not nombre:
            raise ErrorValidacion("El nombre del servicio no puede estar vacío.")
        if precio_base <= 0:
            raise ErrorValidacion("El precio base debe ser mayor a cero.")

        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ErrorServicioNoDisponible(f"El servicio {self.nombre} no está disponible.")

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ErrorValidacion("La duración de la reserva debe ser mayor a cero.")

        subtotal = self.precio_base * duracion
        subtotal -= subtotal * descuento
        total = subtotal + subtotal * impuesto
        return total

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}, precio por hora: ${self.precio_base}"


class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ErrorValidacion("La duración del alquiler debe ser mayor a cero.")

        seguro = 15000
        subtotal = (self.precio_base * duracion) + seguro
        subtotal -= subtotal * descuento
        total = subtotal + subtotal * impuesto
        return total

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}, incluye seguro básico."


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        if duracion <= 0:
            raise ErrorValidacion("La duración de la asesoría debe ser mayor a cero.")

        tarifa_profesional = 30000
        subtotal = (self.precio_base * duracion) + tarifa_profesional
        subtotal -= subtotal * descuento
        total = subtotal + subtotal * impuesto
        return total

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}, con tarifa profesional adicional."