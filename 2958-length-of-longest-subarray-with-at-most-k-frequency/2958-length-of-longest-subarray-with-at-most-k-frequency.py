class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        seen={}
        max_count=0
        left=0
        for right in range(0,n):
            seen[nums[right]]=seen.get(nums[right],0)+1
            while seen[nums[right]]>k:
                seen[nums[left]]-=1
                if seen[nums[left]]==0:
                    del seen[nums[left]]
                left+=1
            max_count=max(max_count,right-left+1)
        return max_count
