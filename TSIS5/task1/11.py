import os

statinfo = os.stat('file2.txt')
print(statinfo.st_size, 'bytes')