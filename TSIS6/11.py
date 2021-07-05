def f(a):
    z = []
    for x in range(1, a):
        if a % x == 0:
            z.append(x)

    x = sum(z)
    if x == a:
        if (x + a) / 2 == a:
            return True
        else: return False
    else: return False

a = int(input())

if f(a): print("YES")
else: print("NO")