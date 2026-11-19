class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        changesmallers=nums[n-1]-nums[2]
        changelargers=nums[n-3]-nums[0]
        changeSmallLarge=nums[n-2]-nums[1]
        return min(changesmallers,changelargers,changeSmallLarge)

        