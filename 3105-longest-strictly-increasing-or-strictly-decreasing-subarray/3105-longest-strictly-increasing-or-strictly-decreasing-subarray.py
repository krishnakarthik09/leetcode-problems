class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count1=1
        count2=1
        max_count=1
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                count1+=1
                count2=1
            elif nums[i-1]>nums[i]:
                count1=1
                count2+=1
            else:
                count1=1
                count2=1
            max_count=max(max_count,count1,count2)
        return max_count

            

            





        