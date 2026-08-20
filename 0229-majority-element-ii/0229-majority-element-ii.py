class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        count1=0
        count2=0
        el1=float("-inf")
        el2=float("inf")
        for i in range(0,n):
            if count1==0 and nums[i]!=el2:
                count1=1
                el1=nums[i]
            elif count2==0 and nums[i]!=el1:
                count2=1
                el2=nums[i]
            elif nums[i]==el1:
                count1+=1
            elif nums[i]==el2:
                count2+=1
            else:
                count1-=1
                count2-=1
        count1=0
        count2=0
        for i in range(0,n):
            if nums[i]==el1:
                count1+=1
            if nums[i]==el2:
                count2+=1
        if count1>(n//3):
            res.append(el1)
        if count2>(n//3):
            res.append(el2)
        return res


