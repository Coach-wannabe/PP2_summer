a = list(input().split())

b = []
cnt = 0
for x in a:
    if int(x) > 0: b.append(x)
    elif int(x) == 0: cnt += 1
while cnt != 0:
    b.append("0")
    cnt -= 1

for i in b:
    print(i, end = ' ')