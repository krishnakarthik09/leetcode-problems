class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        total=float("-inf")
        s=0
        for i in range(0,n):
            s+=nums[i]
            total=max(total,s)
            if s<0:
                s=0
        return total

        