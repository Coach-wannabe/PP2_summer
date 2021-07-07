with open("file.txt") as file:
    words = file.read().split()

longest = max(words, key = len)

print(longest)