class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        long = 0
        for num in numSet:
            if num - 1 not in numSet:
                curNum = num + 1
                curLong = 1
                if curLong > long:
                    long = curLong
                while curNum in numSet:
                    curLong += 1
                    curNum += 1
                    if curLong > long:
                        long = curLong
        return long