# Definition for a undirected graph node
# z这里需要向考官问清楚 neighbors 是怎么存储
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        import collections
        copy = UndirectedGraphNode(node.label)
        visted = {node: copy}
        queue = collections.deque([node])
        newNode = None
        while queue:
            node = queue.popleft()
            newNode = visted.get(node, None) or UndirectedGraphNode(node.label)
            visted[node] = newNode
            for n in node.neighbors:
                if not n in visted:
                    queue.append(n)
                visted[n] = visted.get(n, None) or UndirectedGraphNode(n.label)
                newNode.neighbors.append(visted[n])
        return copy


courses={}
courses.get(1, [])
