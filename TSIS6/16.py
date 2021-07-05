import math

def f(n):
    res = list()
    i = 1
    while i <= n:
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            res.append(i)
        i += 1

    print(res)

n = 30

f(n)

