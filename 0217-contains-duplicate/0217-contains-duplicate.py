class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        h={}
        for i in range(0,n):
            if nums[i] in h:
                return True
            else:
                h[nums[i]]=1
        return False

        