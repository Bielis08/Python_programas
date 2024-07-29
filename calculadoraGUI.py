import tkinter as tk

#Operaciones
def sumar(n1, n2):
    resultado = n1 + n2
    return resultado


def restar(n1, n2):
    resultado = n1 - n2
    return resultado


def multiplicacion(n1, n2):
    resultado = n1 * n2
    return resultado


def division(n1, n2):
    resultado = n1 / n2
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


# Creación de GUI
app = tk.Tk()

# Configuración principal
app.geometry("350x600")
app.configure(background="black")
app.wm_title('Calculadora')

#Entrada
operacion = tk.Entry(app, font=("SanFrancisco", 20),fg="white", bd=10, insertwidth=2, width=20, borderwidth=0, bg="black")
operacion.place(x=20, y=70)

# Estilos botones
ancho = 3
alto = 1
colorNum = "#363636"
colorOp = "#ffaf00"
color = "#a3a3a3"

# Botones
Boton0 = tk.Button(app, text="0", relief="flat", bd=0, font=("SanFrancisco", 20),highlightthickness=0, fg="white", bg=colorNum, width=8, height=alto).place(x=20, y=520)
Boton1 = tk.Button(app, text="1", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=20, y=440)
Boton2 = tk.Button(app, text="2", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=100, y=440)
Boton3 = tk.Button(app, text="3", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=440)
Boton4 = tk.Button(app, text="4", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=20, y=360)
Boton5 = tk.Button(app, text="5", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=100, y=360)
Boton6 = tk.Button(app, text="6", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=360)
Boton7 = tk.Button(app, text="7", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=20, y=280)
Boton8 = tk.Button(app, text="8", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=100, y=280)
Boton9 = tk.Button(app, text="9", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=280)

BotonComa = tk.Button(app, text=",", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorNum, width=ancho, height=alto).place(x=180, y=520)
BotonIgual = tk.Button(app, text="=", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=520)
BotonMas = tk.Button(app, text="+", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=440)
BotonMenos = tk.Button(app, text="-", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=360)
BotonMultiplicar = tk.Button(app, text="x", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=280)
BotonDividir = tk.Button(app, text="÷", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="white", bg=colorOp, width=ancho, height=alto).place(x=260, y=200)
BotonRestante = tk.Button(app, text="%", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="black", bg=color, width=ancho, height=alto).place(x=180, y=200)
BotonSigno = tk.Button(app, text="+/-", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="black", bg=color, width=ancho, height=alto).place(x=100, y=200)
BotonBorrar = tk.Button(app, text="AC", relief="flat", bd=0, font=("SanFrancisco", 20), highlightthickness=0, fg="black", bg=color, width=ancho, height=alto).place(x=20, y=200)

app.mainloop()