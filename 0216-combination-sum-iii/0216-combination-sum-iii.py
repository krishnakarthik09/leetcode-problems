class Solution:
    def backtrack(self,num,total,subset,result,k,n):
        if len(subset)>=k:
            if total==n:
                result.append(subset.copy())
            return
        if total>n:
            return
        if num>9:
            return
        Sum=total+num
        subset.append(num)
        self.backtrack(num+1,Sum,subset,result,k,n)
        subset.pop()
        Sum=total
        self.backtrack(num+1,Sum,subset,result,k,n)

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        subset=[]
        total=0
        num=1
        result=[]
        self.backtrack(num,total,subset,result,k,n)
        return result

        