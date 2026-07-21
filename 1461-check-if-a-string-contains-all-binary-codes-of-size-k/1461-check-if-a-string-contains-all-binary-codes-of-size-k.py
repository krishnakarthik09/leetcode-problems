class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        my_set=set()
        for i in range(0,n-k+1):
            curr=s[i:i+k]
            my_set.add(curr)
        if len(my_set)==2**k:
            return True
        return False

        