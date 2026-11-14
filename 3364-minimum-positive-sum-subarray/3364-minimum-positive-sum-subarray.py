class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        min_sum = float("inf")

        for i in range(n):
            summ = 0

            for j in range(i, min(n, i + r)):
                summ += nums[j]

                length = j - i + 1

                if l <= length <= r and summ > 0:
                    min_sum = min(min_sum, summ)

        return min_sum if min_sum != float("inf") else -1