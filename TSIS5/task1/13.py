with open("file3.txt") as file3:
    with open("file4.txt", "w") as file4:
        for line in file3:
            file4.write(line)