class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        st=[]
        maxarea=0
        for i in range(n):
            while st and heights[st[-1]]>heights[i]:
                el=heights[st[-1]]
                st.pop()
                nse=i
                if st:
                    pse=st[-1]
                else:
                    pse=-1
                area=el*(nse-pse-1)
                maxarea=max(maxarea,area)
            st.append(i)
        if st:
            while st:
                nse=n
                el=heights[st[-1]]
                st.pop()
                if st:
                    pse=st[-1]
                else:
                    pse=-1
                area=el*(nse-pse-1)
                maxarea=max(maxarea,area)
                
        return maxarea
        