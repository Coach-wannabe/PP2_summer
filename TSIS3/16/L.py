d = dict()

n = int(input())

for i in range(n):
    s = input().split()
    d[s[0]] = s[1]

s = input()

for k, v in d.items():
    if s == k: print(v)
    elif s == v: print(k)


