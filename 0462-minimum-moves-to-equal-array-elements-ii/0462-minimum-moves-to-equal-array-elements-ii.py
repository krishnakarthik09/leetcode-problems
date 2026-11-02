class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        median=nums[n//2]
        count=0
        for i in range(n):
            if nums[i]>=median:
                count+=nums[i]-median
            else:
                count+=median-nums[i]
        return count

        