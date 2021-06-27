n, m = input().split()

n, m = int(n), int(m)

a = set()
b = set()

for i in range(n):
    a.update(map(int, input().split()))

for i in range(m):
    b.update(map(int, input().split()))

c = a & b

c = sorted(c)
print(len(c))
for x in c:
    print(x, end = ' ')
else: print()

a.symmetric_difference_update(c)
a = sorted(a)
print(len(a))
for x in a:
    print(x, end = ' ')
else: print()

b.symmetric_difference_update(c)
b = sorted(b)
print(len(b))
for x in b:
    print(x, end = ' ')