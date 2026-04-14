class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            count = 0
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                count += 1
                ind = stack.pop()
                out[ind] = i - ind
            stack.append(i)
        
        return out
            