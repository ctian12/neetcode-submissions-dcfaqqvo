class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        out = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[i] <= heights[stack[-1]]):
                h = heights[stack[-1]]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                out = max(out, (h * width))
            stack.append(i)
        return out