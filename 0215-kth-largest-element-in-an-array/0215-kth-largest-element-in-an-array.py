class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        result = 0
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        result = heapq.heappop(nums)
        return result