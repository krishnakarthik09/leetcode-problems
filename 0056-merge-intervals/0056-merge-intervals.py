class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        if n==1:
            return intervals
        res=[]
        intervals.sort()
        [start,end]=intervals[0]
        for i in range(0,n):
            [newstart,newend]=intervals[i]
            if newstart<=end:
                end=max(end,newend)
            else:
                res.append([start,end])
                [start,end]=[newstart,newend]
        res.append([start,end])
        return res


        