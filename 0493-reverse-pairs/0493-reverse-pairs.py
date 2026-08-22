class Solution:
    def merge(self,left,right):
        n=len(left)
        m=len(right)
        i=0
        j=0
        res=[]
        while i<n and j<m:
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while i<n:
            res.append(left[i])
            i+=1
        while j<m:
            res.append(right[j])
            j+=1
        return res
    def mergesort(self,arr):
        if len(arr)==1:
            return arr
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        left=self.mergesort(left_half)
        right=self.mergesort(right_half)
        n=len(left)
        m=len(right)
        i=0
        j=0
        prev_count=0
        while i<n and j<m:
            if left[i]>2*right[j]:
                prev_count+=1
                j+=1
            else:
                self.count+=prev_count
                i+=1
        while i<n:
            self.count+=prev_count
            i+=1
        prev_count=0
        return self.merge(left,right)
    def reversePairs(self, nums: List[int]) -> int:
        self.count=0
        self.mergesort(nums)
        return self.count
        
       