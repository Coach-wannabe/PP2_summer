def f(a):
    a.sort()

    for x in a:
        print(x, end = '-')

s = input()

a = s.split('-')

f(a)