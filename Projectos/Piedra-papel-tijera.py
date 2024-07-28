import random

print("Bienvenido a Piedra Papel o Tijera")
print("Para jugar escriba una de estas elecciones: Piedra, Papel o Tijera")
print("Para salir escriba: Salir")

def comprobar(eleccion):
    elecciones = ["Piedra", "Papel", "Tijera"]
    eleccionrival = random.choice(elecciones)
    print(f"Tu elección: {eleccion}, Elección del rival: {eleccionrival}")
    
    if eleccionrival == eleccion:
        print("Empate.")
    elif (eleccion == "Tijera" and eleccionrival == "Piedra") or \
         (eleccion == "Papel" and eleccionrival == "Tijera") or \
         (eleccion == "Piedra" and eleccionrival == "Papel"):
        print("Has perdido.")
    else:
        print("Has ganado.")

def comprobarentrada():
    while True:
        eleccion = input("Escriba su elección: ")
        if eleccion.lower() in ["piedra", "papel", "tijera", "salir"]:
            return eleccion.capitalize()
        else:
            print("Entrada no válida. Inténtelo de nuevo.")

while True:
    eleccion = comprobarentrada()
    if eleccion == "Salir":
        break
    comprobar(eleccion)
