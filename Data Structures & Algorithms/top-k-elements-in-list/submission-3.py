class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        arr = []
        
        for num, cts in counts.items():
            arr.append([cts, num])
        
        arr.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res
        