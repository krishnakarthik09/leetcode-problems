class Solution:
    def nse(self,arr,n):
        st=[]
        nse=[0]*n
        for j in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[j]:
                st.pop()
            
            if st:
                nse[j]=st[-1]
            else:
                nse[j]=n
            st.append(j)
        return nse
    def pse(self,arr,n):
        st=[]
        pse=[0]*n
        for j in range(n):
            while st and arr[st[-1]]>arr[j]:
                st.pop()
            if st:
                pse[j]=st[-1]
            else:
                pse[j]=-1
            st.append(j)
        return pse
        

    def sumSubarrayMins(self, arr: list[int]) -> int:
        n=len(arr)
        nse=self.nse(arr,n)
        pse=self.pse(arr,n)
        total=0
        mod=(10**9)+7
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            total+=(left*right*arr[i])
        return total%mod

        