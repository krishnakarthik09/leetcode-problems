class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n=len(nums)
        pres=False
        low=0
        high=n-1
        lb=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    pres=True
                lb=mid
                high=mid-1
            else:
                low=mid+1
        if not pres:
            return []
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return [i for i in range(lb,ub)]
        

        