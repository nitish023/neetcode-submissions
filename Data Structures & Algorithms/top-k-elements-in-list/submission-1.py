class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        
        for i in range(len(nums)):
            freqs[nums[i]] += 1
        
        ans = [[] for _ in range(len(nums)+1)]

        for num, freq in freqs.items():
            ans[freq].append(num)

        print(ans)
        
        final = []
        for i in ans[::-1]:
            for num in i:
                final.append(num)
                if len(final) == k:
                    return final



        
        
                
        