class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st=[]
        n=len(nums2)
        hmap={}
        for i in range(n-1,-1,-1):
            while len(st) and st[-1]<nums2[i]:
                st.pop()
            if len(st):
                hmap[nums2[i]]=st[-1]
            else:
                hmap[nums2[i]]=-1
            st.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i]=hmap[nums1[i]]
        return nums1


        