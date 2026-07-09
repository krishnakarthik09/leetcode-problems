class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        start=0
        i=0
        j=0
        while i <  n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                start+=1
                i=start
                j=0
            if j==m:
                return start
        return -1

        
        