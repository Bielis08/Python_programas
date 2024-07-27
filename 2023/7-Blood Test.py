sex = input()
redbloodcells = int(input())
whitebloodcells = int(input())
platelets = int(input())
hemoglobin = int(input())
hematocrcit = int(input())
lista = [redbloodcells, whitebloodcells, platelets, hemoglobin, hematocrcit]
if sex == 'Male':
    if redbloodcells < 4.3:
        redbloodcells = 'VISIT THE DOCTOR'

print(redbloodcells)