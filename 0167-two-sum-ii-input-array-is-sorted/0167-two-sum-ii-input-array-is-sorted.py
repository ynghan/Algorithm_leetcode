"""
주어진 1-indexed 정수 배열 numbers는 이미 감소하지 않는 순서로 정렬되어 있다. 
특정 target 정수에 합산되는 두 개의 숫자를 찾습니다. 
이 두 숫자를 numbers[index1]과 numbers[index2]로 둡니다. 
여기서 1 <= index1 < index2 <= numbers.length입니다.

두 숫자 index1과 index2의 인덱스를 길이 2의 정수 배열 [index1, index2]로 1씩 더한 값으로 반환합니다.

테스트는 정확히 하나의 솔루션이 있도록 생성됩니다. 동일한 요소를 두 번 사용할 수 없습니다.

솔루션은 일정한 추가 공간만 사용해야 합니다.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        input = sys.stdin.readline
        # nums = list(map(int, input().split()))
        # target = int(input())

        start = 0
        end = len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start+1, end+1]