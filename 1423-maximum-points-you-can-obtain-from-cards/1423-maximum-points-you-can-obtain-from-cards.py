class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=0
        for i in range(n):
            total+=cardPoints[i]
        curr=0
        for i in range(n-k):
            curr+=cardPoints[i]
        maxi=total-curr
        for j in range(k):
            curr-=cardPoints[j]
            curr+=cardPoints[j+n-k]
            maxi=max(total-curr,maxi)
        return maxi

        
        

        