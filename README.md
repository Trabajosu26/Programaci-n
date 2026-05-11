# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

## Descripción del proyecto

Este proyecto corresponde al desarrollo de la Fase 4 del curso **Programación 213023** de la Universidad Nacional Abierta y a Distancia - UNAD. La actividad tiene como propósito implementar una solución orientada a objetos que evidencie estabilidad, robustez y manejo adecuado de errores mediante el uso de excepciones en Python.

El sistema desarrollado permite gestionar clientes, servicios y reservas para la empresa ficticia **Software FJ**, la cual ofrece diferentes tipos de servicios como:

- Reserva de salas.
- Alquiler de equipos.
- Asesorías especializadas.

La aplicación no utiliza bases de datos. Toda la información se gestiona mediante objetos, listas internas y archivos de registro para eventos y errores.

## Objetivo general

Desarrollar una aplicación orientada a objetos en Python que permita gestionar clientes, servicios y reservas, implementando principios de programación orientada a objetos y manejo avanzado de excepciones para garantizar la estabilidad del sistema.

## Objetivos específicos

- Aplicar los principios de abstracción, herencia, polimorfismo y encapsulación.
- Implementar clases abstractas y clases derivadas para representar las entidades del sistema.
- Gestionar clientes, servicios y reservas mediante objetos y listas internas.
- Implementar validaciones estrictas para evitar errores durante la ejecución.
- Crear excepciones personalizadas para controlar situaciones inválidas.
- Registrar eventos y errores en un archivo de logs.
- Simular operaciones válidas e inválidas para comprobar la robustez del programa.

## Tecnologías utilizadas

- Python 3
- Programación orientada a objetos
- Módulo `abc` para clases abstractas
- Módulo `logging` para archivo de logs
- Manejo de excepciones con `try`, `except`, `else` y `finally`

## Requisitos del sistema

Para ejecutar el proyecto se requiere:

- Tener instalado Python 3.10 o superior.
- Un editor de código como Visual Studio Code, PyCharm o similar.
- Consola o terminal para ejecutar el archivo principal.

## Estructura general del proyecto

```text
software_fj/
│
├── main.py
├── logs_sistema.log
└── README.md
