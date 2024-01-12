class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(res, [], 1, n, k)
        return res

    def backtracking(self, res, subset, start, n, k):
        if len(subset) == k:
            res.append(subset[:])
            return

        for i in range(start, n + 1):
            subset.append(i)
            self.backtracking(res, subset, i + 1, n, k)
            subset.pop()