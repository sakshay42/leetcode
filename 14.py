class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min([len(x) for x in strs]) 
        out =""
        for i in range(n):
            z = strs[0][i]
            for string in strs:
                if string[i]!=z:
                    return out
            out +=z
        return out
