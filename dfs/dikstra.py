class Edge:
  def __init__(self,fromNode ,to,distance=float('inf')):
    self.fromNode  = fromNode 
    self.to = to
    self.distance = distance

class Solution:
    def dikstra(self, start, n, nodes):
        print(n)
        # graph = [[float('inf')] * n for _ in range(n)]
        graph = [[] for _ in range(n)]
        distance = [[float('inf')] * n for _ in range(n)]
        # build graph
        for u, v, d in nodes:
          graph[u].append(Edge(u,v,d))

        for i in range(n):
          graph[i] = sorted(graph[i], key=lambda g:g.distance)

        visted = set([start])
        vertex = set([i for i in range(n)])
        # add note
        # update distance
        distance = [float('inf') for _ in range(n)]
        distance[0] = 0
        while len(visted) < n:
            tmp = {"dis": float('inf'), 'u': -1, 'v': -1}
            noVisted = vertex - visted
            for u in visted:
              for e in graph[u]:
                if e.to in noVisted:
                  tmp["dis"] = e.distance
                  tmp['u'] = e.fromNode 
                  tmp['v'] = e.to
                  break
        
            distance[tmp['v']] = min(distance[tmp['u']] + tmp['dis'], distance[tmp['v']])
            
            if tmp['v'] != -1:
                visted.add(tmp['v'])
                for node in graph[tmp['v']]:
                        distance[node.to] = min(
                            distance[node.to], distance[node.fromNode] + distance[tmp['v']])


nodes = []
with open('test.txt') as f:
    for line in f:
        data = line.split(" ")
        u = int(data[0])
        v = int(data[1])
        d = float(data[2])
        nodes.append([u, v, d])
import time
start = time.time()
s = Solution()
s.dikstra(0, 1000, nodes)
print(time.time() - start)
# [0, 10, 20, 40, 20, 21]
