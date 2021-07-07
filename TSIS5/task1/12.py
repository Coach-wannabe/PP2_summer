color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

file = open("file3.txt", "w")

for c in color:
    file.write("%s\n" % c)

new = open('file3.txt')
print(new.read())