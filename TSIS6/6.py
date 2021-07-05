def test(a, b, c):
    if c in range(a, b):
        print("YES")
    else: print("NO")

a, b, c = [int(x) for x in input().split()]

test(a, b, c)