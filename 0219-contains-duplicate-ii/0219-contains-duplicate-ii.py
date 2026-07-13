class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        h={}
        for i in range(0,n):
            if nums[i] in h:
                if i-h[nums[i]]<=k:
                    return True
                else:
                    h[nums[i]]=i
            else:
                h[nums[i]]=i
        return False

        