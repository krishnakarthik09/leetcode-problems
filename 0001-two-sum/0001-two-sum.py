class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        ma={}
        for i in range(0,n):
            remain=target-nums[i]
            if remain in ma:
                return [ma[remain],i]
            else:
                ma[nums[i]]=i
        return []


        