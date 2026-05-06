class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(int)
        for ind, num in enumerate(nums):
            if target-num in indices:
                return [indices[target-num], ind]
            indices[num] = ind
        
        return [-1, -1]