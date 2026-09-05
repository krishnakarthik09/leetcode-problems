class Solution:
    def divisor(self ,bloomDay,mid,k):
        n=len(bloomDay)
        count1=0
        count2=0
        for i in range(0,n):
            if mid >= bloomDay[i]:
                count1+=1
                if count1==k:
                    count2+=1
                    count1=0
            else:
                count1=0
        return count2

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n:
            return -1
        ans=-1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            count2=self.divisor(bloomDay,mid,k)
            if count2>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans



        