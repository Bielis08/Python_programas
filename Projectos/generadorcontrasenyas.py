import random

def crearcontrasenya(longitud):
    longitud = ["a"] * (longitud - 1)
    contrasenya = ""
    for i in longitud:
        contrasenya = contrasenya + random.randrange(10)
    print(f"Su contraseña es: {contrasenya}")

while True:
    longitud = int(input("Introduzca la longitud de la contraseña: "))
    crearcontrasenya(longitud)
