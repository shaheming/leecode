# 1. build adjacency list
# 2. build indegree map
# 3. bfs


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True

        indegrees = self.getIndegree(numCourses, prerequisites)
        topCourses = self.findFirstCourses(indegrees)
        visited = set([])
        if len(topCourses) == 0:
            return False

        import collections
        allCourses = self.buildCourseRelation(numCourses, prerequisites)
        queue = collections.deque(topCourses)

        while queue:
            course = queue.popleft()
            nextCourses = allCourses[course]
            visited.add(course)
            for c in nextCourses:
                indegrees[c] -= 1
                if indegrees[c] == 0:
                    queue.append(c)
        return len(visited) == numCourses

    def buildCourseRelation(self, numCourses, prerequisites):
        courses = {}
        for preCourse, nextCourse in prerequisites:
            courses[preCourse] = courses.get(preCourse, [])
            courses[preCourse].append(nextCourse)
        for c in list(set(range(numCourses)) - set(courses.keys())):
            courses[c] = []
        return courses

    def findFirstCourses(self, indegrees):
        res = []
        for k, v in indegrees.items():
            if v == 0:
                res.append(k)
        return res

    def getIndegree(self, numCourses, prerequisites):
        indegrees = {}
        for p, n in prerequisites:
            indegrees[n] = indegrees.get(n, 0) + 1
        for c in list(set(range(numCourses)) - set(indegrees.keys())):
            indegrees[c] = 0
        return indegrees
