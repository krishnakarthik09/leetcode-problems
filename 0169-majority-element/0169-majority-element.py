class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        h={}
        for i in range(0,n):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
        for j in nums:
            if h[j]>n//2:
                return j
        