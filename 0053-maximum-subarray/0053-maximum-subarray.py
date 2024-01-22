from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = dict()

        # 최대값 저장

        # nums : -2 1 -3 4 -1 2 1 -5 4

        # -2
        # -1 or 1
        # -2 or -3
        # 2 or 4
        # 3 or -1
        # 5 or 2
        # 6 or 1
        # 1 or -5
        # 5 or 4

        # memo : -2 1 -2 4 3 5 6 1 5

        max_sum = nums[0]
        for i in range(len(nums)):
            if i == 0:
                memo[i] = nums[i]
            elif nums[i] > nums[i] + memo[i-1]:
                memo[i] = nums[i]
            else:
                memo[i] = nums[i] + memo[i-1]

            if max_sum < memo[i]:
                max_sum = memo[i]

        return max_sum