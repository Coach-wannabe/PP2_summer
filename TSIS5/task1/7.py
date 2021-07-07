with open("file2.txt") as file:
    array = list()

    for line in file:
        array.append(line)

    print(array)
