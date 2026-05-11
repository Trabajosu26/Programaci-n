import logging
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import ErrorSistema


logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def ejecutar_operacion(numero, descripcion, funcion):
    print(f"\nOperación {numero}: {descripcion}")
    logging.info(f"Inicia operación {numero}: {descripcion}")

    try:
        resultado = funcion()
    except ErrorSistema as error:
        print(f"Error controlado: {error}")
        logging.error(f"Error controlado en operación {numero}: {error}")
    except Exception as error:
        print(f"Error inesperado: {error}")
        logging.exception(f"Error inesperado en operación {numero}: {error}")
    else:
        print(resultado)
        logging.info(f"Operación {numero} ejecutada correctamente.")
    finally:
        print("Finalizó la operación.")
        logging.info(f"Finalizó operación {numero}.")


clientes = []
servicios = []
reservas = []


def op1_cliente_valido():
    cliente = Cliente("C001", "Carlos Pérez", "123456789", "carlos@email.com", "3001234567")
    clientes.append(cliente)
    return cliente.mostrar_informacion()


def op2_cliente_invalido_nombre():
    cliente = Cliente("C002", "Lu", "987654321", "luis@email.com", "3009876543")
    clientes.append(cliente)
    return cliente.mostrar_informacion()


def op3_cliente_invalido_correo():
    cliente = Cliente("C003", "Ana Torres", "1234567", "correo_mal", "3014567890")
    clientes.append(cliente)
    return cliente.mostrar_informacion()


def op4_crear_servicio_sala():
    servicio = ReservaSala("S001", "Sala Ejecutiva", 50000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def op5_crear_servicio_equipo():
    servicio = AlquilerEquipo("S002", "Video Beam", 40000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def op6_crear_servicio_asesoria():
    servicio = AsesoriaEspecializada("S003", "Asesoría en Software", 80000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def op7_servicio_precio_invalido():
    servicio = ReservaSala("S004", "Sala Pequeña", -10000)
    servicios.append(servicio)
    return servicio.describir_servicio()


def op8_reserva_exitosa():
    cliente = clientes[0]
    servicio = servicios[0]
    reserva = Reserva(cliente, servicio, 3)
    reservas.append(reserva)
    return reserva.confirmar()


def op9_reserva_duracion_invalida():
    cliente = clientes[0]
    servicio = servicios[1]
    reserva = Reserva(cliente, servicio, 0)
    reservas.append(reserva)
    return reserva.confirmar()


def op10_servicio_no_disponible():
    cliente = clientes[0]
    servicio = AsesoriaEspecializada("S005", "Asesoría no disponible", 70000, disponible=False)
    reserva = Reserva(cliente, servicio, 2)
    reservas.append(reserva)
    return reserva.confirmar()


def op11_cancelar_reserva():
    reserva = reservas[0]
    return reserva.cancelar()


def op12_procesar_reserva_cancelada():
    reserva = reservas[0]
    return reserva.procesar()


if __name__ == "__main__":
    print("SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS")
    print("Empresa: Software FJ")

    ejecutar_operacion(1, "Registro válido de cliente", op1_cliente_valido)
    ejecutar_operacion(2, "Registro inválido de cliente por nombre corto", op2_cliente_invalido_nombre)
    ejecutar_operacion(3, "Registro inválido de cliente por correo incorrecto", op3_cliente_invalido_correo)
    ejecutar_operacion(4, "Creación válida de servicio reserva de sala", op4_crear_servicio_sala)
    ejecutar_operacion(5, "Creación válida de servicio alquiler de equipo", op5_crear_servicio_equipo)
    ejecutar_operacion(6, "Creación válida de servicio asesoría especializada", op6_crear_servicio_asesoria)
    ejecutar_operacion(7, "Creación inválida de servicio con precio negativo", op7_servicio_precio_invalido)
    ejecutar_operacion(8, "Reserva exitosa", op8_reserva_exitosa)
    ejecutar_operacion(9, "Reserva fallida por duración inválida", op9_reserva_duracion_invalida)
    ejecutar_operacion(10, "Reserva fallida por servicio no disponible", op10_servicio_no_disponible)
    ejecutar_operacion(11, "Cancelación de reserva", op11_cancelar_reserva)
    ejecutar_operacion(12, "Procesamiento fallido de reserva cancelada", op12_procesar_reserva_cancelada)

    print("\nProceso finalizado. Revise el archivo sistema.log.")