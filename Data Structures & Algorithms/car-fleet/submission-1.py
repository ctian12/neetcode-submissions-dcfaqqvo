class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            hours = (target - pos) / spd
            if not stack or hours > stack[-1]:
                stack.append(hours)

        return len(stack)