def do_task(x):
    if x == 0:
        return print(0)
    low = x+1
    for c in range(1,x+1):
        if x % c == 0:
            s = c + x//c
            low = min(low, s)

    return print(low)

do_task(int(input()))