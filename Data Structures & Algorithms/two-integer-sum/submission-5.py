class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict:
                return [dict[diff], i]
            dict[num] = i

        return