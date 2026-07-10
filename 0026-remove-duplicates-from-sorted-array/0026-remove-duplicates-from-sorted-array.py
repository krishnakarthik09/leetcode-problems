class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=i+1
        count=0
        if n==1:
            return
        while i<j and j < n:
            if nums[i]==nums[j]:
                j+=1
                count+=1

            elif j<n and nums[j]!=nums[i]:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
                j+=1
        k=n-count
        return k

