class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in jewels:
            for my_jewels in stones:
                if my_jewels in char:
                    count += 1
        return count


# 해당 문제는 보석이 중복되지 않아 count를 사용해도 괜찮지만
# 파이썬은 set 함수를 사용하면 편리하다.
# set("ab") = {"a", "b"}
    def numJewels(self, jewels, stones):
        jewels = set(jewels)
        