class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        n=len(arr1)
        m=len(arr2)
        count=n
        for i in range(n):
            low=0 
            high=m-1
            while low<=high:
                mid=(low+high)//2
                if abs(arr1[i]-arr2[mid])<=d:
                    count-=1
                    break
                elif arr1[i]<arr2[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return count
        