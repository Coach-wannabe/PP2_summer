class Solution:
    def interpret(self, c: str) -> str:
        s = ""
        
        i = 0
        while i < len(c):
            if c[i] == 'G':
                s += 'G'
                i += 1
            elif c[i] == '(' and c[i + 1] == ')':
                s += 'o'
                i += 2
            else:
                s += 'al'
                i += 4
        
        return s
