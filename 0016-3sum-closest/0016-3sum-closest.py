class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        mini=float("inf")
        ans=-1
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==target:
                    return total
                if abs(target-total)<mini:
                    mini=abs(target-total)
                    ans=total
                if total>target:
                    k-=1
                else:
                    j+=1
        return ans
              
        