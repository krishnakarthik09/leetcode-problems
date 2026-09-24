class Solution:
    def palindrome(self, s, left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        left=0
        right=n-1
        while left<right:
            if s[left]!=s[right]:
                break
            left+=1
            right-=1
        if right-left==1:
            return True
        return self.palindrome(s,left+1,right) or self.palindrome(s,left,right-1)

        