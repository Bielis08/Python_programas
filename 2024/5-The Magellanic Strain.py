from math import floor

micro = int(input())
time = int(input())

times = floor(time/13)
x = 0
if time >= 13:
    while x < times:
        micro = micro*2
        x = x + 1
else:
    micro = micro
print(micro)