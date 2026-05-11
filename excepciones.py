class ErrorSistema(Exception):
    """Excepción base del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Excepción para datos inválidos."""
    pass


class ErrorServicioNoDisponible(ErrorSistema):
    """Excepción para servicios no disponibles."""
    pass


class ErrorReserva(ErrorSistema):
    """Excepción para errores en reservas."""
    pass


class ErrorOperacionNoPermitida(ErrorSistema):
    """Excepción para operaciones no permitidas."""
    pass