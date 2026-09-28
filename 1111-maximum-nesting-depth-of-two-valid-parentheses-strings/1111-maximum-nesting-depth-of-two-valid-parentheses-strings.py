class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n=len(seq)
        res=[]
        depth=0
        for i in range(n):
            if seq[i]=="(" :
                res.append(depth%2)
                depth+=1
            else:
                depth-=1
                res.append(depth%2)
        return res
                
            

        