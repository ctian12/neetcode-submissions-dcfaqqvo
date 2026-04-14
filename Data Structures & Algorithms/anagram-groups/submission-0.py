class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            lettercounts = [0] * 26
            for c in s:
                lettercounts[ord(c) - ord('a')] += 1
            anagrams[tuple(lettercounts)].append(s)
        return list(anagrams.values())