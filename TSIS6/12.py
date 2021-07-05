def f(s):
    return s == s[::-1]

s = input()

if f(s): print("YES")
else: print("NO")