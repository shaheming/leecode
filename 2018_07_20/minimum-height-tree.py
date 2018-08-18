class Solution(object):
    def buildTree(self, root, val, edges):
        print(self.tree)
        print(root)
        for edge in edges:
            if val in edge:
                edge.remove(val)
                root[edge[0]] = {}
                edges.remove(edge)
        for k, v in root.items():
            self.buildTree(v, k, edges)

    def findMaxPath(self, nodes, path, maxpath):
        for k, v in nodes.items():
            path.append(k)
        if len(path) > len(maxpath):
            maxpath = path
        return maxpath

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]

        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1: new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


s = Solution()
n = 4
edges = [[1, 0], [1, 2], [1, 3]]
s.findMinHeightTrees(n, edges)
