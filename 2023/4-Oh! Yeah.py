times = int(input())
mensaje = 'OH! YEAH!'
mensajeacabado = ''

for i in mensaje:
    if i == 'A':
        mensajeacabado += i*times
    elif i == 'E':
        mensajeacabado += i*times
    elif i == 'I':
        mensajeacabado += i*times
    elif i == 'O':
        mensajeacabado += i*times
    elif i == 'U':
        mensajeacabado += i*times
    else:
        mensajeacabado += i

print(mensajeacabado)