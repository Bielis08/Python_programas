msbienv = """Bienvenidos a la calculadora
Para salir escribe Salir
Las operaciones son suma, multi, div y resta"""
print(msbienv)
n1 = 0
op = ""
n2 = 0
while True:
    if n1 != 0:
        op = input('Ingresa operación: ')
        if op.lower() == 'salir':
            break
        n2 = int(input('ingresa siguiente número: '))
        if op.lower() == 'suma':
            n1 += n2
        if op.lower() == 'resta':
            n1 -= n2
        if op.lower() == 'multi':
            n1 *= n2
        if op.lower() == 'div':
            n1 /= n2
        print(f'El resultado es {n1}.')
    else:
        n1 = int(input('Ingresa número: '))