class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        total=0
        for i in range(0,k):
            total+=nums[i]
        maxi=total/k
        i=0
        j=k-1
        while j<n-1:
            j+=1
            total+=nums[j]
            total-=nums[i]
            i+=1
            maxi=max(maxi,total/k)
        return maxi

        