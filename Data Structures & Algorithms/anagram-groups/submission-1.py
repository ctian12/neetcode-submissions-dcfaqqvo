class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        out = []

        for s in strs:
            freqList = [0] * 26
            for c in s:
                freqList[ord(c) - ord('a')] += 1
            d[tuple(freqList)].append(s)
        
        for key in d:
            out.append(d[key])
        
        return out