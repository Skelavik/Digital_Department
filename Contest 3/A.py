
def math_car(k_n,a):

    last = 0
    res = 0

    for i in range(0,len(a)):

        if (int(a[i]) - int(k_n[0]) + last) > 0:
            res = int(a[i]) - int(k_n[0]) + last
            last = int(a[i]) - int(k_n[0])
        else:
            res = int(a[i]) - int(k_n[0]) + last
            last = 0

    print()


#l1 = input()
l1 = "4 3"
k_n = l1.split()

#l2 = input()
l2 = "3 4 5"
a = l2.split()
math_car(k_n,a)






