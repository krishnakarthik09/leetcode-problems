class Solution:
    def candy(self, ratings: list[int]) -> int:
        n=len(ratings)
        ans=1
        i=1
        while i<n:
            if ratings[i]==ratings[i-1]:
                ans+=1
                i+=1
                continue
            peak=1
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                ans+=peak
                i+=1
            down=1
            while i<n and ratings[i-1]>ratings[i]:
                
                ans+=down
                down+=1
                i+=1
            if down>peak:
                ans+=(down-peak)
        return ans
        
            
       

       