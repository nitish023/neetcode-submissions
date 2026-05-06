class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupls = set()
        for num in nums:
            if num in dupls:
                return True
            dupls.add(num)
        
        return False