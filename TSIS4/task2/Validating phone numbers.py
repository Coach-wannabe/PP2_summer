import re

txt = r"[789]\d{9}$"

n = int(input())

while n != 0:
    s = input()
    
    if re.match(r'[789]\d{9}$', s):   
        print("YES")  
    else:  
        print("NO")

    n -= 1
