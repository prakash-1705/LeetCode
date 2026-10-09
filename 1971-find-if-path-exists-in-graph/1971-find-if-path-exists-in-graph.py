
from collections import deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

        return False