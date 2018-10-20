N = 10


class Solution:
    def isDag(self, n, edges):
        nodes = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        visited = [0 for _ in range(n)]
        for s, e in edges:
            nodes[s].append(e)
            degree[e] += 1
        if 0 in degree:
            for i in range(n):
                if degree[i] == 0 and visited[i] == 0:
                    if not self.dfs(nodes, visited, i, []):
                        return False
        else:
            return self.dfs(nodes, visited, 0, [])
        return True

    def dfs(self, nodes, visited, node, path):
        visited[node] = 1
        path.append(node)
        for n in nodes[node]:
            if visited[n] == 0:
                if not self.dfs(nodes, visited, n, path):
                    return False
            elif visited[n] == 1:
                print path[path.index(n):] + [n]
                return False
        path.pop()
        visited[node] = 2
        return True


N = 6
edges = [(0, 1), (1, 2), (0, 3), (3, 4), (3, 5), (5, 0)]
s = Solution()
s.isDag(N, edges)




isDag(n,edges):
Find nodes with indegree is zore
if nodes exit:
  for n in nodes
    dfs(n,path)
else
  dfs(randomeNone,path) to print the cycle


dfs(node, path):
mark node is visited
path add node
for n in node's neighbors
  if n is not marked as visted
      dfs(n, path)
      if find cycle:
        return False
      endif
  elif n is marked as visted:
    print cycle, path[n.index:end] + [n]
    return False
remove node from path 
mark node's descendants are visted
return True
    
