class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = [[]]

        for num in nums:
            out += [subset + [num] for subset in out]
        
        return out 