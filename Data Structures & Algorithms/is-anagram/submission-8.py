class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = [0] * 26
        tArray = [0] * 26

        for i in range(len(s)):
            sArray[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            tArray[ord(t[i]) - ord('a')] += 1
        
        return sArray == tArray