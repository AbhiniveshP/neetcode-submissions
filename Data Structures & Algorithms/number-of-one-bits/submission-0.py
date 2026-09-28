class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        for i in range(32):
            if ((1 << i) & n):
                bits += 1
        return bits