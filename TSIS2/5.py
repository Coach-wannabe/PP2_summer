class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro = 1
        sum = 0
        
        m = n
        
        while n != 0:
            pro *= n % 10
            n = int(n / 10)
            
        while m != 0:
            sum += m % 10
            m = int(m / 10)
            
        return pro - sum
