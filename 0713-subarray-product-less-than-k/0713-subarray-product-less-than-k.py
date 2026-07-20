class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        curr=1
        max_count=0
        left=0
        for right in range(0,n):
            curr*=nums[right]
            while curr>=k:
                curr=curr/nums[left]
                left+=1
            if curr<k:
                max_count+=right-left+1
        return max_count


