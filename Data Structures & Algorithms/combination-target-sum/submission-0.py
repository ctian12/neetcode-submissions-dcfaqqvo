class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        def recSum(total, cur, pos):
            if total == target:
                out.append(cur.copy())
                return
            if total > target or pos >= len(nums):
                return
            cur.append(nums[pos])
            recSum(total + nums[pos], cur, pos)
            cur.pop()
            recSum(total, cur, pos + 1)
        recSum(0, [], 0)
        return out
