#!/usr/bin/env python3

"""
Calculadora 1: prototipo basico

Este es un ejemplo de demostración del uso de la plantilla
para el curso de Introducción a la progración

Autor: Danna Fernanda Motta Heranadez <dannamotta1306@gmail.com>
Fecha: 2025-03-13
"""

# ** En esta región puede importar los módulos necesarios para su programa
# ** O las definiciones de clases y/o funciones que requiera.


def run():
    """script entrypoint"""

    # ** Poner el código ejecutable de su ejercicio aquí

    print("Escoge una operación: ")
    print("A. Suma ")
    print("B. Resta ")
    print("C. Multiplicación ")
    print("D. División ")

    escogerOperacion = input("Bienvenida, selecciona tu operación entre A/B/C/D: ")

    # Recopilar operandos
    primerTermino = int(input("Escribe un número entero: "))
    segundoTermino = int(input("Escribe otro número entero: "))

    if escogerOperacion == 'A':
        resultadoSuma = primerTermino + segundoTermino
        print(
            f"La suma de {primerTermino} y {segundoTermino} es {resultadoSuma}"
            )

    elif escogerOperacion == 'B':
        resultadoResta = primerTermino - segundoTermino
        print(
            f"La resta de {primerTermino} y {segundoTermino} es {resultadoResta}"
            )

    elif escogerOperacion == 'C':
        resultadoMultiplicacion = primerTermino * segundoTermino
        print(
            f"La multiplicación de {primerTermino} y {segundoTermino} es {resultadoMultiplicacion}"
            )

    elif escogerOperacion == 'D':
        if segundoTermino != 0:
            resultadoDivision = primerTermino / segundoTermino
            print(
                f"La división de {primerTermino} y {segundoTermino} es {resultadoDivision}"
                )
        else:
            print("Nunca dividas por cero 0.")

    # Si no se escoge una opción de A/B/C/D, ejecutar de nuevo el código
    else:
        print("Selecciona opciones A/B/C/D.")

        # Saludo
        print("Hola mundo!")

        # ** **


# ** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
