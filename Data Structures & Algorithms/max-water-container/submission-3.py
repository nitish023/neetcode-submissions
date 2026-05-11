class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, ans = 0, 0
        r = len(heights)-1

        while l < r:
            short = min(heights[l], heights[r])
            area = short * (r - l)
            ans = max(ans, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            print(f'{l}-{r}')
        
        return ans