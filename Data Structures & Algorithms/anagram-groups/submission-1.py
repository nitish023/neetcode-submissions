class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict = defaultdict(list)
        
        for str in strs:
            str_key = "".join(sorted(str))
            sort_dict[str_key].append(str)
        
        return list(sort_dict.values())