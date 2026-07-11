class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        ind=0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                ind=i
                break
        low=0
        high=ind-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        low=ind
        high=n-1
        while low <= high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False

        
        