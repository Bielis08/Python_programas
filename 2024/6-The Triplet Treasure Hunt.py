times = int(input())
suma = 0

for i in range(1, times+1):
    if i%3 == 0:
        suma += i

print(suma)