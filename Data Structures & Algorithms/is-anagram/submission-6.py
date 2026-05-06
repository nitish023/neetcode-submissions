class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range((len(s))):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        for char in s_dict:
            if s_dict[char] != t_dict[char]:
                return False
        
        return True