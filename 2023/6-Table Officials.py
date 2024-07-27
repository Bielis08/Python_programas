from math import floor

freetrhouws = int(input())
fieldgoals = int(input())
fieldgoals3 = int(input())
totalshoots = int(input())

points = freetrhouws + fieldgoals*2+fieldgoals3*3
perc = ((freetrhouws+fieldgoals+fieldgoals3)*100)/totalshoots

print(f'{points} {floor(perc)}%')