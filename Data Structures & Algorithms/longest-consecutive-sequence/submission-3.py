class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                len = 1
                while num + len in numSet:
                    len += 1
                longest = max(len, longest)
        
        return longest
            
