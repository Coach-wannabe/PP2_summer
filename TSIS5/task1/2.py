with open('file.txt') as x:
    i = [next(x) for i in range(int(input()))]
print(*i)