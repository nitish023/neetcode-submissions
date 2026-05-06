class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        res = ""
        for s in strs:
            sizes.append(str(len(s)))

        for size in sizes:
            res += size
            res += ','
        
        res += "#"
        for s in strs:
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        print(s)
        lengths = []
        final = []
        left = 0
        while s[left] != '#':
            cur = ""
            while s[left] != ',':
                cur += s[left]
                left += 1
            
            lengths.append(int(cur))
            left += 1
        left += 1
        
        for length in lengths:
            final.append(s[left:left+length])
            left += length
            





            

        return final