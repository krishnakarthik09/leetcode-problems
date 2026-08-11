class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]
        for i in range(1,n):
            temp_max=max(nums[i],curr_max*nums[i],curr_min*nums[i])
            temp_min=min(nums[i],curr_max*nums[i],curr_min*nums[i])
            curr_max = temp_max
            curr_min = temp_min
            maxi=max(maxi,curr_max)
        return maxi

        