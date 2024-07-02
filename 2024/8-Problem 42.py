mensaje = input()
contador = 0
lista = mensaje.split()
encontrado = -1
for x in lista:
    puntos = 0
    encontrado = -1
    encontrado = x.find('42')
    if encontrado != -1:
        for i in x:
            if i != '0' or '.' or ',':
                puntos += 1
        if puntos == 0:
            contador += 1
print(contador)