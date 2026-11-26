class Solution:
    def canAliceWin(self, n: int) -> bool:
        i=10
        turn=0
        while n:
            if turn%2==0 and i>n:
                return False
            elif turn%2==1 and i>n:
                return True
            n-=i
            i-=1
            turn+=1
        if turn%2==1:
            return True
        return False
            


        