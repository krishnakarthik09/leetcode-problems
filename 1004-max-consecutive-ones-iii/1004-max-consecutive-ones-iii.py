class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        count=0
        max_count=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                k-=1
            while left<=i and k==-1:
                if nums[left]==0:
                    k+=1
                left+=1
                count-=1
            count+=1
            max_count=max(max_count,count)
        return max_count
        