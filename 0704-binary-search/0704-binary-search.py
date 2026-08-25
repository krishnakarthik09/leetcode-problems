class Solution:
    def BinarySearch(self,nums,low,high,target):
        if low>high:
            return -1
        mid =(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.BinarySearch(nums,low,mid-1,target)
        else:
            return self.BinarySearch(nums,mid+1,high,target)
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        return self.BinarySearch(nums,low,high,target)