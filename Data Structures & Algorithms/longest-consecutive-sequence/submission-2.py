class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (nums is None or len(nums) == 0):
            return 0
        
        numSet, maxLength = set(nums), 0

        for start in numSet:
            if ((start - 1) not in numSet):
                length = 1
                while ((start + length) in numSet):
                    length += 1
                maxLength = max(maxLength, length)
        
        return maxLength
        