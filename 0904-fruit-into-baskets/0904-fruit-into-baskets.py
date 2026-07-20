class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        seen={}
        max_count=0
        left=0
        for right in range(0,n):
            seen[fruits[right]]=seen.get(fruits[right],0)+1
            while len(seen)>2:
                seen[fruits[left]]-=1
                if seen[fruits[left]]==0:
                    del seen[fruits[left]]
                left+=1
            max_count=max(max_count,right-left+1)
        return max_count
        