class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        chars = {}
        for c in t:
            chars[c] = chars.get(c, 0) + 1

        window = {}
        have = 0
        need = len(chars)

        res = ""
        res_len = float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in chars and window[c] == chars[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in chars and window[s[l]] < chars[s[l]]:
                    have -= 1
                l += 1

        return res