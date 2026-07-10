class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        for i in nums:
            total+=i
        total_s=n*(n+1)//2
        return total_s-total
        