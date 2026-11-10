class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxind=nums[0]
        n=len(nums)
        for i in range(1,n):
            if i>maxind:
                return False
            maxind=max(maxind,i+nums[i])
            if maxind>=n-1:
                return True
        return True
            
            
        