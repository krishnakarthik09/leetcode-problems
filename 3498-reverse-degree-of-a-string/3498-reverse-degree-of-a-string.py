class Solution:
    def reverseDegree(self, s: str) -> int:
        n=len(s)
        total=0
        for i in range(n):
            indst=i+1
            reverseind=26+ord('a')-ord(s[i])
            total+=indst*reverseind
        return total
        