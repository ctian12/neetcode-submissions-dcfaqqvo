class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lettermap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        out = []

        def backtrack(cur, i):
            if len(cur) == len(digits):
                out.append(''.join(cur))
                return
            for letter in lettermap[digits[i]]:
                cur.append(letter)
                backtrack(cur, i + 1)
                cur.pop()

        backtrack([], 0)
        return out