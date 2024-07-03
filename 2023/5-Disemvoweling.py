mensaje = input()
mensajecensurado = ''
for i in mensaje:
    if i == 'A':
        mensajecensurado += '*'
    elif i == 'E':
        mensajecensurado += '*'
    elif i == 'I':
        mensajecensurado += '*'
    elif i == 'O':
        mensajecensurado += '*'
    elif i == 'U':
        mensajecensurado += '*'
    elif i == 'a':
        mensajecensurado += '*'
    elif i == 'e':
        mensajecensurado += '*'
    elif i == 'i':
        mensajecensurado += '*'
    elif i == 'o':
        mensajecensurado += '*'
    elif i == 'u':
        mensajecensurado += '*'
    else:
        mensajecensurado += i
print(mensajecensurado)