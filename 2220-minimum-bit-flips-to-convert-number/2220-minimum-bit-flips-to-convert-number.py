class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start==goal:
            return 0
        ans=start^goal
        count=1
        while ans > 1:
            if ans%2==1:
                count+=1
            ans=ans//2
        return count
        