class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        for row in range(0,m):
            n=len(matrix[row])
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if matrix[row][mid]==target:
                    return True
                elif matrix[row][mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return False
            