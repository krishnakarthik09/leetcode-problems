class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        res=""
        for i in range(n-1,-1,-1):
            digit=int(num[i])
            if digit%2!=0:
                break
        if i==0 and int(num[i]) % 2 ==0:
            return res
        for j in range(i+1):
            res+=num[j]
        return res

        