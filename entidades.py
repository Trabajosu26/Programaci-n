from abc import ABC, abstractmethod
import re
from excepciones import ErrorValidacion


class EntidadSistema(ABC):
    def __init__(self, codigo):
        if not codigo:
            raise ErrorValidacion("El código no puede estar vacío.")
        self._codigo = codigo

    @property
    def codigo(self):
        return self._codigo

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Cliente(EntidadSistema):
    def __init__(self, codigo, nombre, documento, correo, telefono):
        super().__init__(codigo)
        self.__nombre = self.__validar_nombre(nombre)
        self.__documento = self.__validar_documento(documento)
        self.__correo = self.__validar_correo(correo)
        self.__telefono = self.__validar_telefono(telefono)

    def __validar_nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 3:
            raise ErrorValidacion("El nombre debe tener mínimo 3 caracteres.")
        return nombre.strip()

    def __validar_documento(self, documento):
        if not str(documento).isdigit() or len(str(documento)) < 6:
            raise ErrorValidacion("El documento debe ser numérico y tener mínimo 6 dígitos.")
        return str(documento)

    def __validar_correo(self, correo):
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron, correo):
            raise ErrorValidacion("El correo electrónico no es válido.")
        return correo

    def __validar_telefono(self, telefono):
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise ErrorValidacion("El teléfono debe ser numérico y tener mínimo 7 dígitos.")
        return str(telefono)

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento} | Correo: {self.__correo}"

    @property
    def nombre(self):
        return self.__nombre