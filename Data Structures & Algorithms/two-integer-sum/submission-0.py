class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndexMap = {}
        for j in range(len(nums)):
            delta = target - nums[j]
            if (delta in valueIndexMap):
                i = valueIndexMap[delta]
                return [i, j]
            valueIndexMap[nums[j]] = j
        return None
        