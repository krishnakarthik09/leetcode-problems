class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ex=[]
        for i in range(n):
            if i==0:
                ex.append('.')
            else:
                ex.append('#')
        mat=[ex for _ in range(m-1)]
        ex2=['.' for _ in range(n)]
        mat.append(ex2)
        for i in range(len(mat)):
            mat[i]="".join(mat[i])
        return mat

        # for i in range(n):
        #     if i==0:
        #         ex+="."
        #     else:
        #         ex+="#"
        # mat=[ex for i in range(m-1)]
        # ex=""
        # for _ in range(n):
        #     ex+="."
        # mat.append(ex)
        # return mat


        # for row in range(m):
        #     for col in range(n):
        #         if (col==0 and row<m) or row==m-1:
        #             mat[row]+="."
        #         else:
        #             mat[row]+="#"
        # return mat

       
        