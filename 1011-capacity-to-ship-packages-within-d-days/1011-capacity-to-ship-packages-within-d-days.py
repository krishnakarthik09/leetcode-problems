class Solution:
    def calculateweight(self, weights,mid):
        n=len(weights)
        count=0
        Days=0
        for i in range(0,n):
            count+=weights[i]
            if count>mid:
                Days+=1
                count=weights[i]
        Days+=1
        return Days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=high
        while low<=high:
            mid=(low+high)//2
            rem=self.calculateweight(weights,mid)
            if rem<=days:
                ans=mid
                high=mid-1
             
            else:
                low=mid+1
        return ans
            
        