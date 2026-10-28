class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        n=len(nums)
        def backtrack(ind,subset):
            if ind>=n:
                result.append(subset.copy())
                return 
            subset.append(nums[ind])
            backtrack(ind+1,subset)
            subset.pop()
            backtrack(ind+1,subset)
        backtrack(0,[])
        return result
        