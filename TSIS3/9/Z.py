from collections import deque

nums = list(input().split())
k = int(input())

x = deque(nums)
x.rotate(k)

for i in x:
    print(i, end = ' ')