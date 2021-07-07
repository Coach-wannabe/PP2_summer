n = int(input())

a = open("file2.txt", "r")

lines = a.readlines()

last_lines = lines[-n :]

print(last_lines)

a.close()