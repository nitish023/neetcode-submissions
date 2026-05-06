class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for i in nums:
            if i in unique_elements:
                return True
            else:
                unique_elements.add(i)
        return False         