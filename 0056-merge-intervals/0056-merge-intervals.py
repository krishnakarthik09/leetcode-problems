class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n==1:
            return intervals
        res=[]
        intervals.sort()
        for i in range(0,n):
            if len(res)!=0 and intervals[i][0]<= res[len(res)-1][1]:
                res[len(res)-1][1]=max(intervals[i][1],res[len(res)-1][1])
            else:
                res.append(intervals[i])
        return res


        