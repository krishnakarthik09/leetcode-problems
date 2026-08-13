class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        count=0
        for j in range(1,n): 
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
            else:
                count+=1
        return n-count
        
        

        