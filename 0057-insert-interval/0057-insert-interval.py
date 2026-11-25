class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n=len(intervals)
        ns=newInterval[0]
        ne=newInterval[1]
        res=[]
        i=0
        while i<n and intervals[i][1]<ns:
            res.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=ne:
            ns=min(ns,intervals[i][0])
            ne=max(ne,intervals[i][1])
            i+=1
        res.append([ns,ne])
        while i<n:
            res.append(intervals[i])
            i+=1
        return res
       