class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n=len(nums)
        count=0
        mini=nums[0]
        for i in range(1,n):
            mini=min(mini,nums[i])
        for i in range(n):
            count+=nums[i]-mini
        return count
        