file = open("file2.txt")

data = file.read()
data.replace(",", " ")

print(len(data.split(" ")))