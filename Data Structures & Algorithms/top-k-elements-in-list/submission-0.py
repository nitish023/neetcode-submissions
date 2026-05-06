class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        result = []
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)
     
        for num, c in num_dict.items():
            freq[c].append(num)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
            
