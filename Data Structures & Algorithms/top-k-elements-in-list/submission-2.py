class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ans = []
        freqs = sorted(counts.values(), reverse=True)
        ans_freqs = freqs[0:k]
        for i in counts:
            if counts[i] in ans_freqs:
                ans.append(i)
        return ans
        