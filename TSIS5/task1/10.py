file = open("file2.txt")
d = dict()
x = file.read().split()

for i in x:
    d[i] = 0
for i in x:
    d[i] += 1
for i in d:
    print(i, ":", d[i])