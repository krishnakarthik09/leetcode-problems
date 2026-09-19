class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res=""
        strs.sort()
        fast=strs[0]
        last=strs[len(strs)-1]
        i=0
        j=0
        while i<len(fast) and j<len(last):
            if fast[i]==last[j]:
                res+=fast[i]
                i+=1
                j+=1
            else:
                break
        return res

        