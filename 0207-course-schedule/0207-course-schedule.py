class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            graph[n2].append(n1)

        visited = set()
        traced = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)

            return True

        print(graph)
        for x in list(graph):
            if not dfs(x):
                return False
        return True