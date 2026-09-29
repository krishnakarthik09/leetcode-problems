class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        pre=1
        suff=1
        for i in range(0,n):
            if i!=0:
                pre*=nums[i-1]
            ans[i]=pre
        for j in range(n-1,-1,-1):
            if j!=n-1:
                suff*=nums[j+1]
            ans[j]*=suff
        return ans
