def compare(x, y):
    # x와 y를 연결했을 때, 더 큰 조합을 만드는 순으로 정렬
    option1 = x + y
    option2 = y + x
    if option1 > option2:
        return -1
    elif option1 < option2:
        return 1
    else:
        return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 정수를 문자열로 변환
        arr = [str(num) for num in nums]

        # 모든 숫자 조합 중 가장 큰 수를 만들기 위해 정렬
        arr.sort(key=cmp_to_key(compare))

        # 0만 있는 경우, "0"을 반환 (예: [0, 0] -> "0")
        if arr[0] == "0":
            return "0"

        # 정렬된 배열을 합쳐 하나의 문자열로 반환
        return ''.join(arr)