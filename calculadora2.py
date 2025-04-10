def formatear_resultado(resultado):
    """Devuelve el resultado como entero si no tiene decimales, de lo contrario, como flotante."""
    return int(resultado) if resultado.is_integer() else resultado

def calcular_operacion(operacion, primerTermino, segundoTermino):
    """Realiza la operación seleccionada y muestra el resultado."""
    if operacion == 'A':
        resultado = primerTermino + segundoTermino
        print(f"La suma de {primerTermino} y {segundoTermino} es {resultado}")

    elif operacion == 'B':
        resultado = primerTermino - segundoTermino
        print(f"La resta de {primerTermino} y {segundoTermino} es {resultado}")

    elif operacion == 'C':
        resultado = primerTermino * segundoTermino
        print(f"La multiplicación de {primerTermino} y {segundoTermino} es {resultado}")

    elif operacion == 'D':
        if segundoTermino != 0:
            resultado = primerTermino / segundoTermino
            print(f"La división de {primerTermino} y {segundoTermino} es {resultado}")
        else:
            print("Nunca dividas por cero 0.")

    elif operacion == 'E':
        resultado = primerTermino ** segundoTermino
        print(f"La potenciación de {primerTermino} y {segundoTermino} es {resultado}")

    elif operacion == 'F':
        if segundoTermino != 0:
            resultado = primerTermino // segundoTermino  # División entera
            print(f"La división entera de {primerTermino} y {segundoTermino} es {resultado}")
        else:
            print("Nunca dividas por cero 0.")

    elif operacion == 'G':
        if segundoTermino != 0:
            resultado = primerTermino % segundoTermino
            print(f"El módulo de {primerTermino} y {segundoTermino} es {resultado}")
        else:
            print("No se puede calcular el módulo por 0.")

    elif operacion == 'H':
        print("¡Gracias por usar la calculadora!")
        return False  # Retornamos False para salir del bucle

    return True  # Retornamos True para continuar el bucle


def run():
    """script entrypoint"""
    while True:
        print("\nEscoge una operación: ")
        print("A. Suma")
        print("B. Resta")
        print("C. Multiplicación")
        print("D. División")
        print("E. Potenciación")
        print("F. División Entera")
        print("G. Módulo")
        print("H. Salir de la calculadora")

        escogerOperacion = input("Selecciona tu operación entre A/B/C/D/E/F/G/H: ").upper()

        # Recopilar operandos
        try:
            primerTermino = int(input("Escribe un número entero: "))
            segundoTermino = int(input("Escribe otro número entero: "))
        except ValueError:
            print("Por favor ingresa números enteros válidos.")
            continue  # Vuelve a mostrar el menú si ocurre un error

        # Ejecutar la operación y verificar si se debe salir
        if not calcular_operacion(escogerOperacion, primerTermino, segundoTermino):
            break  # Salir si el usuario elige 'H'


if __name__ == "__main__":
    run()
