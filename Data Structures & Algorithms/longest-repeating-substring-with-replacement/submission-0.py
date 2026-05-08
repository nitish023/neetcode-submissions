class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, l, max_freq = 0, 0, 0

        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            
            for freq in counts.values():
                max_freq = max(max_freq, freq)

            if (r-l+1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
                
            ans = max(ans, r-l+1)
        
        return ans
            
            

                