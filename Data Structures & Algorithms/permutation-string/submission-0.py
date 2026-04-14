class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1counts = [0] * 26
        s2counts = [0] * 26
        for c in s1:
            s1counts[ord(c) - ord('a')] += 1
        for i in range(len(s1)):
            s2counts[ord(s2[i]) - ord('a')] += 1
            if s1counts == s2counts:
                return True
        for l in range(len(s2) - len(s1)):
            r = l + len(s1)
            index = ord(s2[r]) - ord('a')
            s2counts[index] += 1
            index = ord(s2[l]) - ord('a')
            s2counts[index] -= 1
            print(s1counts)
            print(s2counts)
            print('-------------')
            if s1counts == s2counts:
                return True
        return False

