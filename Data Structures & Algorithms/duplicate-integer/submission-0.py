class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = set()
        for x in nums:
            if x not in i:
                i.add(x)
            else:
                return True
        return False
         