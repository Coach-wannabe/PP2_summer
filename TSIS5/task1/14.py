file1 = open("file3.txt")
file2 = open("file4.txt")

for line1, line2 in zip(file1, file2):
    print(line1 + line2)