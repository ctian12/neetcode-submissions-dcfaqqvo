class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = []
        for c in s:
            chars.append(c)
        for ch in t:
            if ch in chars:
                chars.remove(ch)
            else:
                return False
        return len(chars) == 0