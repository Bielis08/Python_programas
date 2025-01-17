import tkinter as tk

#Operaciones
def sumar(n1, n2):
    resultado = n1 + n2
    return resultado


def restar(n1, n2):
    resultado = n1 - n2
    return resultado


def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado


def dividir(n1, n2):
    if n2 != 0:
        resultado = n1 / n2
    else:
        return -1
    return resultado


def restante(n1, n2):
    resultado = n1 % n2
    return resultado


def cambiarsigno(n):
    resultado = -n
    return resultado


def borrar(operacion):
    operacion -= operacion
    return operacion


def simplificar(operacion):
    operaciones = ['*', '/', '%']
    posicion = 0
    # Buscar operaciones de alta prioridad
    for numero in operacion:
        if numero in operaciones:
            if numero == '*':
                n1 = operacion[posicion - 1]
                n2 = operacion[posicion + 1]
                resultado = multiplicar(n1, n2)
                # Eliminar operacion y dejar el resultado en la lista de operacion
                operacion.pop(posicion - 1)
                operacion.pop(posicion)
                operacion.pop(posicion - 1)
                operacion.insert(posicion - 1, resultado)
            elif numero == '/':
                n1 = operacion[posicion - 1]
                n2 = operacion[posicion + 1]
                resultado = dividir(n1, n2)
                # Eliminar operacion y dejar el resultado en la lista de operacion
                operacion.pop(posicion - 1)
                operacion.pop(posicion)
                operacion.pop(posicion - 1)
                operacion.insert(posicion - 1, resultado)
                if resultado == -1:
                    mensaje = "No se puede dividir entre 0!"
                    return mensaje
            elif numero == '%':
                n1 = operacion[posicion - 1]
                n2 = operacion[posicion + 1]
                resultado = restante(n1, n2)
                # Eliminar operacion y dejar el resultado en la lista de operacion
                operacion.pop(posicion - 1)
                operacion.pop(posicion)
                operacion.pop(posicion - 1)
                operacion.insert(posicion - 1, resultado)
        posicion += 1
    return operacion



def calcular(entrada):
    # Convertir entrada a lista con numeros convertidos a float
    operaciones = ['+', '-', '*', '/', '%']
    operacion = []
    numeroactual = ""
    for numero in entrada:
        if numero in operaciones:
            if numeroactual != "":
                numeroactual = float(numeroactual)
                operacion.append(numeroactual)
                operacion.append(numero)
            numeroactual = ""
        # Quita imperfecciones de la entrada del usuario
        elif numero == ",":
            numeroactual = numeroactual + "."
        elif numero != " ":
            numeroactual = numeroactual + numero
    numeroactual = float(numeroactual)
    operacion.append(numeroactual)
    # Empezar a calcular
    operacion = simplificar(operacion)
    if operacion == "No se puede dividir entre 0!":
        return operacion
    else:
        resultado = 0
        while not len(operacion) == 0:
            if len(operacion) == 1:
                resultado += operacion[0]
                return resultado
            elif len(operacion) == 2:
                operacion.pop(0)
                operacion.pop(0)
            else:
                if operacion[1] == '+':
                    resultado += sumar(operacion[0], operacion[2])
                    operacion.pop(0)
                elif operacion[1] == '-':
                    resultado += restar(operacion[0], operacion[2])
                    operacion.pop(0)
        return resultado


def comprobar():
    if entrada.lower() != 'salir':
        resultado = calcular(entrada)
        if resultado != "No se puede dividir entre 0!":
            print(f'El resultado de la operación es: {resultado}')
        else:
            print(resultado)
    else:
        return -1



# Calculadora
print('Bienvenido a la calculadora. Para salir escriba "Salir"')
while True:
    entrada = input("Introduzca la operación: ")
    if comprobar() == -1:
        break


# # Creación de GUI
# app = tk.Tk()

# # Configuración principal
# app.geometry("350x600")
# app.configure(background="black")
# app.wm_title('Calculadora')

# #Entrada
# operacion = tk.Entry(app, font=("SanFrancisco", 20),fg="white", bd=10, insertwidth=2, width=20, borderwidth=0, bg="gray")
# operacion.place(x=20, y=70)

# # Estilos botones
# ancho = 3
# alto = 1
# colorNum = "#363636"
# colorOp = "#ffaf00"
# color = "#a3a3a3"

# # Botones
# Boton0 = tk.Button(app, text="0", relief="flat", bd=0, font=("SanFrancisco", 20),highlightthickness=0, fg="white", bg=colorNum, width=8, height=alto).place(x=20, y=520)
# Boton1 = tk.Button(app, text="1", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=20, y=440)
# Boton2 = tk.Button(app, text="2", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=100, y=440)
# Boton3 = tk.Button(app, text="3", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=440)
# Boton4 = tk.Button(app, text="4", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=20, y=360)
# Boton5 = tk.Button(app, text="5", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=100, y=360)
# Boton6 = tk.Button(app, text="6", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=360)
# Boton7 = tk.Button(app, text="7", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=20, y=280)
# Boton8 = tk.Button(app, text="8", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=100, y=280)
# Boton9 = tk.Button(app, text="9", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=280)

# BotonComa = tk.Button(app, text=",", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=520)
# BotonIgual = tk.Button(app, text="=", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=520)
# BotonMas = tk.Button(app, text="+", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=440)
# BotonMenos = tk.Button(app, text="-", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=360)
# BotonMultiplicar = tk.Button(app, text="x", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=280)
# BotonDividir = tk.Button(app, text="÷", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=200)
# BotonRestante = tk.Button(app, text="%", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="black", bg=color, width=ancho, height=alto).place(x=180, y=200)
# BotonSigno = tk.Button(app, text="+/-", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="black", bg=color, width=ancho, height=alto).place(x=100, y=200)
# BotonBorrar = tk.Button(app, text="AC", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="black", bg=color, width=ancho, height=alto).place(x=20, y=200)

# app.mainloop()