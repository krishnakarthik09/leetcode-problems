class Solution:
    def solve(self,ind,total,paren,result):
        if ind>=len(paren):
            if total==0:
                result.append("".join(paren))
            return
        if total>len(paren)//2 or total<0:
            return
        paren[ind]="("
        Sum=total+1
        self.solve(ind+1,Sum,paren,result)
        paren[ind]=")"
        Sum=total-1
        self.solve(ind+1,Sum,paren,result)
    def generateParenthesis(self, n: int) -> list[str]:
        paren=[""]*2*n
        result=[]
        ind=0
        total=0
        self.solve(ind,total,paren,result)
        return result

        