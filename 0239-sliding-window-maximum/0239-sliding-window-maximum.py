from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        que=deque()
        n=len(nums)
        ans=[]
        for i in range(0,n):
            if que and que[0]<=i-k:
                que.popleft()
            while que and nums[que[-1]]<=nums[i]:
                que.pop()
            que.append(i)
            if i>=k-1:
                ans.append(nums[que[0]])
        return ans




        