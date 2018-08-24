import collections


# 这是一个拓扑排序
# 思路是不断将孤立点提出来
# 首先构造一个图的全部关系
# 不断抽出入度为零的点找出来
# 用另一个dic构造兄弟关系将子节点的父亲节点关系刻画出来
# 不断剔除入度为零的点更新子节点的关系
# 这里用了python的 collection 库，和队列库
# collection库可以直接 for key in dict
# dfs用压栈
# bfs用队列
class Solution:
    def findOrder1(self, numCourses, prerequisites):
        neigh = collections.defaultdict(set)
        dic = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [node for node in range(numCourses) if not dic[node]]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for n in neigh[node]:
                dic[n].remove(node)
                if not dic[n]:
                    stack.append(n)
            dic.pop(node)
        return res if not dic else []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []

    # 用邻接表做的 bfs 效率不够 n*n
    def findOrder3(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[i][j] = 1
        queue = collections.deque([index for index, node in enumerate(graph) if all([n == 0 for n in node])])

        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in range(numCourses):
                if graph[i][node] == 1:
                    graph[i][node] = 0
                    if all([n == 0 for n in graph[i]]):
                        queue.append(i)
        return res if count == numCourses else []

    def findOrder1(self, numCourses, prerequisites):

        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)

        queue = collections.deque([i for i in dic if not dic[i]])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if len(res) == numCourses else []


s = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(s.findOrder3(numCourses, prerequisites))
print(s.findOrder(numCourses, prerequisites))
print(s.findOrder1(numCourses, prerequisites))
