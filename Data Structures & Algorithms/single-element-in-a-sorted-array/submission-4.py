class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1


        while l <= r:
            m = (l + r) // 2
            ml = m - 1
            mr = m + 1

            if ((ml < 0 or nums[ml] != nums[m]) and
                (mr == len(nums) or nums[m] != nums[mr])):
                return nums[m]

            if m % 2 == 0:
                if nums[m] == nums[ml]:
                    r = m - 1
                elif nums[m] == nums[mr]:
                    l = m + 1
            else:
                if nums[m] == nums[ml]:
                    l = m + 1
                elif nums[m] == nums[mr]:
                    r = m - 1

        
        return nums[l]