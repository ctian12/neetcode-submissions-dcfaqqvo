class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxLen = 0
        cur = set()

        while r < len(s):
            if s[r] in cur:
                while s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                cur.remove(s[l])
                l += 1
            
            cur.add(s[r])
            print(cur)
            maxLen = max(maxLen, r - l + 1)

            r += 1
        
        return maxLen