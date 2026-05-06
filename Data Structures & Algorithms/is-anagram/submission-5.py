class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            if t[i] not in t_dict:
                t_dict[t[i]] = 0

            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        for j in s_dict:
            if s_dict[j] != t_dict.get(j, 0):
                return False
        
        return True
 


