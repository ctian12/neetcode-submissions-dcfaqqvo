class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)

        before = 1
        after = 1

        for i in range(len(nums)):
            out[i] = before
            before *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= after
            after *= nums[i]
        
        return out
