class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        char=set()
        maxi=0
        left=0
        for i in range(0,n):
            while s[i] in char:
                char.remove(s[left])
                left+=1
            char.add(s[i])
            maxi=max(maxi,i-left+1)
        return maxi
        