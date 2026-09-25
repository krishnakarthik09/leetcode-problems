class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        maxlen=0
        leftmax=-1
        rightmax=-1
        for i in range(0,n):
            left=i
            right=i
            while left>=0 and right<n:
                if s[left]!=s[right]:
                    break
                if maxlen<(right-left+1):
                    leftmax=left
                    rightmax=right
                    maxlen=right-left+1
                left-=1
                right+=1
            right=i+1
            left=i
            while left>=0 and right<n:
                if s[left]!=s[right]:
                    break
                if maxlen<(right-left+1):
                    maxlen=right-left+1
                    leftmax=left
                    rightmax=right
                left-=1
                right+=1
        return s[leftmax:rightmax+1]
            