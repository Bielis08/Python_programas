mensaje = input()
contador = 0
lista = mensaje.split()
encontrado = -1
signos = {'.', ',', ':', ';', '!', '¡', '?', '¿', '-',}
for x in lista:
    palabra = ""
    for i in x:
        if not i in signos:
            palabra += i
    if palabra.find('42') == 0:
        contador += 1
print(contador)