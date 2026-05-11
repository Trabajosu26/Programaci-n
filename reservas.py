from excepciones import ErrorReserva, ErrorOperacionNoPermitida


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ErrorReserva("La reserva debe tener un cliente asociado.")
        if servicio is None:
            raise ErrorReserva("La reserva debe tener un servicio asociado.")
        if duracion <= 0:
            raise ErrorReserva("La duración de la reserva debe ser mayor a cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Creada"
        self.total = 0

    def confirmar(self):
        if self.estado != "Creada":
            raise ErrorOperacionNoPermitida("Solo se pueden confirmar reservas en estado Creada.")

        self.servicio.validar_disponibilidad()
        self.total = self.servicio.calcular_costo(self.duracion, descuento=0.05, impuesto=0.19)
        self.estado = "Confirmada"
        return f"Reserva confirmada para {self.cliente.nombre}. Total: ${self.total:.2f}"

    def cancelar(self):
        if self.estado == "Cancelada":
            raise ErrorOperacionNoPermitida("La reserva ya se encuentra cancelada.")
        if self.estado == "Procesada":
            raise ErrorOperacionNoPermitida("No se puede cancelar una reserva procesada.")

        self.estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        if self.estado != "Confirmada":
            raise ErrorOperacionNoPermitida("Solo se pueden procesar reservas confirmadas.")

        self.estado = "Procesada"
        return "Reserva procesada correctamente."

    def mostrar_reserva(self):
        return f"Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Estado: {self.estado}"