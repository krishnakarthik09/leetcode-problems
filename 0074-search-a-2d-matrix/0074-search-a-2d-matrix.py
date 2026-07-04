class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        matrix1=[]
        for i in range(n):
            matrix1+=matrix[i]
        s=len(matrix1)
        low=0
        high=s-1
        while low <= high:
            mid=(low+high)//2
            if matrix1[mid]==target:
                return True
            elif matrix1[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False
        