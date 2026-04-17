class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                elif target == nums[m]:
                    return m
                elif target > nums[m] and target < nums[r]:
                    l = m + 1
                else:
                    return r
            else:
                if target < nums[m] and target > nums[r]:
                    r = m - 1
                elif target < nums[r] or target > nums[m]:
                    l = m + 1
                elif target == nums[m]:
                    return m
                else:
                    return r
        if nums[l] == target:
            return l
        else:
            return -1
