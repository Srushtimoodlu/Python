class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        def dfs(u):
            suspicious[u] = True
            for v in graph[u]:
                if not suspicious[v]:
                    dfs(v)

        def dfs2(u):
            visited[u] = True
            for v in undirected[u]:
                if not visited[v]:
                    suspicious[v] = False
                    dfs2(v)

        graph = [[] for _ in range(n)]
        undirected = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)
            undirected[a].append(b)
            undirected[b].append(a)

        suspicious = [False] * n
        dfs(k)

        visited = [False] * n
        for i in range(n):
            if not suspicious[i] and not visited[i]:
                dfs2(i)

        return [i for i in range(n) if not suspicious[i]]       