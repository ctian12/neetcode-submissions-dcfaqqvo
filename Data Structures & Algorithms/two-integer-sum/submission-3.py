class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = defaultdict()

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in need:
                return([need[remain], i])
            need[nums[i]] = i
        
        return