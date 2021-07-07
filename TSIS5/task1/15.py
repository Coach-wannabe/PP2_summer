import random

file = open("file2.txt", "r")

lines = file.readlines()

print(random.choice(lines))