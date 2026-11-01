class Solution:
    def backtrack(self,ind,total,nums,subset,result):
        if total==0:
            result.append(subset.copy())
            return
        if total<0 or ind>=len(nums):
            return
        for i in range(ind,len(nums)):
            if i>ind and nums[i]==nums[i-1]:
                continue
            Sum=total-nums[i]
            subset.append(nums[i])
            self.backtrack(i+1,Sum,nums,subset,result)
            subset.pop()
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result=[]
        self.backtrack(0,target,candidates,[],result)
        return result




        