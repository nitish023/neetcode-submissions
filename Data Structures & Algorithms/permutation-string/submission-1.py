class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        l = 0

        for s in s1:
            index = ord(s) - ord('a')
            s1_arr[index] += 1

        for r in range(len(s1)):
            index = ord(s2[r]) - ord('a')
            s2_arr[index] += 1
        
        if s1_arr == s2_arr:
                return True
      
        for r in range(len(s1), len(s2)):
            index_r = ord(s2[r]) - ord('a')
            index_l = ord(s2[l]) - ord('a')
            s2_arr[index_r] += 1
            s2_arr[index_l] -= 1
            if s1_arr == s2_arr:
                return True
            l += 1
            

        return False
            
