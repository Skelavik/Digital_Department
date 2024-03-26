
def do_task(x):
    s = 0
    c = 0
    if x == 0:
        return print(0)
    while (x % 10 != 0) or (x // 10 != 0):
        if (x % 10)%4 == 0:
            c = 1
            s += (x%10)
        x = x // 10
    if c == 1:
        return print(s)
    else:
        return print("No")
do_task(int(input()))