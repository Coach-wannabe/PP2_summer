class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        cnt = 0
        
        for i in range(0, len(a)):
            for j in range(i, len(a)):
                if a[i] == a[j] and i < j:
                    cnt += 1
                    
        return cnt
