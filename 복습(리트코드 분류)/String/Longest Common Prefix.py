import functools

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def getCommonPrefix(a, b):
            min_len = min(len(a), len(b))
            
            common = ""
            for i in range(min_len):
                if a[i] == b[i]: common += a[i]
                else: break

            return common

        return functools.reduce(getCommonPrefix, strs)