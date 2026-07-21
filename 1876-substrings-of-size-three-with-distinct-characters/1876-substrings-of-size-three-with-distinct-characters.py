class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        my_set=set()
        count=0
        left=0
        for right in range(0,n):
            while s[right] in my_set:
                my_set.remove(s[left])
                left+=1
            my_set.add(s[right])
            if len(my_set)==3:
                count+=1
                my_set.remove(s[left])
                left+=1
        return count
        