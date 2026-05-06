class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        num_map = defaultdict(list)
        for num in nums:
            
            if (num-1) not in num_set:
                if num not in num_map[num]:
                    num_map[num].append(num)
            else:
                k = num
                while (k-1) in num_set:
                    k -= 1
                if num not in num_map[k]:
                    num_map[k].append(num)
       
        
        ans = 0 
        for i in num_map.values():
            ans = max(ans, len(i))

        print(num_map)
        return ans