class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        if len(edges) == 0:
            return True

        edgesMap = {}
        for i, j in edges:
            if i in edgesMap:
                edgesMap[i].add(j)
            else:
                edgesMap[i] = set([j])

            if j in edgesMap:
                edgesMap[j].add(i)
            else:
                edgesMap[j] = set([i])

        import collections
        queue = collections.deque([edges[0][0]])
        nodes = set([])

        while queue:
            node = queue.popleft()
            nodes.add(node)
            for nd in list(edgesMap[node]):
                if not nd in nodes:
                    queue.append(nd)

        return len(nodes) == n
