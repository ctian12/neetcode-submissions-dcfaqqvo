class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        out = 0
        charSet = set(s)
        for c in charSet:
            curMax = 0
            l = 0
            for r in range(len(s)):
                if s[r] == c:
                    curMax += 1
                while r - l + 1 - curMax > k:
                    if s[l] == c:
                        curMax -= 1
                    l += 1
                if r - l + 1 > out:
                    out = r - l + 1
        return out