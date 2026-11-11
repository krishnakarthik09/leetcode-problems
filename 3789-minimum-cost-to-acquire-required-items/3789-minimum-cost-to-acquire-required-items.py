class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        maxneed=max(need1,need2)
        Bothcost=maxneed*costBoth
        Need1cost=need1*cost1
        Need2cost=need2*cost2
        totalcost=Need1cost+Need2cost
        combined=0
        if need1>need2:
            commoncost=need2*costBoth
            remaining=(need1-need2)*cost1
            combined=commoncost+remaining
        else:
            commoncost=need1*costBoth
            remaining=(need2-need1)*cost2
            combined=commoncost+remaining

        return min( Bothcost,totalcost,combined)
        