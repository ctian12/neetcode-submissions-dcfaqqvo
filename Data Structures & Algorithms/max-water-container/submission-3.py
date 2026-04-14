class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0

        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            print(area)
            out = max(out, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return out