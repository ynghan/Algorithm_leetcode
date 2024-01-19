"""
m x n 정수 행렬 행렬에서 목표 값을 검색하는 효율적인 알고리즘을 작성하세요.
이 행렬에는 다음과 같은 속성이 있습니다.
각 행의 정수는 왼쪽에서 오른쪽으로 오름차순으로 정렬됩니다.
각 열의 정수는 위에서 아래로 오름차순으로 정렬됩니다.
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # matrix의 각 행의 첫 번째 값 < target
        # matrix의 각 행의 마지막 값 > target
        row = 0
        col = 0
        start_row = 0
        end_row = len(matrix) - 1

        while start_row < end_row:
            if matrix[start_row][0] > target or matrix[start_row][-1] < target:
                start_row += 1
            elif matrix[end_row][0] > target or matrix[end_row][-1] < target:
                end_row -= 1
            else:
                break

        # 가능한 행의 범위 내에서 반복문으로 해당 값과 일치하는 행과 열을 찾는다.
        for i in range(start_row, end_row + 1):
            start = 0
            end = len(matrix[i]) - 1
            while start <= end:
                if matrix[i][end] > target:
                    end -= 1
                elif matrix[i][start] < target:
                    start += 1
                else:
                    row = i
                    col = start
                    break

        # 검색 값이 일치하면 true
        if target == matrix[row][col]:
            return True
        return False


res = Solution().searchMatrix([[-1,3]], 3)
print(res)