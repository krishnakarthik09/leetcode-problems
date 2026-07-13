class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        while i< n:
            if nums[i]==0:
                break
            i+=1
        if i==n-1:
            return
        j=i+1
        while i<n-1 and j<n:
            if nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        
        