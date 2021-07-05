def f(a):
    for x in a:
        if x % 2 == 0: print(x, end = ' ')

a = [int(x) for x in input().split()]

f(a)