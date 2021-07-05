def isPrime(a):
    d = 0

    if a == 0: return False
    elif a == 1: return False
    else:
        for x in range(1, a + 1):
            if a % x == 0: d += 1

        if d == 2: return True
        else: return False
    

a = int(input())

if isPrime(a):
    print("YES")
else: print("NO")