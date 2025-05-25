#!/usr/bin/env python3

"""
Calculadora de Fechas: Prototipo básico

Este programa permite realizar cálculos con fechas usando la fecha y hora actual del sistema 
como punto de referencia. El usuario puede ingresar una cantidad de segundos o días (positivos o negativos)
para calcular una nueva fecha resultante de sumar o restar el tiempo indicado. El programa muestra 
la nueva fecha y repite el proceso hasta que el usuario decida salir.

Este ejemplo forma parte de una práctica del curso de Introducción a la Programación.

Autor: Danna Fernanda Motta Heranadez <dannamotta1306@gmail.com>
Fecha: 2025-05-24
"""

from datetime import datetime, timedelta

def mostrar_fecha_actual():
    ahora = datetime.now()
    print(f"> La fecha actual es: {ahora}")
    return ahora

def menu():
    print("> Escriba 1 para ingresar segundos, ")
    print(">         2 para ingresar dias,")
    print(">         3 para salir.")

def main():
    while True:
        fecha_actual = mostrar_fecha_actual()
        menu()
        opcion = input("< ")

        if opcion == "1":
            print("> Escriba la cantidad de segundos")
            try:
                segundos = int(input("< "))
                nueva_fecha = fecha_actual + timedelta(seconds=segundos)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print("> Entrada inválida. Por favor ingrese un número entero.")
        elif opcion == "2":
            print("> Escriba la cantidad de días")
            try:
                dias = int(input("< "))
                nueva_fecha = fecha_actual + timedelta(days=dias)
                print(f"> La nueva fecha es: {nueva_fecha}")
            except ValueError:
                print("> Entrada inválida. Por favor ingrese un número entero.")
        elif opcion == "3":
            print("> Gracias!")
            break
        else:
            print("> Opción no válida. Intente de nuevo.")
        print()
    

if __name__ == "__main__":
    main()


