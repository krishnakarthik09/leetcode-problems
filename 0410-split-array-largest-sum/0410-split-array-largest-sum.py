class Solution:
    def possibletoarrange(self, nums ,k ,mid):
        n=len(nums)
        sb=1
        total=0
        for i in range(0,n):
            if nums[i]>mid:
                return False
            if (total+nums[i])>mid:
                sb+=1
                total=nums[i]
            else:
                total+=nums[i]
        if sb>k:
            return False
        return True
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        low=min(nums)
        high=sum(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.possibletoarrange(nums,k,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return low
        