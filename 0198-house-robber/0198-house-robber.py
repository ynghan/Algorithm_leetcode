from typing import List


class Solution:
    # 2 1 1 2

    # 2
    # 2 or 1
    # 2 or 3
    # 3 or 4

    # 2 2 3 4
    def rob(self, nums: List[int]) -> int:
        memo = dict()
        max_sum = nums[0]

        for i in range(len(nums)):
            if i == 0:
                memo[i] = nums[i]
            elif i == 1:
                memo[i] = max(nums[i], memo[0])
            else:
                memo[i] = max(memo[i-1], memo[i-2] + nums[i])

            if memo[i] > max_sum:
                max_sum = memo[i]

        return max_sum