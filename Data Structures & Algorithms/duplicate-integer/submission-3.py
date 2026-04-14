class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialize set to track seen numbers
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False