class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        lb=-1
        ub=n
        low=0
        high=n-1
        flag=True
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                flag=False
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        if flag:
            return [-1,-1]
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return [lb,ub-1]
        
        
