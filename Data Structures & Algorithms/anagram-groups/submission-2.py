class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list)
        ans = []
        
        for s in strs:
            char_map = [0] * 26
            for i in s:
                pos = ord(i) - ord('a')
                char_map[pos] += 1

            key = tuple(char_map)
            dict[key].append(s)
        
        for value in dict.values():
            ans.append(value)

        return ans
