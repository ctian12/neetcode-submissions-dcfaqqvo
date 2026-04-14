class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        net = gas[start] - cost[start]
        while start > end:
            if net < 0:
                start -= 1
                net += gas[start] - cost[start]
            else:
                net += gas[end] - cost[end]
                end += 1
        return start if net >= 0 else -1
            