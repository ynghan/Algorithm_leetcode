class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    # mat의 각각의 행들 중에 가장 약한 k개의 행을 리스트로 반환하시오.
        heap = []
        result = []
        idx = 0
        for n in mat:
            count = 0
            for i in n:
                if i == 1:
                    count += 1
                else:
                    break

            heapq.heappush(heap, (count, idx))
            idx += 1

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result