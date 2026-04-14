class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        place = 1
        for i in range(len(digits) - 1, -1, -1):
            num += place * digits[i]
            print(num)
            place *= 10
        num += 1
        out = [int(digit) for digit in str(num)]
        return out