def do_task(x):
    x1 = x
    while True:
        if x == 2:
            break
        if x == 3:
            break
        if x % 2 != 0 and x % 3 != 0:
            break
        x = x - 1

    while True:
        if x1 == 2:
            break
        if x1 == 3:
            break
        if x1 % 2 != 0 and x1 % 3 != 0:
            break
        x1 = x1 + 1
    return print(x,x1)

while True:
    x = int(input())
    if x > 1 and x <= 10000:
        do_task(x)
        break