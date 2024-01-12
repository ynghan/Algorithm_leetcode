class Solution:
    # [3, 4, 5, 2]
    # 가장 큰 두 수를 찾는다.
    # 그 값을 계산하고 반환한다.
    def maxProduct(self, nums: List[int]) -> int:
        # 힙 리스트를 만든다.
        heap = []
        # nums 배열의 요소들을 차례대로 heap에 넣는다.
        for n in nums:
            # max_heap으로 만들기 위해 2개의 인자를 사용한다.
            # 첫 번째 인자는 max_heap으로 만들기 위한 정렬 전략
            # 두 번째 인자는 기존의 nums 요소 값
            heapq.heappush(heap, (-n, n))

        # 이제 heappop을 통해 가장 큰 두 수를 반환한다.
        # 이때, heap에는 두 개의 요소가 하나의 쌍으로 되어 있으므로,
        # 실제 값인 두 번째 요소를 반환한다.
        i = heapq.heappop(heap)[1]
        j = heapq.heappop(heap)[1]

        result = (i - 1) * (j - 1)
        
        return result
        