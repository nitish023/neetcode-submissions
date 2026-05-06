class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1], [1]
        ans = []
        for num in nums[:-1]: 
            pre.append(num*pre[-1])
        
        for num in nums[::-1][:-1]:
            post.append(num*post[-1])

        post = post[::-1]
        for i in range(len(pre)):
            ans.append(pre[i] * post[i])

        return ans