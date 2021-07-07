flist = open("file5.txt").readlines()

print([s.rstrip('\n') for s in flist])