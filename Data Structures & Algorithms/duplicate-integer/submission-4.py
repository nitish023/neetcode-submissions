class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for i in nums:
            if i not in unique_elements:
                unique_elements.add(i)     
            else:
                return True    
        return False
                