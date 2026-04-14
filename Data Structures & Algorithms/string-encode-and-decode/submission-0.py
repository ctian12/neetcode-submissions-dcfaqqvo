class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += string
            out += '|'
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        word = ""
        for c in s:
            if c == '|':
                out.append(word)
                word = ""
            else:
                word += c
        
        return out
