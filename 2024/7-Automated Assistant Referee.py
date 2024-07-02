inputactual = input()
posicionx = 0
posiciony = 0
longitud = 0
altura = 0
pxtemp = 0
pytemp = 0

#establecer la longitud del campo
for i in inputactual:
    longitud += 1

while inputactual != '#':
    posicionx = 0
    inputactual = input()
    if pxtemp == 0:
        altura +=1
    elif pxtemp != 0:
        pytemp = altura
    for i in inputactual:
        if i != 'o':
            posicionx += 1
        elif i == 'o':
            pxtemp = posicionx
            break
        



print(f'The ball is in: ({pxtemp}, {pytemp})')