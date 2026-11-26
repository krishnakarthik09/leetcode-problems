class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
            arr=intervals.copy()
            arr.sort()
            intervals.sort(key=lambda x: (x[1]))
            i=0
            j=0
            n=len(intervals)
            maxi=-1
            count=0
            while i<n and j<n:
                if arr[i][0]<=intervals[j][1]:
                    count+=1
                    i+=1
                else:
                    count-=1
                    j+=1
                maxi=max(maxi,count)
            return maxi

        