x = 1

while True:
    if x == 2:
        break
    if x == 3:
        break
    if x % 2 != 0 and x % 3 != 0:
        break
    x = x - 1
print(x)