class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        curr=0
        seen={0:1}
        for i in range(0,n):
            curr+=nums[i]
            if curr-k in seen:
                count+=seen[curr-k]
            seen[curr]=seen.get(curr,0)+1
        return count
        