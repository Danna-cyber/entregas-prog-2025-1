#!/usr/bin/env python3

"""
Calculadora 2: prototipo basico

Este es un ejemplo de demostración del uso de la plantilla
para el curso de Introducción a la progración

Autor: Danna Fernanda Motta Heranadez <dannamotta1306@gmail.com>
Fecha: 2025-04-06
"""

# ** En esta región puede importar los módulos necesarios para su programa
# ** O las definiciones de clases y/o funciones que requiera.

def formatear_resultado(resultado):
    """Devuelve el resultado como entero si no tiene decimales, de lo contrario, como flotante."""
    return int(resultado) if resultado.is_integer() else resultado

def solicitar_letra(mensaje):
    """Solicita una letra al usuario sin validación."""
    entrada = input(mensaje).strip()
    if entrada == "":
        return None
    return float(entrada)

def calculadora():
    """script entrypoint"""

    # ** Poner el código ejecutable de su ejercicio
    while True:
        print("Escoge una operación: ")
        print("A. Suma  ")
        print("B. Resta  ")
        print("C. Multiplicación  ")
        print("D. División ")
        print("E. Potenciación  ")
        print("F. División Entera  ")
        print("G. Moduló  ")
        print("H. Salir de la calculadora  ")

        escogerOperacion = input("Bienvenida, selecciona tu operación entre A/B/C/D/E/F/G/H: ")

        # Salir de la calculadora
        if escogerOperacion == 'H':
            print("¡Gracias por usar la calculadora!")  # Mensaje de agradecimiento
            break  # Cierra el ciclo y termina el programa

        # Recopilar operandos solo si no se selecciona 'H'
        primerTermino = int(input("Escribe un número entero: "))
        segundoTermino = int(input("Escribe otro número entero: "))

        if escogerOperacion == 'A':
            resultadoSuma = primerTermino + segundoTermino
            print(f"La suma de {primerTermino} y {segundoTermino} es {resultadoSuma}")

        elif escogerOperacion == 'B':
            resultadoResta = primerTermino - segundoTermino
            print(f"La resta de {primerTermino} y {segundoTermino} es {resultadoResta}")

        elif escogerOperacion == 'C':
            resultadoMultiplicacion = primerTermino * segundoTermino
            print(f"La multiplicación de {primerTermino} y {segundoTermino} es {resultadoMultiplicacion}")

        elif escogerOperacion == 'D':
            if segundoTermino != 0:
                resultadoDivision = primerTermino / segundoTermino
                print(f"La división de {primerTermino} y {segundoTermino} es {resultadoDivision}")
            else:
                print("Nunca dividas por cero 0.")

        elif escogerOperacion == 'E':
            resultadopotenciacion = primerTermino ** segundoTermino
            print(f"La potenciación de {primerTermino} y {segundoTermino} es {resultadopotenciacion}")

        elif escogerOperacion == 'F':
            if segundoTermino != 0:
                resultadodivisionentera = primerTermino // segundoTermino
                print(f"La división entera de {primerTermino} y {segundoTermino} es {resultadodivisionentera}")
            else:
                print("Nunca dividas por cero 0.")

        elif escogerOperacion == 'G':
            if segundoTermino != 0:
                resultadomodulo = primerTermino % segundoTermino
                print(f"El módulo de {primerTermino} y {segundoTermino} es {resultadomodulo}")
            else:
                print("No se puede calcular el módulo por 0.")

        # Si no se escoge una opción válida, ejecutar de nuevo el código
        else:
            print("Selecciona opciones A/B/C/D/E/F/G/H.")

        # Saludo
        print("Hola mundo!")

# ** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    calculadora()
