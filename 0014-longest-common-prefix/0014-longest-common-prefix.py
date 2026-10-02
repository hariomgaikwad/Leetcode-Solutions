class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        result = ""
        base = strs[0]
        for i in range(0,len(base)):
            for chr in strs[1:]:
                if i == len(chr) or chr[i] != base[i]:
                    return result 
            result += base[i]
        return result 
        