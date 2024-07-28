import random

def crearnumero():
    numero = random.randrange(1, 11)
    return numero


def adivinar(eleccion):
    numero = str(crearnumero())
    print(f"El número era: {numero}")
    if eleccion == numero:
        print("Has acertado!!!")
    else:
        print("Has perdido!")

while True:
    elecion = input("Elige un número del 1 al 10: ")
    adivinar(elecion)