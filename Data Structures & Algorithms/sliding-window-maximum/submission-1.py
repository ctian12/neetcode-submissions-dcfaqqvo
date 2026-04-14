class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        out = []
        q = deque()

        while r < len(nums):
            #remove values smaller than nums[r] because they are no longer needed
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #keep window at size k and add largest to out
            if r - l + 1 >= k:
                out.append(nums[q[0]])
                l += 1

            #remove indices that are out of window
            while q and q[0] < l:
                q.popleft()

            r += 1

        return out