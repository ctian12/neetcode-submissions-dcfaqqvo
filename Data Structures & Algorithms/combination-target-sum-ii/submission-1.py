class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        def recSum(total, cur, pos):
            if total == target:
                if cur not in out:
                    out.append(cur.copy())
                return
            if total > target or pos >= len(candidates):
                return
            cur.append(candidates[pos])
            recSum(total + candidates[pos], cur, pos + 1)
            cur.pop()
            recSum(total, cur, pos + 1)
        recSum(0, [], 0)
        return out