class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(0,n):
            if count==0:
                count=1
                el=nums[i]
            elif nums[i]==el:
                count+=1
            elif nums[i]!=el:
                count-=1
        return el
        