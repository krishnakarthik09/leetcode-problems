class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        start=intervals[0][0]
        end=intervals[0][1]
        count=0
        for i in range(1,n):
            ns=intervals[i][0]
            ne=intervals[i][1]
            if ns<end and ne<end:
                count+=1
                start=intervals[i][0]
                end=intervals[i][1]
            elif ns<end:
                count+=1
            else:
                start=intervals[i][0]
                end=intervals[i][1]
        return count

        