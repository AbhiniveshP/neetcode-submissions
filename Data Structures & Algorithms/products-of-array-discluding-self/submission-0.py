class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if (nums is None):
            return None
        
        size = len(nums)
        products = [1] * size
        prefix, suffix = 1, 1

        for i in range(1, size):
            prefix *= nums[i - 1]
            products[i] = prefix
        
        for i in range(size - 2, -1, -1):
            suffix *= nums[i + 1]
            products[i] *= suffix
        
        return products