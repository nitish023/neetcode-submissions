class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_dict = {}
        final_list = []

        for i in range(len(strs)):
            sorted_chars = sorted(strs[i])
            sorted_str = "".join(sorted_chars)
            if sorted_str not in final_dict:
                final_dict[sorted_str] = []
            final_dict[sorted_str].append(strs[i])
        
        for val in final_dict.values():
            final_list.append(val)

        return final_list