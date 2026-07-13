class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        h=set()
        for i in range(0,n):
            if nums[i] in h:
                return True
            else:
                h.add(nums[i])
        return False

        