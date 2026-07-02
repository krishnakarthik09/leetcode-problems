class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        org=x
        while x>0:
            d=x%10
            rev=rev*10+d
            x=x//10
        if rev==org:
            return True
        return False
        