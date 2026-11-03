class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=max(nums)
        count=0
        for i in range(n):
            count+=maxi-nums[i]
        return count
        