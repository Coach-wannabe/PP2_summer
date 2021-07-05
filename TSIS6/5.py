def fac(a):
    res = 1
    for x in range(1, a + 1):
        res *= x

    return res

a = int(input())

print(fac(a))