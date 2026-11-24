class Solution:
    def findGCD(self, nums: list[int]) -> int:
        n=len(nums)
        mini=float("inf")
        maxi=-1
        for i in range(n):
            mini=min(mini,nums[i])
            maxi=max(maxi,nums[i])
        d=mini
        while mini>0:
            if mini%d ==0 and maxi%d==0:
                return d
            d-=1
        return 1
        