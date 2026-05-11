class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_hash = Counter(s1)
        s2_hash = Counter(s2[:len(s1)])
        left = 0

        if s1_hash == s2_hash:
            return True
        

        for right in range(len(s1), len(s2)):
            s2_hash[s2[right]] += 1
            s2_hash[s2[left]] -= 1
            if s2_hash[s2[left]] <= 0:
                del s2_hash[s2[left]]
            if s1_hash == s2_hash:
                return True
            left += 1

        return False
