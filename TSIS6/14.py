def f(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True

str = input()

if f(str): print("YES")
else: print("NO")
