class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        visited = set()

        def backtrack(cur):
            if len(cur) == len(nums):
                out.append(cur.copy())
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                cur.append(nums[i])
                visited.add(nums[i])
                backtrack(cur)
                cur.pop()
                visited.remove(nums[i])

        backtrack([])
        return out