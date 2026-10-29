class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=set()
        n=len(nums)
        def backtrack(ind,subset):
            if ind>=n:
                result.add(tuple(subset.copy()))
                return 
            subset.append(nums[ind])
            backtrack(ind+1,subset)
            subset.pop()
            backtrack(ind+1,subset)
        backtrack(0,[])
        return [list(i) for i in result]
        