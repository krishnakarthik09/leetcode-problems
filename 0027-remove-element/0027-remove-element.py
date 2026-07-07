class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        count=0
        while i<=j:
            if nums[i]!=val:
                i+=1
            if nums[j]==val:
                count+=1
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]

        return n-count     
        