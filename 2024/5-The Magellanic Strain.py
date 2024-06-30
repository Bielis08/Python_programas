from math import floor

micro = int(input())
time = int(input())

times = floor(time/micro)
x = 1
if time >= 13 and micro != 1:
    while x < times:
        micro = micro*2
        x = x + 1
elif micro == 1:
    micro = micro*2
else:
    micro = micro
print(micro)