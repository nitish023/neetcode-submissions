class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_dict = defaultdict(int)
        for ind, num in enumerate(numbers):
            if target - num in index_dict:
                return [index_dict[target-num]+1, ind+1]
            index_dict[num] = ind
        
        return [-1, -1]