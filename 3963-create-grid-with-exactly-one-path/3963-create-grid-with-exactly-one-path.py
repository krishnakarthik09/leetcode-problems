class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        mat=["" for i in range(m)]
        for row in range(m):
            for col in range(n):
                if (col==0 and row<m) or row==m-1:
                    mat[row]+="."
                else:
                    mat[row]+="#"
        return mat

       
        