def f(s):
    txt = open("file.txt", 'a')
    txt.write(s)

    txt.close()
    
    f = open("file.txt", 'r')
    print(f.read())


s = input()
f(s)