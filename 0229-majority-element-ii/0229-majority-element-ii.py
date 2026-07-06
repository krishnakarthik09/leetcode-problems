class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        h1={}
        for i in range(0,n):
            if nums[i] in h1:
                h1[nums[i]]+=1
            else:
                h1[nums[i]]=1
        for j in h1:
            if h1[j]>n//3:
                res.append(j)
        return res
        