class Solution:
    def divisor(self,nums,mid):
        count=0
        for i in range(0,len(nums)):
            count+=(nums[i]+mid-1)//mid
        return count
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        high=max(nums)
        low=1
        ans=high
        while low<=high:
            mid=(low+high)//2
            rem=self.divisor(nums,mid)
            if rem<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

        