class Solution:
    def getMaxArea(self, arr):
        # code here
        n=len(arr)
        st=[]
        maxarea=0
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                nse=i
                el=st[-1]
                st.pop()
                if st:
                    pse=st[-1]
                else:
                    pse=-1
                area=arr[el]*(nse-pse-1)
                maxarea=max(maxarea,area)
            st.append(i)
        while st:
            nse=n
            el=st.pop()
            if st:
                pse=st[-1]
            else:
                pse=-1
            area=arr[el]*(nse-pse-1)
            maxarea=max(maxarea,area)
        return maxarea
        
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        rows=len(matrix)
        maximal=0
        cols=len(matrix[0])
        for i in range(0,rows):
            for j in range(cols):
                if i!=0 and int(matrix[i][j])!=0:
                    matrix[i][j]=int(matrix[i][j])+int(matrix[i-1][j])
                else:
                    matrix[i][j]=int(matrix[i][j])
            area=self.getMaxArea(matrix[i])
            maximal=max(maximal,area)
        return maximal

            
        
                
        