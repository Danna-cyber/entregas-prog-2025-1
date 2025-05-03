"""
Organizador de texto 

Este es un ejemplo de demostración del uso de la plantilla
para el curso de Introducción a la programación de un organizador de texto de texto.

Autor: Danna Fernanda Motta Heranadez <dannamotta1306@gmail.com>
Fecha: 2025-05-02
"""

def mostrar_menu():
    print("\nMenú de operaciones:")
    print("1. Pasar a minúsculas")
    print("2. Pasar a mayúsculas")
    print("3. Invertir mayúsculas/minúsculas")
    print("4. Capitalización (primera letra mayúscula)")
    print("5. Titulación (primera letra mayúscula en cada palabra)")
    print("6. Reemplazar espacios por guiones bajos")
    print("7. Salir")

def main():
    texto = input("Ingrese una línea de texto: ")

    mostrar_menu()
    opcion = input("Seleccione una opción (1-7): ")

    if opcion == "1":
        texto = texto.lower()
        print("Texto modificado:", texto)
    elif opcion == "2":
        texto = texto.upper()
        print("Texto modificado:", texto)
    elif opcion == "3":
        texto = texto.swapcase()
        print("Texto modificado:", texto)
    elif opcion == "4":
        texto = texto.capitalize()
        print("Texto modificado:", texto)
    elif opcion == "5":
        texto = texto.title()
        print("Texto modificado:", texto)
    elif opcion == "6":
        texto = texto.replace(" ", "_")
        print("Texto modificado:", texto)
    elif opcion == "7":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Programa finalizado.")

if __name__ == "__main__":
    main()
