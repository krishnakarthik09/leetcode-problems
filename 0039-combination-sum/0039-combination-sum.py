class Solution:
    def solve(self,ind,total,subset,target,candidates,result):
        if total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        elif ind>=len(candidates):
            return
        Sum=total+candidates[ind]
        subset.append(candidates[ind])
        self.solve(ind,Sum,subset,target,candidates,result)
        e=subset.pop()
        Sum=total
        self.solve(ind+1,Sum,subset,target,candidates,result)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ind=0
        result=[]
        subset=[]
        total=0
        self.solve(ind,total,subset,target,candidates,result)
        return result


        