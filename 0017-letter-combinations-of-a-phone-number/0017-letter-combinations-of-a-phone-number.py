class Solution:
    def Solve(self,ind,digits,mapp,subset,result):
        if ind>=len(digits):
            result.append("".join(subset.copy()))
            return
        for i in range(len(mapp[digits[ind]])):
            subset.append(mapp[digits[ind]][i])
            self.Solve(ind+1,digits,mapp,subset,result)
            subset.pop()
    def letterCombinations(self, digits: str) -> list[str]:
        mapp={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        self.Solve(0,digits,mapp,[],result)
        return result
       


        