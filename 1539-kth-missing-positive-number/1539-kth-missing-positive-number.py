class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        j=0
        i=1
        while j<n:
            Xor=(i)^arr[j]
            if Xor==0:
                i+=1
                j+=1
            elif Xor!=0:
                k-=1
                if k==0:
                    return i
                i+=1
        if k>0:
            return arr[n-1]+k

    