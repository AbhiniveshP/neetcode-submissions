class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 2):
            return n
        
        n1, n2, res = 1, 2, None
        for i in range(3, n+1):
            res = n1 + n2
            n1 = n2
            n2 = res
        
        return res 