import collections
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #1. build adjacent chart
        #2. select a node bfs, and record visted node
        #3. iterate when there is no visted nodes
        if n < 2:
            return n
        
        nodes = self.buildAdjacent(n, edges)
        visted = set([])
        res = 0
        
        for node in range(n):
            if not node in visted:
                visted = self.bfs(node, visted, nodes)
                res += 1
        return res
    
    def buildAdjacent(self, n, edges):
        nodes = [set([]) for i in range(n)]
        for v1, v2 in edges:
            nodes[v1].add(v2)
            nodes[v2].add(v1)
        return nodes
    
    def bfs(self, node, visted, nodes):
        queue = collections.deque([node])
        while queue:
            n = queue.popleft()
            visted.add(n)
            for i in list(nodes[n]):
                if not i in visted:
                    queue.append(i)
        return visted
        
        
        