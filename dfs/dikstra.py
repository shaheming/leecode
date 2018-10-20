class Solution:
    def dikstra(self,start ,n, nodes):
        print(n)
        graph = [[float('inf')] * n for _ in range(n)]
        distance = [[float('inf')] * n for _ in range(n)]
        # build graph
        for u, v, d in nodes:
            graph[u][v] = d
        for i in range(n):
            graph[i][i] = 0
        visted = set([start])
        vertex = set([i for i in range(n)])
        # add note
        # update distance
        distance = [float('inf') for _ in range(n)]
        print(distance)
        distance[0] = 0
        while len(visted) < n:
            tmp = {"dis": float('inf'), 'u': -1, 'v': -1}
            noVisted = vertex - visted
            for u in visted:
                for v in noVisted:
                    if graph[u][v] < tmp["dis"]:
                        tmp["dis"] = graph[u][v]
                        tmp['u'] = u
                        tmp['v'] = v
            print(visted)
            distance[tmp['v']] = min(
                distance[tmp['u']] + tmp['dis'], distance[tmp['v']])
            if tmp['v'] != -1:
              visted.add(tmp['v'])
              for i in range(n):
                  if graph[tmp['v']][i] < float('inf'):
                      distance[i] = min(
                          distance[i], distance[tmp['v']]+graph[tmp['v']][i])
        print(distance)


nodes = []
with open('test.txt') as f:
    for line in f:
        nodes.append([int(i) for i in line.split(" ")])
import time
start = time.time()        
s = Solution()
s.dikstra(0, 6, nodes)
print(time.time() - start)
