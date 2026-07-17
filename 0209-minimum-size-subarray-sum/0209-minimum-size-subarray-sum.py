class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=0
        curr_sum=0
        mini=float("inf")
        for right in range(0,n):
            curr_sum+=nums[right]

            while curr_sum>=target:
                mini=min(mini,right-left+1)
                curr_sum-=nums[left]
                left+=1
        if mini==float("inf"):
            return 0
        return mini

        