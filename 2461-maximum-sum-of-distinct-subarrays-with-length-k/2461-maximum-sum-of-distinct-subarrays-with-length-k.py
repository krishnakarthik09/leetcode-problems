class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        my_set=set()
        max_sum=0
        curr=0
        left=0
        for right in range(0,n):
            while nums[right] in my_set:
                curr-=nums[left]
                my_set.remove(nums[left])
                left+=1
            curr+=nums[right]
            my_set.add(nums[right])
            if len(my_set)==k:
                max_sum=max(max_sum,curr)
                my_set.remove(nums[left])
                curr-=nums[left]
                left+=1
        return max_sum

        