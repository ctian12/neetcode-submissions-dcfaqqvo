class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        out = 0

        for c in charSet:
            l = r = 0
            remaining = k

            while r < len(s):
                if s[r] != c:
                    remaining -= 1
                
                while remaining < 0:
                    if s[l] != c:
                        remaining += 1
                    l += 1
                
                out = max(out, r - l + 1)
                r += 1
        
        return out