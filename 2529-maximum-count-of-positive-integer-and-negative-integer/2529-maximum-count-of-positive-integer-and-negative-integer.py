class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        ub=n
        lb=0
        low=0
        high=n-1
        flag=False
        while low <= high:
            mid=(low+high)//2
            if nums[mid]<=-1:
                lb=mid
                flag=True
                low=mid+1
            else:
                high=mid-1
        low=0
        high=n-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid]>=1:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        if flag:
            ne=lb+1 
        else:
            ne=lb
        ps=n-ub
        return max(ne,ps)
        
        
        