class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        st=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            while len(st) and st[-1]<=nums[i]:
                st.pop()
            st.append(nums[i])
        for i in range(n-1,-1,-1):
            while len(st) and st[-1]<=nums[i]:
                st.pop()
            value=nums[i]
            if len(st):
                nums[i]=st[-1]
            else:
                nums[i]=-1
            st.append(value)
        return nums

        

        