import heapq


class Edge:
    def __init__(self, fromNode, to, distance=float('inf')):
        self.fromNode = fromNode
        self.to = to
        self.distance = distance


class Solution:
    def dikstra(self, start, n, nodes):
        # graph = [[float('inf')] * n for _ in range(n)]
        graph = [[] for _ in range(n)]
        distance = [[float('inf')] * n for _ in range(n)]
        parents = [[-1] * n for _ in range(n)]
        # build graph
        for u, v, d in nodes:
            graph[u].append(Edge(u, v, d))

        for i in range(n):
            graph[i] = sorted(graph[i], key=lambda g: g.distance)

        visted = set([start])
        vertex = set([i for i in range(n)])
        # add note
        # update distance
        distance = [float('inf') for _ in range(n)]
        distance[start] = 0
        pqueue = []

  
        heapq.heappush(pqueue, (0, start))
        while len(visted) < n and pqueue:
            node = heapq.heappop(pqueue)
            distance[node[1]] = node[0]
            #for m edges and k*n nodes in queue
            # O(mlong(k*n))
            for n_ in graph[node[1]]:
                if n_.to not in visted:
                    heapq.heappush(
                        pqueue, (min(n_.distance + distance[n_.fromNode], distance[n_.to]), n_.to))
            visted.add(node[1])
        print(distance)
nodes = []
with open('test.py') as f:
    for line in f:
        data = line.split(" ")
        u = int(data[0])
        v = int(data[1])
        d = float(data[2])
        nodes.append([u, v, d])
import time
start = time.time()
s = Solution()
s.dikstra(0, 6, nodes)
print(time.time() - start)
# [0, 10, 20, 40, 20, 21]
