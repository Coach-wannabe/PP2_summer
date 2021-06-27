class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        alt = 0
        
        for x in gain:
            alt += x
            if alt > res:
                res = alt
                
        return res
