import collections


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        # 1 exit invalid variable(not exits in Equations) -1
        # 2 two same variable in Equations 1.0
        # 3 two variable
        if len(equations) == 0:
            return [-1.0 for _ in range(len(queries))]

        tree = self.buildGraph(equations, values)

        paths = self.bfs(tree)

        res = []

        for querie in queries:
            q = " ".join(querie)
            if q in paths:
                res.append(paths[q])
            elif q[::-1] in paths:
                res.append(1 / paths[q[::-1]])
            else:
                res.append(-1.0)
        return res

    def buildGraph(self, equations, values):
        graph = {}
        for eq, v in zip(equations, values):
            graph[eq[0]] = graph.get(eq[0], {})
            graph[eq[0]][eq[1]] = graph[eq[0]].get(eq[1], v)
            graph[eq[1]] = graph.get(eq[1], {})
            graph[eq[1]][eq[0]] = graph[eq[1]].get(eq[0], 1 / v)
        return graph

    def bfs(self, graph):
        res = {}
        for n in graph.keys():
            queue = collections.deque([[n, 1.0]])
            visited = set()
            while len(queue) != 0:
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    visited.add(node[0])
                    res[n+' '+node[0]] = node[1]
                    for k, v in graph[node[0]].items():
                        if k not in visited:
                            # print(node[1],graph)
                            queue.append([k, node[1] * v])
        return res
