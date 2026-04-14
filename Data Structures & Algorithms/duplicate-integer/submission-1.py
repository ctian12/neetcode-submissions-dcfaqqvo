class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = []
        for i in nums:
            if i in dupe:
                return True
            else:
                dupe.append(i)
        return False
