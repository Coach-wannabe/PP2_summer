def make(a):
    b = set(a)

    return b

a = [int(x) for x in input().split()]

print(make(a))