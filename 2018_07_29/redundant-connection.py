import collections


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)

        def dfs(s, t):
            if s not in visited:
                visited.add(s)
                if s == t: return True
                return any(dfs(n, t) for n in graph[s])

        for u, v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)
