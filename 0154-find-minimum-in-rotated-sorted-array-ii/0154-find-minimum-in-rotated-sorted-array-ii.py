class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        val=float("inf")
        while low<=high:
            mid=(low+high)//2
            val=min(val,nums[mid])
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1
        return val
        