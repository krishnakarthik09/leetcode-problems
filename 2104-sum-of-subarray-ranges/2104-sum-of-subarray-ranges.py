class Solution:
    def smallers(self,arr,n):
        nse=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                nse[i]=st[-1]
            else:
                nse[i]=n
            st.append(i)
        pse=[]
        st=[]
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                pse.append(st[-1])
            else:
                pse.append(-1)
            st.append(i)
        total=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            total+=(left*right*arr[i])
        return total
    def largers(self,arr,n):
        nle=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if st:
                nle[i]=st[-1]
            else:
                nle[i]=n
            st.append(i)
        ple=[]
        st=[]
        for i in range(n):
            while st and arr[st[-1]]<arr[i]:
                st.pop()
            if st:
                ple.append(st[-1])
            else:
                ple.append(-1)
            st.append(i)
        total=0
        for i in range(n):
            left=i-ple[i]
            right=nle[i]-i
            total+=(left*right*arr[i])
        return total
    def subArrayRanges(self, nums: list[int]) -> int:
        n=len(nums)
        return self.largers(nums,n)-self.smallers(nums,n)

        