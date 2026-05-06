class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_set = set()

        for i in range(len(nums)):
            if target - nums[i] in diff_set:
                return [nums.index(target-nums[i]), i]
            else:
                diff_set.add(nums[i])
        
            