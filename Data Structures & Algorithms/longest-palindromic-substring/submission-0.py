class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ""

        #odd length palindrome check
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            substring = s[l + 1:r]
            if len(substring) > len(out):
                out = substring
        
        #even length palindrome check
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            substring = s[l + 1:r]
            if len(substring) > len(out):
                out = substring
        
        return out
