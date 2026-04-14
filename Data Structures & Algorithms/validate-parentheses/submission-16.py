class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(" : ")", "[" : "]", "{" : "}"
            }
        stack = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(d[c])
            else:
                if len(stack) == 0 or c != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) != 0:
            return False

        return True