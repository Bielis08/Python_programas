def convertirdis(datos, convertir_a):
    distancia = 0
    if convertir_a.lower() == "km":
        distancia /= 1,609
    elif convertir_a.lower() == "m" or "millas":
        distancia *= 1,609
    return distancia


def convertirtemp(datos, convertir_a):
    if convertir_a.lower() == "c":
        temperatura =  (temperatura - 32) * (9/5)
    elif convertir_a.lower() == "f":
        temperatura *= (9/5) +32
    return temperatura


while True:
    print("A continuación elige la unidad a la que deseas convertir")
    convertir_a = input("Elige 'km' o 'millas' para distancia o 'f' o 'c' para temperatura: ")
    datos = input("Ingrese el parámetro: ")
    if convertir_a.lower() == "m":
        distancia = convertirdis(datos, convertir_a)
        print(distancia)
    elif convertir_a.lower() == "f":
        temperatura = convertirtemp(datos, convertir_a)
        print(temperatura)