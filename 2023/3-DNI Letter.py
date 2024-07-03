number = int(input())

reminder = number%23

if reminder == 0:
    letter = 'T'
elif reminder == 1:
    letter = 'R'
elif reminder == 2:
    letter = 'W'
elif reminder == 3:
    letter = 'A'
elif reminder == 4:
    letter = 'G'
elif reminder == 5:
    letter = 'M'
elif reminder == 6:
    letter = 'Y'
elif reminder == 7:
    letter = 'F'
elif reminder == 8:
    letter = 'P'
elif reminder == 9:
    letter = 'D'
elif reminder == 10:
    letter = 'X'
elif reminder == 11:
    letter = 'B'
elif reminder == 12:
    letter = 'N'
elif reminder == 13:
    letter = 'J'
elif reminder == 14:
    letter = 'Z'
elif reminder == 15:
    letter = 'S'
elif reminder == 16:
    letter = 'Q'
elif reminder == 17:
    letter = 'V'
elif reminder == 18:
    letter = 'H'
elif reminder == 19:
    letter = 'L'
elif reminder == 20:
    letter = 'C'
elif reminder == 21:
    letter = 'K'
else:
    letter = 'E'

print('Letter:', letter)