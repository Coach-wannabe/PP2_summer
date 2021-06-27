d = dict()

try:
    while True:
        line = input()
        words = line.split()
        for word in words:
            if d.get(word, 0) != 0: d[word] += 1
            else: d[word] = 1
except: pass

def f(item):
    return (-item[1], item[0])

for item in sorted(d.items(), key = f):
    print(item[0])