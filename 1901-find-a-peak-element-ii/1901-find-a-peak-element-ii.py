class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        low=0
        high=n-1
        while low<=high:
            maxi=-1
            maxiind=-1
            mid=(low+high)//2
            for i in range(m):
                if mat[i][mid]>maxi:
                    maxiind=i
                    maxi=mat[i][mid]
            left=-1
            right=-1
            if mid-1>=0:
                left=mat[maxiind][mid-1]
            if mid+1<n:
                right=mat[maxiind][mid+1]
            if maxi>left and maxi>right:
                return [maxiind,mid]
            if right>maxi:
                low=mid+1
            else:
                high=mid-1
        return [-1,-1]
                
               