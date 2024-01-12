class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)
        result = []
        answer = 0
        for pair in zip(nums[0::2], nums[1::2]):
            result.append(list(pair))
        for i in result:
            answer += min(i)
        return answer