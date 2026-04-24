class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def dfs(cur, used):
            if len(cur) == len(nums):
                out.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    cur.append(nums[i])
                    used[i] = True
                    dfs(cur, used)
                    cur.pop()
                    used[i] = False


        dfs([], [False] * len(nums))
        return out