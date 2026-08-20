class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(1,numRows+1):
            temp=[1]
            ans=1
            for j in range(1,i):
                ans=ans*(i-j)
                ans=ans//j
                temp.append(ans)
            res.append(temp)
        return res



        