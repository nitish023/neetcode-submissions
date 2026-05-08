class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, l = 0, 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        chars = set(s[l])
        for r in range(1, len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            ans = max(ans, r-l+1)
        
        return ans
